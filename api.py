import json
from flask import Flask, jsonify

app = Flask(__name__)

# Chemin du fichier JSON
json_file = 'top8_manga.json'

# Lecture du fichier JSON
with open(json_file, 'r') as f:
    data = json.load(f)

# Création d'une route pour renvoyer les données sous forme de JSON
@app.route('/top8', methods=['GET'])
def get_top8():
    return jsonify(data)

# Création d'une route pour renvoyer un manga spécifique sous forme de JSON
@app.route('/manga/<int:classement>', methods=['GET'])
def get_manga(classement):
    for manga in data:
        if manga['classement'] == str(classement):
            return jsonify(manga)
    return jsonify({'error': 'Manga non trouvé'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)