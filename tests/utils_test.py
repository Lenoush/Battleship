import pytest
from src.utils import (
    string_from_pos,
    pos_from_string,
    id_taille_Nom
)

@pytest.mark.parametrize("input_position, expected_output", [
    ((0, 0), ('a', 0)),
    ((5, 8), ('f', 8)),
])
def test_string_from_pos(input_position, expected_output):
    result = string_from_pos(input_position)
    assert result == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ('a2', (0, 2)),
    ('f7', (5, 7)),
])
def test_pos_from_string(input_string, expected_output):
    result = pos_from_string(input_string)
    assert result == expected_output

@pytest.mark.parametrize("input_nom, expected_output", [
    ('Transporteur', 0),
    ('Cuirassé', 1),
    ('Croisseur', 2),
    ('Sous-marin', 3),
    ('Destructeur', 4)
])
def test_id_taille_Nom(input_nom, expected_output):
    result = id_taille_Nom(input_nom)
    assert result == expected_output
