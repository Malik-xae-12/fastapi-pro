from sqlmodel import SQLModel,create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

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
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print(result.all())
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session()-> AsyncSession:
    Session= sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session