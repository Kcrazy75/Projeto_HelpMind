import os
from fastapi import FastAPI

app = FastAPI()
NODE_ID = os.getenv("NODE_ID", "?")


@app.get("/health")
def health():
    return {"status": "ok", "node": NODE_ID}