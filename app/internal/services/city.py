from fastapi import HTTPException
import httpx

from app.config import settings
from app.pkg.models import City


async def get_city_coordinates(query: City):
    async with httpx.AsyncClient() as client:
        url = ("http://api.openweathermap.org/data/2.5/"
               f"weather?q={query.name}&appid={settings.TOKEN}")
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="City not found")
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        return lat, lon
