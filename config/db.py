from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

#engine = create_engine("postgresql://postgres+asyncpg:FkHecP0E7TzPllCb@db.yyuqbvoevfpbswnyxpoo.supabase.co:5432/postgres")

engine = create_async_engine("postgresql+asyncpg://postgres:2yBXiAom7L4wfbxE@db.yyuqbvoevfpbswnyxpoo.supabase.co:5432/postgres")

Base = declarative_base()
metadata = Base.metadata

conn = engine.connect()
