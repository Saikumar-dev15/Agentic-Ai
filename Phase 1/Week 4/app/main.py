from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional, List
import psycopg2
from random import randrange
from psycopg2.extras import RealDictCursor
import time
try:
    from . import models, schemas, utils
    from .database import engine, SessionLocal, get_db
    from .router import post, user 
except ImportError:
    import models, schemas, utils
    from database import engine, SessionLocal, get_db
    from router import post, user


from sqlalchemy.orm import Session 

models.Base.metadata.create_all(bind=engine)



app = FastAPI()




class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



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


my_posts = [{"title": "title of post 1", "content":"content of post 1", "id":1},
            {"title": "favorite foods", "content": "I like pizza", "id":2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
app.include_router(post.router)
app.include_router(user.router)



@app.get("/")
def root():
    return {"message": "Welcome to My API"}