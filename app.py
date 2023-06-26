from flask import Flask, render_template, jsonify
from GameOfLife import jeu_de_la_vie, initialiser_grille

app = Flask(__name__)
grille = None
iterations = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_of_life')
def game_of_life():
    global grille, iterations
    grille = initialiser_grille(10, 10)  # a chnager
    iterations = 20

    return render_template('game_of_life.html', grille=grille.tolist())

@app.route('/update_grid')
def update_grid():
    global grille, iterations
    grille_generator = jeu_de_la_vie(grille, iterations)
    grille = next(grille_generator, None)
    iterations -= 1

    return jsonify(grille=grille, iterations=iterations)



if __name__ == '__main__':
    app.run()
