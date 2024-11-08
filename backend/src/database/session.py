from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .URI import DATABASE_URI

engine = create_engine(DATABASE_URI)

Session = sessionmaker(engine)