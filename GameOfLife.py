import numpy as np
import time

def jeu_de_la_vie(grille, iterations):
    for it in range(iterations):
        nouvelle_grille = np.copy(grille)
        for i in range(len(grille)):
            for j in range(len(grille[0])):
                nb_voisins = np.sum(grille[max(0, i-1):min(len(grille), i+2), max(0, j-1):min(len(grille[0]), j+2)]) - grille[i, j]
                if grille[i, j] == 1 and (nb_voisins < 2 or nb_voisins > 3):
                    nouvelle_grille[i, j] = 0
                elif grille[i, j] == 0 and nb_voisins == 3:
                    nouvelle_grille[i, j] = 1
        grille = nouvelle_grille
        yield grille.tolist()


def initialiser_grille(n, m):
    return np.random.choice([0, 1], size=(n, m), p=[0.7, 0.3])
