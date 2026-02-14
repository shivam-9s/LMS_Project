from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import StudentCreate
from app.models import Student
from app import crud

# Router must be defined first
router = APIRouter()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Add Student (CREATE)
@router.post("/students")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


#2. Get All Students (READ ALL)
@router.get("/students")
def list_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# 3. Get Single Student By ID (READ ONE) Needed for Edit Feature
@router.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# 4. Update Student (UPDATE)
@router.put("/students/{id}")
def update_student(id: int, student: StudentCreate, db: Session = Depends(get_db)):

    db_student = db.query(Student).filter(Student.id == id).first()

    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update fields
    db_student.name = student.name
    db_student.email = student.email
    db_student.course = student.course

    db.commit()
    db.refresh(db_student)

    return db_student


# 5. Delete Student (DELETE)
@router.delete("/students/{id}")
def remove_student(id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}
