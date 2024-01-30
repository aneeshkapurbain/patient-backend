from fastapi import APIRouter
from ..models import patient
from http import HTTPStatus

router = APIRouter()


@router.get("/patients/", status_code=HTTPStatus.OK)
async def get_all():
    try:
        return [{"username": "Rick"}, {"username": "Morty"}]
    except Exception as e:
        raise e