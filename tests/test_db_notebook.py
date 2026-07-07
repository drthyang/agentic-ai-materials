from matdiscover.db import CandidateDB, CandidateRow
from matdiscover.notebook import LabNotebook


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
