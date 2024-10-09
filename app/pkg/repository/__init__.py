from app.pkg.repository.city import CityRepository

__all__ = [
    "get_city_repository",
    'CityRepository'
]


def get_city_repository() -> CityRepository:
    return CityRepository()
