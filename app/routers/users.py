# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.deps.db import get_db
import app.models as models
import app.schemas as schemas
from app.schemas import Gender
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = models.User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    

@router.get("/users", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        users = db.query(models.User).offset(skip).limit(limit).all()
        return users
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")

@router.patch("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        for var, value in vars(user_update).items():
            setattr(user, var, value) if value is not None else None

        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")

@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(user)
        db.commit()
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/users/{user_id}/matches", response_model=List[schemas.User])
def find_matches(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        # Determine opposite gender
        opposite_gender = Gender.female if user.gender == Gender.male else Gender.male

        # Calculate age range
        min_age = user.age - 5
        max_age = user.age + 5

        # Find matches
        matches = (
            db.query(models.User)
            .filter(models.User.gender == opposite_gender)
            .filter(models.User.age.between(min_age, max_age))
            .filter(models.User.id != user_id)
            .all()
        )

        def calculate_matching_interests(user1, user2):
            return len(set(user1.interests).intersection(set(user2.interests)))

        matches.sort(key=lambda x: calculate_matching_interests(user, x), reverse=True)

        return matches

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")
