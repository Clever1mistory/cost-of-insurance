import asyncpg
from fastapi import FastAPI
from tortoise import Tortoise

from src.config import DB_USER, DB_HOST, DB_NAME, DB_PORT, DB_PASS


DATABASE_URL = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["src.ops.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={'models': ['src.ops.models']},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
    await Tortoise.close_connections_asyncio()
