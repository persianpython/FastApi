from fastapi import APIRouter

router = APIRouter(prefix='/blog', tags=['blog'])


@router.post('/new')
def create_blog():
    return {"message": 'OK'}

