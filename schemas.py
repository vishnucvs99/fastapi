from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    age: int
    address: str
    position: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
