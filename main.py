from datetime import datetime, date
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    currentTime = datetime.now()
    h = currentTime.hour
    greeting = "Night"
    if 12 <= h < 18:
        greeting = "Afternoon"
    if h < 12:
        greeting = "Morning"
    return {
        "today": f"{date.today()}, {currentTime.hour}:{currentTime.minute}",
        "greeting": f"Good {greeting}!",
    }
