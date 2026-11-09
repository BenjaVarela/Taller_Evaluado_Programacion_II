from sqlalchemy.orm import Session
from conexion import engine
from modelos import Sala

def insertar_sala(nombre: str, capacidad: int):
    if not nombre or capacidad <= 0:
        print("Error: Nombre vacío o capacidad inválida, revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            nueva_sala = Sala(nombre=nombre, capacidad=capacidad)
            session.add(nueva_sala)
        print("La sala se guardó exitosamente.")