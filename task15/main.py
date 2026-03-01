from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
def check_adult(name: str, age: int):
    return {
        "name": name,
        "age": age,
        "is_adult": age >= 18,
    }


# http://localhost:8000/docs
