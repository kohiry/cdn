from pydantic import BaseModel


class City(BaseModel):
    name: str


class CityResponse(City):
    id: int | None = None
    latitude: float
    longitude: float
