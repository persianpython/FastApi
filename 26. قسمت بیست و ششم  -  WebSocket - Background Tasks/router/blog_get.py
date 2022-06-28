from fastapi import APIRouter, status, Response
from fastapi import BackgroundTasks
from enum import Enum
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])


class TypeBlogs(str, Enum):
    Mesal1 = 'mesal1'
    Mesal2 = 'mesal2'
    Mesal3 = 'mesal3'


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f"blog id {id} comment id {comment_id} {valid=} {username=}"}


def log_data(message):
    with open('log.txt', 'a') as file:
        file.write(message)


@router.get('/all')
def get_blogs(bt: BackgroundTasks, page: Optional[int] = None, page_size: str = None):
    bt.add_task(log_data, 'Get All Blogs')
    return {"message": f"{page=} -- {page_size=}"}


@router.get('/type/{type}')
def get_type_blog(type: TypeBlogs):
    return {'message': f'blog type is {type}'}


# @app.get('/blog/all')
# def get_blogs():
#     return {'message':f'all blogs'}

@router.get('/{id}', status_code=status.HTTP_200_OK, summary='daryaft blog !', response_description='id blog darkhasti !')
def get_blog(id: int, response:Response):

    """
    in api baraye daryaft blog hastesh !

    - **id** baraye daryaft id blog

    """

    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": f"Blog {id} Not Found !"}
    return {'message': f'blog {id}'}