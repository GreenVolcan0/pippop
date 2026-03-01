from fastapi import FastAPI
import models

app = FastAPI()

user = models.User(name="Анна Беляева", id=1)


@app.get("/users")
def get_user():
    return user



