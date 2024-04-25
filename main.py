from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
 
app = FastAPI()
 
class Position(BaseModel):
    department_name: str
    position_name: str
    employee_count: int
 
positions = [
    {"department_name": "Sales", "position_name": "Accountant", "employee_count": 6},
    {"department_name": "Human Resources", "position_name": "Accountant", "employee_count": 4},
    {"department_name": "IT", "position_name": "Accountant", "employee_count": 1},
    {"department_name": "Finance", "position_name": "Accountant", "employee_count": 2},
    {"department_name": "Marketing", "position_name": "Accountant", "employee_count": 2},
    {"department_name": "Sales", "position_name": "Analyst", "employee_count": 4},
    {"department_name": "Human Resources", "position_name": "Analyst", "employee_count": 1},
    {"department_name": "IT", "position_name": "Analyst", "employee_count": 5},
    {"department_name": "Finance", "position_name": "Analyst", "employee_count": 6},
    {"department_name": "Marketing", "position_name": "Analyst", "employee_count": 4},
    {"department_name": "Sales", "position_name": "Developer", "employee_count": 3},
    {"department_name": "Human Resources", "position_name": "Developer", "employee_count": 2},
    {"department_name": "IT", "position_name": "Developer", "employee_count": 2},
    {"department_name": "Finance", "position_name": "Developer", "employee_count": 5},
    {"department_name": "Marketing", "position_name": "Developer", "employee_count": 4},
    {"department_name": "Sales", "position_name": "HR Specialist", "employee_count": 2},
    {"department_name": "Human Resources", "position_name": "HR Specialist", "employee_count": 4},
    {"department_name": "IT", "position_name": "HR Specialist", "employee_count": 7},
    {"department_name": "Finance", "position_name": "HR Specialist", "employee_count": 5},
    {"department_name": "Marketing", "position_name": "HR Specialist", "employee_count": 1},
    {"department_name": "Sales", "position_name": "Manager", "employee_count": 6},
    {"department_name": "Human Resources", "position_name": "Manager", "employee_count": 5},
    {"department_name": "IT", "position_name": "Manager", "employee_count": 4},
    {"department_name": "Finance", "position_name": "Manager", "employee_count": 7},
    {"department_name": "Marketing", "position_name": "Manager", "employee_count": 8}
]
 
@app.get("/")
def bienevenida():
    return "Bievenidos a la prueba de GLOBAL MVM, aqui podras consultar el resultado de la vista"

# API 1

@app.get("/API 1 Empleados-puesto/", description="Esta consulta devuelve la cantidad de empleados que tienen un puesto específico")
def empleados_puesto(puesto: Optional[str] = None):
    if puesto is None:
        return {"error": "Debes proporcionar un puesto"}

    count = 0
    for position in positions:
        if position["position_name"].lower() == puesto.lower():
            count += position["employee_count"]

    return {"puesto": puesto, "cantidad": count}

@app.get("/API 2 Empleados-departamento/", description="Esta consulta devuelve la cantidad de empleados en un departamento específico")
def empleados_departamento(departamento: Optional[str] = None):
    if departamento is None:
        return {"error": "Debes proporcionar un departamento"}

    count = 0
    for position in positions:
        if position["department_name"].lower() == departamento.lower():
            count += position["employee_count"]

    return {"departamento": departamento, "cantidad": count}

@app.get("/API 3 Puestos-departamento/", description="Esta consulta devuelve todos los puestos disponibles en un departamento específico")
def puestos_departamento(departamento: Optional[str] = None):
    if departamento is None:
        return {"error": "Debes proporcionar un departamento"}

    puestos = set()
    for position in positions:
        if position["department_name"].lower() == departamento.lower():
            puestos.add(position["position_name"])

    return {"departamento": departamento, "puestos": list(puestos)}

@app.get("/API 4 Departamentos-puesto/", description="Esta consulta devuelve todos los departamentos que tienen al menos un empleado en un puesto específico")
def departamentos_puesto(puesto: Optional[str] = None):
    if puesto is None:
        return {"error": "Debes proporcionar un puesto"}

    departamentos = set()
    for position in positions:
        if position["position_name"].lower() == puesto.lower():
            departamentos.add(position["department_name"])

    return {"puesto": puesto, "departamentos": list(departamentos)}

@app.get("/API 5 Total-empleados/", description="Esta consulta devuelve la cantidad total de empleados")
def total_empleados():
    count = sum(position["employee_count"] for position in positions)
    return {"total_empleados": count}