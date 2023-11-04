from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from core.config import Config


engine = create_async_engine(Config.DB_URL, echo=True)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


async def init_models() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
