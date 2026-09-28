from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()


# =========================================================
# PYDANTIC MODEL
# =========================================================

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

@app.get("/posts")
def get_posts():

    cursor.execute("SELECT * FROM posts")

    posts = cursor.fetchall()

    return {"data": posts}


# =========================================================
# CREATE POST
# =========================================================

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):

    cursor.execute(
        """
        INSERT INTO posts (title, content, published, rating)
        VALUES (%s, %s, %s, %s)
        RETURNING *
        """,
        (
            post.title,
            post.content,
            post.published,
            post.rating
        )
    )

    new_post = cursor.fetchone()

    conn.commit()

    return {"data": new_post}


# =========================================================
# GET SINGLE POST
# =========================================================

@app.get("/posts/{id}")
def get_post(id: int):

    cursor.execute(
        "SELECT * FROM posts WHERE id = %s",
        (id,)
    )

    post = cursor.fetchone()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute(
        """
        DELETE FROM posts
        WHERE id = %s
        RETURNING *
        """,
        (str(id),)
    )
    deleted_post = cursor.fetchone()

    conn.commit()

    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# =========================================================
# UPDATE POST
# =========================================================

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute(
        """
        UPDATE posts
        SET title = %s,
            content = %s,
            published = %s,
            rating = %s
        WHERE id = %s
        RETURNING *
        """,
        (
            post.title,
            post.content,
            post.published,
            post.rating,
            id
        )
    )

    updated_post = cursor.fetchone()

    conn.commit()

    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )

    return {"data": updated_post}

{
    "title": "My First Post",
    "content": "Learning FastAPI with PostgreSQL",
    "published": True,
    "rating": 5
}

{
    "title": "Updated Post",
    "content": "I am learning FastAPI",
    "published": True,
    "rating": 4
}