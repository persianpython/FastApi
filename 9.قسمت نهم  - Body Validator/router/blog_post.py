from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"message": 'OK', "data": blog, "id": id, 'version': version}


@router.post('/new/{id}/comment')
def create_comment(id: int, blog: BlogModel,
                   comment_id: int = Query(None,
                                           title='Title Text !',
                                           description='Description Text !',
                                           alias='CommentID',
                                           deprecated=True
                                           ),
                   content: str = Body(...,
                                       min_length=10,
                                       max_length=20,
                                       regex='^[A-Z].*',
                                       )
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content
    }
