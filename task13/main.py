from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Numbers(BaseModel):
    num1: float
    num2: float


@app.post("/calculate")
def calculate(data: Numbers):
    return {"result": data.num1 + data.num2}

# http://localhost:8000/docs
