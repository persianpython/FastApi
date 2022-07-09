from fastapi import FastAPI
from db.models import Base
from db.database import engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return "First Page"
