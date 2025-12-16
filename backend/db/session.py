import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# Build the database URL
DB_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('PG_USER')}:"
    f"{os.getenv('PG_PASSWORD')}@"
    f"{os.getenv('PG_HOST')}:"
    f"{os.getenv('PG_PORT')}/"
    f"{os.getenv('PG_DATABASE')}"
)

engine = create_engine(DB_URL, connect_args={"sslmode": "disable"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()