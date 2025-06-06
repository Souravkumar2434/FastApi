from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}