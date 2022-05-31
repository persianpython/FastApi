from fastapi import FastAPI
from router import blog_get
from router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def hello():
    return 'hello world'
