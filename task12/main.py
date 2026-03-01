from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def get_index():
    return FileResponse("index.html")


# Запуск:
# uvicorn main:app --reload
# Открыть: http://localhost:8000
