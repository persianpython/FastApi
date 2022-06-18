import time

from fastapi import APIRouter, Response, Header, Cookie, Form
from typing import Optional, List
from fastapi.responses import HTMLResponse, PlainTextResponse

router = APIRouter(prefix='/product', tags=['product'])

products = ['watch', 'clock', 'microphone']


async def test_async():
    time.sleep(10)
    return '1'


@router.get('/')
async def get_all():
    await test_async()
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key='cookie', value='tEst')
    return response

@router.post('/create')
def create_product(data:str=Form(...)):
    products.append(data)
    return products

@router.get('/withheader')
def get_products(custom_header:Optional[List[str]] = Header(None),
                 cookie:str = Cookie(None)):
    print(custom_header)
    print(cookie)
    return {'data': products, 'header': custom_header, 'cookie': cookie}


@router.get("/{id}", responses={
    404: {"content": {"text/plain": {'example': "Product Not Found !"}},
          "description": "vaghti mahsol peyda nashode bashe"},
    200: {"content": {"text/html": {'example': "<div> data </div>"}},
          "description": "Html Code Data "}
})
def get_product(id: int):
    if id > len(products):
        text = "Product Not Found !"
        return PlainTextResponse(status_code=404, content=text, media_type="text/plain")

    data = products[id]
    return HTMLResponse(content=f"<div> {data} </div>", media_type="text/html")
