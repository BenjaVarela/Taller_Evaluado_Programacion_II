from sqlalchemy.orm import Session
from conexion import engine
from modelos import Reserva, Sala

def cancelar_reserva(id_reserva: int):
    with Session(engine) as session:
        with session.begin():
            reserva = session.get(Reserva, id_reserva)
            if not reserva:
                print("Error: La reserva no existe, revise que haya elegido bien el ID.")
                return
            
            sala = reserva.sala
            sala.disponible = True
            session.delete(reserva)
        print("Reserva cancelada y sala liberada exitosamente.")