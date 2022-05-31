from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def hello():
    return 'hello world'


class TypeBlogs(str, Enum):
    Mesal1 = 'mesal1'
    Mesal2 = 'mesal2'
    Mesal3 = 'mesal3'


@app.get('/blog/type/{type}')
def get_type_blog(type:TypeBlogs):
    return {'message': f'blog type is {type}'}

@app.get('/blog/all')
def get_blogs():
    return {'message':f'all blogs'}

@app.get('/blog/{id}')
def get_blog(id:int):
    return {'message':f'blog {id}'}

# pydantic