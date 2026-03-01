from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Feedback(BaseModel):
    name: str
    message: str


# Хранилище отзывов (в памяти)
feedbacks: List[Feedback] = []


@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}


# Дополнительный маршрут — посмотреть все сохранённые отзывы
@app.get("/feedback")
def get_feedbacks():
    return feedbacks


