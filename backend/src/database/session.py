from sqlalchemy import create_engine
from URI import DATABASE_URI

engine = create_engine(DATABASE_URI)