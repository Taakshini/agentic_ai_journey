#install  pip install fastapi uvicorn
from fastapi import FastAPI
app=FastAPI()

@app.get("/hi/{name}")
async def main(name):
    return f"hello {name}"
