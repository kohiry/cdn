import psycopg2
from typing import List, Optional

from app.pkg.models import City, CityResponse
from app.pkg.repository.repository import get_connection


class CityRepository:
    @staticmethod
    def add(query: CityResponse) -> int:
        with get_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        """
                        INSERT INTO city (name, latitude, longitude)
                        VALUES (%s, %s, %s)
                        RETURNING id;
                        """,
                        (query.name, query.latitude, query.longitude)
                    )
                    conn.commit()
                    res = cur.fetchone()[0]
                    return res
                except psycopg2.IntegrityError:
                    conn.rollback()
                    raise Exception(f"City {query.name} already exists")

    @staticmethod
    def get(query: City) -> Optional[CityResponse]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, name, latitude, longitude FROM city
                    WHERE name = %s;
                    """,
                    (query.name,)
                )
                result = cur.fetchone()
                if result:
                    return CityResponse(
                        id=result[0],
                        name=result[1],
                        latitude=result[2],
                        longitude=result[3],
                    )
                return None

    # @lru_cache(maxsize=128)  в идеале конечно кешировать хотяб,
    # но вам будет геморно тестить
    @staticmethod
    def list() -> List[CityResponse]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, latitude, longitude FROM city;")
                result = cur.fetchall()
                return [CityResponse(
                            id=row[0],
                            name=row[1],
                            latitude=row[2],
                            longitude=row[3],
                        ) for row in result]

    @staticmethod
    def delete(query: City) -> None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM city WHERE name = %s;", (query.name,))
                conn.commit()
