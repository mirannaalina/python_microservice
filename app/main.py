from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "say kasse"}

@app.get("/data/{name}")
async def read_data(name: str):
    return {"message": f"Hell on World {name}"}
