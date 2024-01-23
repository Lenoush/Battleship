import pytest
from src.utils import (
    string_from_pos, 
    random_position, 
    random_orientation, 
    pos_from_string, 
    id_taille_Nom, 
    check_fin_partie
)

@pytest.mark.parametrize("input_position, expected_output", [
    ((0, 0), ('a', 0)),
    ((3, 9), ('d', 9)),
    ((5, 7), ('f', 7)),
])
def test_string_from_pos(input_position, expected_output):
    result = string_from_pos(input_position)
    assert result == expected_output


@pytest.mark.parametrize("input_string, expected_output", [
    ('a2', (0, 2)),
    ('f7', (5, 7)),
    ('d9', (3, 9))
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


def test_random_position():
    position = random_position()
    assert position[0] >= 0 and position[0] < 10
    assert position[1] >= 0 and position[1] < 10


def test_random_orientation():
    orientation = random_orientation()
    assert orientation in ["v", "h"]


def test_check_fin_partie():
    assert check_fin_partie("Joueur1", "MaMatrice", ["Transporteur", "Cuirassé"], 7) == False 