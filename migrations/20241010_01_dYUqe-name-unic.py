"""
name unique
"""

from yoyo import step

__depends__ = {'20241009_01_Uo319-main-models'}

steps = [
    step(
        """
        ALTER TABLE city
        ADD CONSTRAINT unique_name UNIQUE (name);
        """,
        """
        ALTER TABLE city
        DROP CONSTRAINT unique_name;
        """
    ),
    step(
        """
        ALTER TABLE city
        ALTER COLUMN name SET NOT NULL,
        ALTER COLUMN latitude SET NOT NULL,
        ALTER COLUMN longitude SET NOT NULL;
        """,
        """
        ALTER TABLE city
        ALTER COLUMN name DROP NOT NULL,
        ALTER COLUMN latitude DROP NOT NULL,
        ALTER COLUMN longitude DROP NOT NULL;
        """
    )
]
