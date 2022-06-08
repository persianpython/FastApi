from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from router import blog_get, blog_post, user,article,product
from auth import authentication
from db import models
from db.database import engine
from exceptions import EmailNotValid


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)


models.Base.metadata.create_all(engine)

@app.get('/')
def hello():
    return 'hello world'


@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)