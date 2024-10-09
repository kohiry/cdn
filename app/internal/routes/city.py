from typing import Annotated
from geopy.distance import geodesic
from fastapi import APIRouter, HTTPException, Depends, Query

from app.config import get_logger
from app.internal.services import get_city_coordinates
from app.pkg.models import CityResponse, City
from app.pkg.repository import get_city_repository, CityRepository

city_router = APIRouter(prefix='/city')
logger = get_logger(__name__)


@city_router.post("/")
async def add_city(city: City,
                   repo: CityRepository = Depends(get_city_repository)) -> int:
    logger.info("Добавление города: %s" % city.name)
    try:
        lat, lon = await get_city_coordinates(city)
        c = CityResponse(name=city.name, latitude=lat, longitude=lon)
        id_city = repo.add(c)
        logger.info("Успешно добавили город: %s" % city.name)
        return id_city
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@city_router.get("/")
def get_city(
        city: Annotated[City, Query()],
        repo: CityRepository = Depends(get_city_repository),
):
    res = repo.get(city)
    if res is None:
        raise HTTPException(status_code=404, detail="City not found")
    return res


@city_router.delete("/")
async def delete_city(
        city: Annotated[City, Query()],
        repo: CityRepository = Depends(get_city_repository),
):
    try:
        logger.info("Удаление города: %s" % city.name)
        repo.delete(city)
        return {"message": f"City {city.name} deleted successfully!"}
    except Exception as e:
        logger.error("City not found: %s" % city.name)
        raise HTTPException(status_code=404, detail=str(e))


@city_router.get("/all")
async def get_cities(repo: CityRepository
                     = Depends(get_city_repository)) -> list[CityResponse]:
    cities = repo.list()
    return cities


@city_router.get("/nearest-cities/")
async def get_nearest_cities(
        latitude: float,
        longitude: float,
        repo: CityRepository = Depends(get_city_repository),
):
    logger.info("Получение ближайших городов по координатам: "
                "latitude %s | longitude %s" % (latitude, longitude))

    distances = []
    # Делать оптимизированное решение будет излишним,
    # поэтому просто по листу иду.
    for city in repo.list():
        distance = geodesic((latitude, longitude),
                            (city.latitude, city.longitude)).kilometers
        distances.append((city.name, distance))

    print(distances)
    distances.sort(key=lambda x: x[1])
    nearest_cities = distances[:2]

    return [{"name": city, "distance_km": dist}
            for city, dist in nearest_cities]
