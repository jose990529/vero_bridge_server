from verobridge_api import handle_request

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("verobridge_api:app", host="0.0.0.0", port=8000)