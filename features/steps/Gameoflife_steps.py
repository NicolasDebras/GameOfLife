from behave import given, when, then
import numpy as np
from GameofLife import initialize_grid, update_grid 
from contextlib import suppress
import pytest

#---------------------------------------------------------------------------------
@given('a file with a grid configuration')
def step_given_file(context):
    context.file_path = "file/testfile/glider.txt"

@when('I initialize the grid from this file')
def step_initialize_grid(context):
    context.grid, context.num_cells_height, context.num_cells_width = initialize_grid(context.file_path)

@then('I should get the correct grid with the right number of cells in height and width')
def step_check_grid(context):
    expected_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ])
    assert np.array_equal(context.grid, expected_grid)
    assert context.num_cells_height == 5
    assert context.num_cells_width == 5

#---------------------------------------------------------------------------------
@given('a random grid of size 5x5')
def step_given_random_grid(context):
    context.grid = np.random.randint(2, size=(5, 5))

@when('I update the grid')
def step_update_grid(context):
    context.updated_grid = update_grid(context.grid, 5, 5)

@then('the size of the grid should remain the same')
def step_check_grid_size(context):
    assert context.updated_grid.shape == context.grid.shape

#---------------------------------------------------------------------------------
@given('an invalid file')
def step_given_invalid_file(context):
    context.file_path = "file/testfile/invalid_file.txt"

@when('I try to initialize the grid')
def step_try_initialize_grid(context):
    with suppress(ValueError):
        context.grid, context.num_cells_height, context.num_cells_width = initialize_grid(context.file_path)

@then('I should receive an error')
def step_check_error(context):
    with pytest.raises(ValueError):
        context.grid, context.num_cells_height, context.num_cells_width = initialize_grid(context.file_path)

#---------------------------------------------------------------------------------

@given('a grid with all cells dead')
def step_given_dead_grid(context):
    context.grid = np.zeros((5, 5), dtype=int)

@when('Update the grid')
def step_update_grid(context):
    context.updated_grid = update_grid(context.grid, 5, 5)

@then('the grid should remain the same')
def step_check_same_grid(context):
    assert np.array_equal(context.updated_grid, context.grid)