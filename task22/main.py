from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from typing import List

app = FastAPI()

# Недопустимые слова (ищем вхождение, чтобы поймать любой падеж)
BANNED_WORDS = ["кринж", "криндж", "рофл", "вайб"]


class Feedback(BaseModel):
    name: str
    message: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("String should have at least 2 characters")
        if len(v) > 50:
            raise ValueError("String should have at most 50 characters")
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        if len(v) < 10:
            raise ValueError("String should have at least 10 characters")
        if len(v) > 500:
            raise ValueError("String should have at most 500 characters")
        # Проверяем наличие запрещённых слов (без учёта регистра)
        lower = v.lower()
        for word in BANNED_WORDS:
            if word in lower:
                raise ValueError("ТЫ ЗАБАНЕН И Я НЕ БУДУ  ТЕБЯ РАЗБАНИВАТЬ")
        return v


# Хранилище отзывов (в памяти)
feedbacks: List[Feedback] = []


@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}


# Дополнительный маршрут — посмотреть все сохранённые отзывы
@app.get("/feedback")
def get_feedbacks():
    return feedbacks


