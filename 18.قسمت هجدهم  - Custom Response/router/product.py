from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse, PlainTextResponse


router = APIRouter(prefix='/product', tags=['product'])

products = ['watch', 'clock', 'microphone']


@router.get('/')
def get_all():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get("/{id}", responses={
    404:{"content":{"text/plain": {'example': "Product Not Found !"}},
         "description": "vaghti mahsol peyda nashode bashe"},
    200:{"content":{"text/html": {'example': "<div> data </div>"}},
         "description": "Html Code Data "}
})
def get_product(id: int):
    if id > len(products):
        text = "Product Not Found !"
        return PlainTextResponse(status_code=404, content=text, media_type="text/plain")

    data = products[id]
    return HTMLResponse(content=f"<div> {data} </div>", media_type="text/html")