from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import config

# engine = create_engine(
#     url=config.DATABASE_URL,
#     echo=True
# )

# engine = AsyncEngine(
#     create_engine(
#         url=config.DATABASE_URL,
#         echo=True
#     )
# )

engine = create_async_engine(
        url=config.DATABASE_URL,
        echo=True
    )



async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")
        result = await conn.execute(statement)
        print(result.all())

