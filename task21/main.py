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


# Пример запроса:
# curl -X POST http://localhost:8000/feedback \
#      -H "Content-Type: application/json" \
#      -d '{"name": "Rustam", "message": "Отличный день! Мне нравится ходить в школу!"}'
#
# Ответ: {"message": "Feedback received. Thank you, Rustam."}
