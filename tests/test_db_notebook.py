import pytest

from athanor.db import CandidateDB, CandidateRow
from athanor.notebook import LabNotebook


def test_db_roundtrip(tmp_path):
    db = CandidateDB(tmp_path / "c.db")
    db.add(CandidateRow(
        iteration=1, formula="AgGaTe2", status="scored",
        parent_prototype="chalcopyrite", substitution={"Cu": "Ag", "In": "Ga", "Se": "Te"},
        hypothesis="heavier anions narrow the gap",
        converged=True, formation_energy_per_atom=-0.42,
        e_above_hull=0.021, band_gap_ev=1.32, is_novel=True,
    ))
    db.add(CandidateRow(iteration=1, formula="PbS", status="filtered_out",
                        filter_reasons=["contains excluded elements: ['Pb']"]))

    assert db.already_seen("AgGaTe2")
    assert not db.already_seen("CuInSe2")

    top = db.top_candidates()
    assert len(top) == 1
    assert top[0]["formula"] == "AgGaTe2"

    summary = db.iteration_summary(1)
    assert summary == {"scored": 1, "filtered_out": 1}
    db.close()


def test_notebook_write_read(tmp_path):
    nb = LabNotebook(tmp_path / "nb.md")
    nb.write("hypothesis", 1, "Try Ag-for-Cu substitution.")
    nb.write("observation", 1, "AgGaTe2 near hull, gap 1.32 eV.")
    nb.write("reflection", 1, "Te-based chalcopyrites look promising.")

    full = nb.read()
    assert "hypothesis" in full and "reflection" in full

    last = nb.read(last_n_entries=1)
    assert "reflection" in last
    assert "hypothesis" not in last


def test_notebook_rejects_bad_type(tmp_path):
    nb = LabNotebook(tmp_path / "nb.md")
    try:
        nb.write("rant", 1, "nope")
        raised = False
    except ValueError:
        raised = True
    assert raised


# --- elemental references: an MP failure must not become a silent FCC cell ---

def test_reference_lookup_raises_when_mp_fails(monkeypatch):
    import mp_api.client

    from athanor.tools import _references

    class Broken:
        def __init__(self, *a, **k):
            raise ConnectionError("MP down")

    monkeypatch.setenv("MP_API_KEY", "x")
    monkeypatch.setattr(mp_api.client, "MPRester", Broken)
    with pytest.raises(ConnectionError):
        _references._elemental_structure("S")


def test_reference_without_key_is_labelled_fallback(monkeypatch):
    from athanor.tools import _references

    monkeypatch.delenv("MP_API_KEY", raising=False)
    s, source = _references._elemental_structure("Se")
    assert source == "fcc-fallback" and len(s) == 4


def test_reference_cache_records_its_source(monkeypatch, tmp_path):
    from athanor.tools import _references

    monkeypatch.setattr(_references, "_CACHE", tmp_path / "refs.json")
    monkeypatch.setattr(_references, "_memory", {})
    (tmp_path / "refs.json").write_text('{"Cu": {"e": -4.08, "source": "mp-30"}}')
    assert _references.elemental_reference_energy("Cu") == -4.08
