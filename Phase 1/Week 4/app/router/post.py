from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from typing import Optional, List
try:
    from .. import models, schemas, utils, oauth2
    from ..database import  get_db
except ImportError:
    import models, schemas, utils, oauth2
    from database import  get_db


router = APIRouter(
    prefix="/posts" ,
    tags = ['Posts']
)



# =========================================================
# GET ALL POSTS
# =========================================================

@router.get("/sqlalchemy")                            #dependent method to get information from pgadmin
def test_posts(db: Session =Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    posts = db.query(models.post).all()
    #return {"status": "success"}             #this is for sql db 
    return {"data": posts}                    #this is for postman 


@router.get("", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.post).all()
    return posts



# =========================================================
# CREATE POST
# =========================================================

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):



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
    
    print(current_user.email)
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

@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # cursor.execute(
    #     "SELECT * FROM posts WHERE id = %s",
    #     (id,)
    # )
    # post = cursor.fetchone()
    post = db.query(models.post).filter(models.post.id == id).first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # cursor.execute(
    #     """
    #     DELETE FROM posts
    #     WHERE id = %s
    #     RETURNING *
    #     """,
    #     (str(id),)
    # )
    # deleted_post = cursor.fetchone()
    # conn.commit()

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

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
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
    
    return post
