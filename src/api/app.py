from fastapi import FastAPI

app = FastAPI()


@app.get("/suma")
def suma(a: int, b: int):
    return a + b


@app.get("/resta")
def resta(
    a: int,
    b: int,
):
    return a - b


@app.get("/mult")
def resta(
    a: int,
    b: int,
):
    return a * b