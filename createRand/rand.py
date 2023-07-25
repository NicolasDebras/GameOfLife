import random

width, height = 100, 100

with open('file/random_grid.txt', 'w+') as f:
    f.write(f"Generation 1:\n")
    f.write(f"{width} {height}\n")
    for _ in range(height):
        line = ''.join('*' if random.random() > 0.5 else '.' for _ in range(width))
        f.write(line + "\n")