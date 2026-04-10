from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:2yBXiAom7L4wfbxE@db.yyuqbvoevfpbswnyxpoo.supabase.co:5432/postgres")
#engine = create_engine("postgresql://postgres+asyncpg:FkHecP0E7TzPllCb@db.yyuqbvoevfpbswnyxpoo.supabase.co:5432/postgres")

meta = MetaData()

conn = engine.connect()
