import models
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config.base import Base


#engine = create_engine("postgresql://postgres+asyncpg:FkHecP0E7TzPllCb@db.yyuqbvoevfpbswnyxpoo.supabase.co:5432/postgres")

engine = create_async_engine("postgresql+asyncpg://postgress:pOakUYRGQYlMWx1H5JTXrambfB22sCsT@dpg-d6tiousr85hc73f9vdjg-a.oregon-postgres.render.com/social_db_bc6g")

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
