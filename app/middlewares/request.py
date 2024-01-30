from uuid import uuid4
from http import HTTPStatus
from fastapi.responses import JSONResponse
from ..logging import get_logger
from ..responses.generic import Generic
from starlette.middleware.base import Response, Request


async def request_middleware(request: Request, call_next) -> Response:
    request_id = str(uuid4())
    logger = await get_logger()

    with logger.contextualize(request_id=request_id):
        logger.info("Request start")

        try:
            response: Response = await call_next(request)
        except Exception as e:
            logger.exception(e)
            response = JSONResponse(
                content=Generic(
                    status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                    message=HTTPStatus(HTTPStatus.INTERNAL_SERVER_ERROR).phrase,
                    data=None,
                ).model_dump(),
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        finally:
            response.headers["X-Request-ID"] = request_id
            logger.info("Request end")
            return response
