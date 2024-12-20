from flask import Flask, jsonify, request
from script_extract import script_extract
from modele import modele

app = Flask(__name__)

@app.route('/get_features', methods=['POST'])
def get_features():
    directory = request.json.get('directory')
    features = script_extract(directory)
    model = modele(features)
    # Retourner les résultats du modèle ou les caractéristiques extraites
    return jsonify(features)

if __name__ == '__main__':
    app.run(debug=True)

