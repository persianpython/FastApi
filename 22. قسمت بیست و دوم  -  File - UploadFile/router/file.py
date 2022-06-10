from fastapi import APIRouter, File, UploadFile
import shutil


router = APIRouter(prefix='/file', tags=['file'])


@router.post('/file')
def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    content.split('\n')
    return {
        'data': content
    }


@router.post('/uploadfile')
def upload_file(file: UploadFile= File(...)):
    name = file.filename
    type = file.content_type

    path = f'files/{name}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        'path': path,
        'type': type
    }




