"""
main models
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
            CREATE TABLE City (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                latitude DECIMAL(9, 6) NOT NULL,
                longitude DECIMAL(9, 6) NOT NULL
            );
        """,
        """
            DROP TABLE City;
        """
    ),

]
