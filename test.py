import pytest
import numpy as np
from GameofLife import initialize_grid, update_grid 

def test_initialize_grid():
    file_path = "file/testfile/glider.txt"  
    grid, num_cells_height, num_cells_width = initialize_grid(file_path)
    expected_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ])
    assert np.array_equal(grid, expected_grid)
    assert num_cells_height == 5
    assert num_cells_width == 5

def test_update_size_grid():
    grid = np.random.randint(2, size=(5, 5))  # Grille rand de taille 5x5
    updated_grid = update_grid(grid, 5, 5)
    assert updated_grid.shape == (5, 5) 

def test_initialize_grid_invalid_file():
    file_path = "file/testfile/invalid_file.txt"  
    with pytest.raises(ValueError):
        grid, num_cells_height, num_cells_width = initialize_grid(file_path)

def test_update_grid_stable_dead():
    grid = np.zeros((5, 5), dtype=int)  #
    updated_grid = update_grid(grid, 5, 5)
    assert np.array_equal(updated_grid, grid)

