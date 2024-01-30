from __future__ import annotations
import loguru
import sys
from ..config import get_config

_logger: loguru.Logger | None = None


async def init() -> None:
    config = await get_config()
    global _logger

    _logger = loguru.logger
    _logger.remove()
    _logger.add(sys.stderr, format=config.logging.format)


async def get_logger() -> loguru.Logger:
    global _logger
    return _logger
