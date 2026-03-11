from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    db_task.title = task.title
    db_task.completed = task.completed

    db.commit()
    db.refresh(db_task)

    return db_task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    db.delete(db_task)
    db.commit()

    return {"message": "Task deleted"}