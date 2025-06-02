
from flask import Flask, request, jsonify
from verobridge_api import handle_request

app = Flask(__name__)

@app.route("/ordenes", methods=["POST"])
def recibir_orden():
    data = request.get_json()
    resultado = handle_request(data)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
