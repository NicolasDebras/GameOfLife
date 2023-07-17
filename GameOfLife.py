import tkinter as tk
from tkinter import filedialog
import pygame
import numpy as np
import time

def initialize_grid(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    if not lines or lines[0] != "Generation 1:":
        raise ValueError("The first line of the file must be 'Generation 1:'")
    
    size_info = lines[1]
    if not size_info:
        raise ValueError("The file must contain the size of the grid on the second line.")

    num_cells_height, num_cells_width = map(int, size_info.split())
    grid_info = lines[2:]
    
    if len(grid_info) != num_cells_height:
        raise ValueError("The height of the grid in the file does not match the specified size.")
    
    for row in grid_info:
        if len(row) != num_cells_width:
            raise ValueError("The width of a row in the grid does not match the specified size.")
    
    grid = np.zeros((num_cells_height, num_cells_width), dtype=int)

    for i, row in enumerate(grid_info):
        for j, cell in enumerate(row):
            if cell == '*':
                grid[i][j] = 1
                
    return grid, num_cells_height, num_cells_width

def update_grid(grid, num_cells_height, num_cells_width):
    new_grid = grid.copy()
    for i in range(num_cells_height):
        for j in range(num_cells_width):
            total = (grid[i, (j-1)%num_cells_width] + grid[i, (j+1)%num_cells_width] + grid[(i-1)%num_cells_height, j] + grid[(i+1)%num_cells_height, j] 
                    + grid[(i-1)%num_cells_height, (j-1)%num_cells_width] + grid[(i-1)%num_cells_height, (j+1)%num_cells_width] + grid[(i+1)%num_cells_height, (j-1)%num_cells_width] + grid[(i+1)%num_cells_height, (j+1)%num_cells_width])
            if grid[i, j]  == 1 and (total < 2 or total > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and total == 3:
                new_grid[i, j] = 1
    return new_grid

def select_file():
    try:
        file_path = filedialog.askopenfilename()
        print("Fichier sélectionné :", file_path)

        grid, num_cells_height, num_cells_width = initialize_grid(file_path)

        pygame.init()
        screen_size = (800, 800)
        screen = pygame.display.set_mode(screen_size)
        clock = pygame.time.Clock()

        cell_size_width = screen_size[0] // num_cells_width
        cell_size_height = screen_size[1] // num_cells_height

        alive = (255, 255, 255)
        dead = (0, 0, 0)
        running = True

        while running:
            screen.fill(dead)
            time.sleep(0.05)
            for i in range(num_cells_height):
                for j in range(num_cells_width):
                    if grid[i][j] == 1:
                        pygame.draw.rect(screen, alive, pygame.Rect(j*cell_size_width, i*cell_size_height, cell_size_width, cell_size_height))
            
            grid = update_grid(grid, num_cells_height, num_cells_width)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

window = tk.Tk()
select_button = tk.Button(window, text="Sélectionner un fichier", command=select_file)
select_button.pack()
window.mainloop()
