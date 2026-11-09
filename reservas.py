from sqlalchemy.orm import Session
from conexion import engine
from modelos import Sala, Reserva

def registrar_reserva(estudiante: str, sala_id: int, fecha: str):
    if not estudiante or not fecha:
        print("Error: Datos del estudiante o fecha inválidos, revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            sala = session.get(Sala, sala_id)
            if not sala:
                print("Error: La sala seleccionada no existe.")
                return
            if not sala.disponible:
                print("Error: La sala seleccionada no está disponible.")
                return
            
            nueva_reserva = Reserva(estudiante=estudiante, sala_id=sala.id, fecha=fecha)
            sala.disponible = False
            session.add(nueva_reserva)
        print("La reserva se guardó exitosamente.")