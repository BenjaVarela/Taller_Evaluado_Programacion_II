from sqlalchemy import select
from sqlalchemy.orm import Session
from conexion import engine
from modelos import Sala, Reserva

def consultar_salas():
    with Session(engine) as session:
        stmt = select(Sala)
        salas = session.scalars(stmt).all()
        if not salas:
            print("No hay salas registrada.")
        for s in salas:
            estado = "Disponible" if s.disponible else "Ocupada"
            print(f"ID: {s.id} | Nombre: {s.nombre} | Capacidad: {s.capacidad} | Estado: {estado}")

def consultar_reservas():
    with Session(engine) as session:
        stmt = select(Reserva)
        reservas = session.scalars(stmt).all()
        if not reservas:
            print("No hay reservas registradas.")
        for r in reservas:
            print(f"ID Reserva: {r.id}\nEstudiante: {r.estudiante}\nSala: {r.sala.nombre}\nFecha: {r.fecha}")