from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional
import psycopg2
from random import randrange
from psycopg2.extras import RealDictCursor
import time
try:
    from . import models
    from .database import engine, SessionLocal, get_db
except ImportError:
    import models
    from database import engine, SessionLocal, get_db

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


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():
    return {"message": "Welcome to My API"}


# =========================================================
# GET ALL POSTS
# =========================================================

@app.get("/sqlalchemy")                            #dependent method to get information from pgadmin
def test_posts(db: Session =Depends(get_db)):
    
    posts = db.query(models.post).all()
    #return {"status": "success"}             #this is for sql db 
    return {"data": posts}                    #this is for postman 


@app.get("/posts")                                 #second method to run in postman to get information from pgadmin
def get_posts():

    cursor.execute("SELECT * FROM posts")                #this is regular sql method

    posts = cursor.fetchall()

    return {"data": posts}


# =========================================================
# CREATE POST
# =========================================================

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session =Depends(get_db)):

    #cursor.execute(                                                           #this is Sqlalchemy
    #    """
    #    INSERT INTO posts (title, content, published, rating)
    #    VALUES (%s, %s, %s, %s)
    #    RETURNING *
    #    """,
    #    (
    #        post.title,
    #        post.content,
    #        post.published,
    #        post.rating
    #    )
    #)
    #new_post = cursor.fetchone()
    #conn.commit()
    
    print(post.dict())
    new_post = models.post(                                                                               #this code is based on python that create posts
        #title= post.title , content=post.content , published=post.published
        **post.dict()                                              #we can see output in terminal
    ) 
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return {"data": new_post}


# =========================================================
# GET SINGLE POST
# =========================================================

@app.get("/posts/{id}")
def get_post(id: int, db: Session =Depends(get_db)):

    #cursor.execute(
    #    "SELECT * FROM posts WHERE id = %s",
    #    (id,)
    #)
    #post = cursor.fetchone()
    post = db.query(models.post).filter(models.post.id == id).first()
    #print(post)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session =Depends(get_db)):

    #cursor.execute(
    #    """
    #    DELETE FROM posts
    #    WHERE id = %s
    #    RETURNING *
    #    """,
    #    (str(id),)
    #)
    #deleted_post = cursor.fetchone()

    #conn.commit()

    post = db.query(models.post).filter(models.post.id == id)
    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# =========================================================
# UPDATE POST
# =========================================================

@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
    
    post = db.query(models.post).filter(models.post.id == id).first()
    
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )
    
    post.title = updated_post.title
    post.content = updated_post.content
    post.published = updated_post.published
    
    db.commit()
    db.refresh(post)
    
    return {"data": post}






# =========================================================
# EXAMPLE REQUEST BODIES (for reference / Postman)
# =========================================================

# Create Post:
# {
#     "title": "My First Post",
#     "content": "Learning FastAPI with PostgreSQL",
#     "published": True,
#     "rating": 5
# }

# Update Post:
# {
#     "title": "Updated Post",
#     "content": "I am learning FastAPI",
#     "published": True,
#     "rating": 4
# }
