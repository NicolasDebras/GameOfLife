import numpy as np
import os
import time

def jeu_de_la_vie(grille, iterations):
    for it in range(iterations):
        nouvelle_grille = np.copy(grille)
        for i in range(n):
            for j in range(m):
                nb_voisins = np.sum(grille[max(0, i-1):min(n, i+2), max(0, j-1):min(m, j+2)]) - grille[i, j]
                if grille[i, j] == 1 and (nb_voisins < 2 or nb_voisins > 3):
                    nouvelle_grille[i, j] = 0
                elif grille[i, j] == 0 and nb_voisins == 3:
                    nouvelle_grille[i, j] = 1
        grille = nouvelle_grille
        it = os.system('cls' if os.name == 'nt' else 'clear')
        for row in grille:
            print(' '.join(['*' if cell == 1 else ' ' for cell in row]))
        time.sleep(0.5)

# Taille de la grille
print("Veuillez sasir la taille de la grille")
nStr = input()
mStr = input()

try:
    n = int(nStr)
    m = int(mStr)
except:
    print("Input mauvais")
    raise

grille = np.random.choice([0, 1], size=(n, m), p=[0.7, 0.3])

# Nombre d'itérations 
iterations = 20

jeu_de_la_vie(grille, iterations)
