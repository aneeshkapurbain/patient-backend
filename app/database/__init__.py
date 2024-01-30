from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from ..logging import get_logger
from ..config import get_config

_engine: AsyncEngine | None = None


async def init() -> None:
    global _engine
    logger = await get_logger()
    config = await get_config()

    try:
        logger.info("Creating connection pool")
        _engine = create_async_engine(config.postgres.dsn)
        logger.info("Connection pool created")
    except Exception as e:
        logger.exception(e)


async def get_engine() -> AsyncEngine:
    return _engine
