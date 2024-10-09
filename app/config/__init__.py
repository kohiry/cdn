from app.config.logger import get_logger
from app.config.settings import get_settings

__all__ = [
    "settings",
    "get_logger"
]
settings = get_settings()
