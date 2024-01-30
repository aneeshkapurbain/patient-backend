from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from .lifespan import lifespan
from .routers import patients
from .middlewares import request
from .responses.default_class import CustomJSONResponse

app = FastAPI(lifespan=lifespan, default_response_class=CustomJSONResponse)
app.add_middleware(BaseHTTPMiddleware, dispatch=request.request_middleware)
app.include_router(patients.router)
