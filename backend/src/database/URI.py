import os

user = os.getenv("B4B_DB_USER", "postgres")
password = os.getenv("B4B_DB_PASSWORD", "postgres")
host = os.getenv("B4B_DB_HOST", "db:5432")
schema = os.getenv("B4B_DB_SCHEMA", "db")

DATABASE_URI = f"postgresql+psycopg2://{user}:{password}@{host}/{schema}"
print(DATABASE_URI)
