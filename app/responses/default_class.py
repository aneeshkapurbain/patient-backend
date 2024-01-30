from fastapi import Response
from typing import Any
from ..responses.generic import Generic
from http import HTTPStatus


class CustomJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return (
            Generic(
                status_code=self.status_code,
                message=HTTPStatus(self.status_code).phrase,
                data=content,
            )
            .model_dump_json()
            .encode("utf-8")
        )
