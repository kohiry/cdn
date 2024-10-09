from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any, Generic, TypeVar, List, Optional

import psycopg2

from app.config import settings

T = TypeVar('T')


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    async def add(self, entity: T) -> None:
        """Добавить сущность в хранилище"""
        pass

    @abstractmethod
    async def get(self, name: str) -> Optional[T]:
        """Получить сущность по ID"""
        pass

    @abstractmethod
    async def list(self) -> List[T]:
        """Получить список всех сущностей"""
        pass

    @abstractmethod
    async def delete(self, name: Any) -> None:
        """Удалить сущность по ID"""
        pass


@contextmanager
def get_connection():
    conn = psycopg2.connect(settings.DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()
