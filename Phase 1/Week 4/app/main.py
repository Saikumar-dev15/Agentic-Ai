from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.params import Body
from typing import Optional , List
import psycopg2
from random import randrange
from psycopg2.extras import RealDictCursor
import time
try:
    from . import models , schemas
    from .database import engine, SessionLocal, get_db
except ImportError:
    import models, schemas
    from database import engine, SessionLocal, get_db

from sqlalchemy.orm import Session 

pwd_context = CryptContext(schemes= ["bcrypt"], deprecated="auto")
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


@app.get("/posts" , response_model=List[schemas.Post])                                 #second method to run in postman to get information from pgadmin
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts")                #this is regular sql method
    # posts = cursor.fetchall()
     
    posts = db.query(models.post).all()
    return {"data": posts}


# =========================================================
# CREATE POST
# =========================================================

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):

    # cursor.execute(                                                           #this is Sqlalchemy
    #     """
    #     INSERT INTO posts (title, content, published, rating)
    #     VALUES (%s, %s, %s, %s)
    #     RETURNING *
    #     """,
    #     (
    #         post.title,
    #         post.content,
    #         post.published,
    #         post.rating
    #     )
    # )
    # new_post = cursor.fetchone()
    # conn.commit()
    
    print(post.dict())
    new_post = models.post(                                                                               #this code is based on python that create posts
        #title= post.title , content=post.content , published=post.published
        **post.dict()                                              #we can see output in terminal
    ) 
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post



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




@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email is already registered
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with email '{user.email}' already exists"
        )

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@app.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist"
        )
    return user