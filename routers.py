from fastapi import APIRouter, HTTPException,status, Depends
from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeCreate, Employee as EmployeeSchema
from db import get_db
from auth import get_current_user

router = APIRouter()    

@router.post("/employees/")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db),user: str = Depends(get_current_user)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/employees/{employee_id}")
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
