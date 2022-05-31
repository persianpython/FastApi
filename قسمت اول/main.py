from fastapi import FastAPI

app = FastAPI()

@app.get('/index')
def hello():
    return 'hello world'
