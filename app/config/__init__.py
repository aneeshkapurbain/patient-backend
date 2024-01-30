from omegaconf import OmegaConf
from dotenv import load_dotenv
from omegaconf import DictConfig, ListConfig
from typing import Union
import os

load_dotenv()

_config: Union[DictConfig, ListConfig] | None = None


async def init() -> None:
    global _config
    _config = OmegaConf.load(
        f"{os.path.join(os.path.dirname(os.path.abspath(__file__)), './config.yaml')}"
    )


async def get_config() -> Union[DictConfig, ListConfig]:
    return _config
