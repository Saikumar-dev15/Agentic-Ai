from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2 , time
from psycopg2.extras import RealDictCursor

DATABASE_URL = "postgresql://postgres:Anantha 123@localhost:5432/fastapi"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try :
        yield db

    finally :
        db.close()
        
        
# =========================================================
# DATABASE CONNECTION
# =========================================================

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="postgres123",
            cursor_factory=RealDictCursor
        )

        cursor = conn.cursor()

        print("Database connection was successful")
        break

    except Exception as e:
        print(f"Database connection error: {e}")
        time.sleep(2)