
from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

# Ruta base donde se ejecutarán las órdenes (ajustar si necesario)
BASE_DIR = "D:/proyecto/Vero 2.0"

@app.route("/", methods=["GET"])
def index():
    return "✅ Vero está en línea, lista para ejecutar órdenes"

@app.route("/orden", methods=["POST"])
def recibir_orden():
    data = request.get_json()
    comando = data.get("comando")

    if comando == "crear_archivo_prueba":
        try:
            ruta = os.path.join(BASE_DIR, "core", "archivo_prueba.txt")
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(f"Archivo de prueba creado el {datetime.datetime.now()}")
            return jsonify({"status": "ok", "mensaje": "Archivo creado con éxito"}), 200
        except Exception as e:
            return jsonify({"status": "error", "mensaje": str(e)}), 500
    else:
        return jsonify({"status": "error", "mensaje": "Comando no reconocido"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
