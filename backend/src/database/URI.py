import os

user: str = os.getenv("B4B_DB_USER", "postgres")
password: str = os.getenv("B4B_DB_PASSWORD", "postgres")
host: str = os.getenv("B4B_DB_HOST", "db:5432")
schema: str = os.getenv("B4B_DB_SCHEMA", "db")

DATABASE_URI: str = f"postgresql+psycopg2://{user}:{password}@{host}/{schema}"
