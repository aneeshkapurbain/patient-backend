from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter()


@router.get("/patients/", status_code=HTTPStatus.OK)
async def get_all():
    a=2/0
    return [{"username": "Rick"}, {"username": "Morty"}]