from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.models import Base
from db.database import engine
from routers import user
from routers import post

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)


app.mount("/uploaded_files", StaticFiles(directory="uploaded_files"), name="uploaded_files")

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return "First Page"
