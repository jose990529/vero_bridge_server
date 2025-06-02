
def handle_request(payload):
    import os
    import subprocess
    orden = payload.get("orden", "")
    if not orden:
        return {"status": "error", "message": "Orden vacía"}
    try:
        resultado = subprocess.getoutput(orden)
        return {"status": "ok", "resultado": resultado}
    except Exception as e:
        return {"status": "error", "message": str(e)}
