from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"message": 'OK', "data": blog, "id": id, 'version': version}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(id: int, blog: BlogModel,
                   comment_title: int = Query(None,
                                           title='Title Text !',
                                           description='Description Text !',
                                           alias='CommentTitle',
                                           deprecated=True
                                           ),
                   content: str = Body(...,
                                       min_length=10,
                                       max_length=20,
                                       regex='^[A-Z].*'
                                       ),
                   v: Optional[List[str]]= Query(['1.2', '1.5']),
                   comment_id: int = Path(None, gt=5)
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id

    }

# Greate Than -- GT -- >
# Greate Or Equal -- GE -- >=
# Less than -- LT -- <
# Less or Equal -- LE -- <=
