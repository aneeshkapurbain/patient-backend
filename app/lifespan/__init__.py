from contextlib import asynccontextmanager
from fastapi import FastAPI
from ..logging import init as logging_init
from ..config import init as config_init


@asynccontextmanager
async def lifespan(app: FastAPI):
    await config_init()
    await logging_init()
    yield
