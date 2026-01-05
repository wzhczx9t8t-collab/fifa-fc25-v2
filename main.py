from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Données FIFA
EQUIPES_FIFA = ["Paris-SG", "Marseille", "Lyon", "Real Madrid", "Barcelona", "Bayern Munich"]

@app.route('/')
def accueil():
    return jsonify({"API": "FIFA FC25 Predictor", "status": "prête"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    equipe1 = data.get('home')
    equipe2 = data.get('away')

    if equipe1 not in EQUIPES_FIFA or equipe2 not in EQUIPES_FIFA:
        return jsonify({"erreur": "Équipe non trouvée"}), 400

    score1 = random.randint(0, 4)
    score2 = random.randint(0, 3)
    confiance = random.randint(70, 95)

    return jsonify({
        "prediction": {
            "match": f"{equipe1} vs {equipe2}",
            "score": f"{score1}-{score2}",
            "confiance": f"{confiance}%"
        }
    })

if __name__ == '__main__':
    app.run()
