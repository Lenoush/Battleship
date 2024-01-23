import pytest
from src.matrice import create_grid, plot_grid, plot_flotte_grid

def test_create_grid():
    matrice = create_grid()
    assert len(matrice) == 10 
    assert all(len(row) == 10 for row in matrice) 
    assert all(cell == "." for row in matrice for cell in row)  

