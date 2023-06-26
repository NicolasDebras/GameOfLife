from flask import Flask, render_template
import numpy as np
import time

app = Flask(__name__)

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
        time.sleep(0.5)
        yield grille.tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_of_life')
def game_of_life():
    # Taille de la grille
    n = 10  # Remplacez par votre taille souhaitée
    m = 10  # Remplacez par votre taille souhaitée

    grille = np.random.choice([0, 1], size=(n, m), p=[0.7, 0.3])

    # Nombre d'itérations
    iterations = 20

    return render_template('game_of_life.html', grille=grille.tolist(), iterations=iterations)

if __name__ == '__main__':
    app.run()
