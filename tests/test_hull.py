"""The hull must be on CHGNet's energy scale: MP2020-corrected.

CHGNet is trained on MPtrj energies that carry MP2020 compatibility
corrections. Until 2026-10 the hull was built from MP's *uncorrected*
energies, which put zinc-blende CaO, MgO and KCl exactly on the hull and
made every chalcogenide candidate look ~0.03-0.2 eV/atom more stable than it
is. The hermetic tests pin the wiring; the network test (opt-in) pins the
physics on real MP data.
"""

from __future__ import annotations

import json
import os

import pytest
from pymatgen.core import Structure

from athanor.tools import scoring

# A toy Ca-O system on two scales. The anion correction lowers CaO's energy
# by 0.687 eV per O atom, as MP2020 does; elements carry no correction.
ROWS = [
    {"entry_id": "Ca", "formula": "Ca1", "energy": -2.00, "uncorrected_energy": -2.00},
    {"entry_id": "O2", "formula": "O2", "energy": -9.86, "uncorrected_energy": -9.86},
    {"entry_id": "CaO", "formula": "Ca1 O1", "energy": -13.18,
     "uncorrected_energy": -13.18 + 0.687},
]


def test_hull_uses_corrected_energies_by_default():
    # a polymorph 0.15 eV/atom above rock-salt CaO on the corrected scale
    e_total = -13.18 + 2 * 0.15
    assert scoring.hull_distance(ROWS, "CaO", e_total) == pytest.approx(0.15, abs=1e-6)


def test_uncorrected_scale_reproduces_the_old_bug():
    # on the raw scale the same candidate sits below the hull -> distance 0
    assert scoring.hull_distance(ROWS, "CaO", -13.18 + 0.30, corrected=False) == 0.0


def test_no_entries_means_no_hull():
    assert scoring.hull_distance([], "CaO", -10.0) is None


def test_e_above_hull_wires_chgnet_energy_into_the_corrected_hull(monkeypatch):
    monkeypatch.setenv("MP_API_KEY", "x")
    monkeypatch.setattr(scoring, "hull_entries", lambda chemsys, use_cache=True: ROWS)

    class FakeCHGNet:
        def predict_structure(self, s):
            return {"e": (-13.18 + 0.30) / len(s)}  # eV/atom, as CHGNet returns

    monkeypatch.setattr(scoring, "_chgnet", lambda: FakeCHGNet())
    s = Structure.from_spacegroup("Fm-3m", [[4.8, 0, 0], [0, 4.8, 0], [0, 0, 4.8]],
                                  ["Ca", "O"], [[0, 0, 0], [0.5, 0.5, 0.5]])
    s = s.get_primitive_structure()  # 2 atoms
    assert scoring.e_above_hull(s) == pytest.approx(0.15, abs=1e-6)


def test_hull_entries_read_from_cache_without_network(tmp_path, monkeypatch):
    monkeypatch.setattr(scoring, "_HULL_CACHE", tmp_path)
    (tmp_path / "Ca-O.json").write_text(json.dumps(ROWS))
    assert scoring.hull_entries("Ca-O") == ROWS


@pytest.mark.network
@pytest.mark.skipif(not (os.environ.get("ATHANOR_NETWORK_TESTS") and os.environ.get("MP_API_KEY")),
                    reason="set ATHANOR_NETWORK_TESTS=1 and MP_API_KEY")
@pytest.mark.parametrize("cation,anion,a,above", [
    ("Ca", "O", 5.2, True), ("Mg", "O", 4.6, True), ("K", "Cl", 7.0, True),
    ("Zn", "S", 5.41, False), ("Zn", "Se", 5.67, False), ("Cd", "Te", 6.48, False),
])
def test_zinc_blende_regression_on_real_mp_data(cation, anion, a, above):
    """Rock-salt formers forced into zinc blende must sit well above the hull;
    true zinc-blende semiconductors must sit within the 0.05 eV/atom window."""
    from athanor.prototypes import get_prototype

    s = get_prototype("zincblende-GaAs").copy()
    s.replace_species({"Ga": cation, "As": anion})
    s.scale_lattice(a ** 3)
    relaxed, converged = scoring.relax_structure(s, max_steps=200)
    assert converged
    hull = scoring.e_above_hull(relaxed)
    if above:
        assert hull > 0.10, hull
    else:
        assert hull < 0.05, hull
