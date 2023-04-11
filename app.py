from flask_cors import CORS
from flask import Flask, request, jsonify
from doploon_optimization import doploon_optimizator
import json


app = Flask(__name__)
CORS(app)

@app.route('/optimization', methods=['POST'])
def media():
    data = request.get_json()
    dataJson = data['dataJson']
    values = json.loads(dataJson)
    result = doploon_optimizator(
        int(values["doploons"]),
        int(values["small"]),
        int(values["medium"]),
        int(values["great"]),
        int(values["powerful"])
    )

    return jsonify({'result': result})

