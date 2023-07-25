Feature: Game of Life
  As a player of the game of life
  I want the grid work properly
  So that the game can proceed as expected

  Scenario: Initialize the grid from a file
    Given a file with a grid configuration
    When I initialize the grid from this file
    Then I should get the correct grid with the right number of cells in height and width

  Scenario: Update the grid size
    Given a random grid of size 5x5
    When I update the grid
    Then the size of the grid should remain the same

  Scenario: Initialize the grid with an invalid file
    Given an invalid file
    When I try to initialize the grid
    Then I should receive an error

  Scenario: Update the grid with all cells dead
    Given a grid with all cells dead
    When update the grid
    Then the grid should remain the same