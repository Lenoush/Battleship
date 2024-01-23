import pytest
from src.bateau import presence_bateau, id_bateau_at_pos, nouveau_bateau, input_ajout_bateau

# Utilisez ce décorateur pour simuler une entrée utilisateur dans vos tests
from unittest.mock import patch

@pytest.mark.parametrize("input_position, flotte, expected_output", [
    ((0, 0), [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}], True),
    ((1, 1), [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}], False)
])
def test_presence_bateau(input_position, flotte, expected_output):
    assert presence_bateau(input_position, flotte) == expected_output


@pytest.mark.parametrize("input_position, flotte, expected_output", [
    ((0, 0), [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}], 0),
    ((2, 3), [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}], 1),
    ((3, 3), [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}], 1)
])
def test_id_bateau_at_pos(input_position, flotte, expected_output):
    assert id_bateau_at_pos(input_position, flotte) == expected_output


def test_nouveau_bateau():
    flotte = [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}]
    assert nouveau_bateau(flotte, "Cuirassé", (4, 4), "h") == None  

# Test de la fonction input_ajout_bateau
# @patch("builtins.input", side_effect=["a0", "v"])
# def test_input_ajout_bateau(mock_input):
#     flotte = [{"pos": [(0, 0), (0, 1)]}, {"pos": [(2, 3), (3, 3)]}]
#     with pytest.raises(GameOverException, match="Cuirassé a gagné en 10 tours"):
#         input_ajout_bateau(flotte, "Cuirassé")

# # Ajoutez d'autres tests au besoin
