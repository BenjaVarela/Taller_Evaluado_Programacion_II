from crear_tablas import crear_tablas
from insertar import insertar_sala
from consultar import consultar_salas, consultar_reservas
from reservas import registrar_reserva
from eliminar import cancelar_reserva

def main():
    crear_tablas()
    while True:
        print("\n_______Reservas de Salas_______")
        print("\n1. Registrar sala")
        print("\n2. Consultar salas")
        print("\n3. Registrar reserva")
        print("\n4. Consultar reservas")
        print("\n5. Cancelar reserva")
        print("\n0. Salir")
        print("\n_______________________________")
        
        try:
            opcion = int(input("\n\nIngrese la opción que desee: "))
        except ValueError:
            print("Error: Debe ingresar solamente un número para la elección.")
            continue

        if opcion == 1:
            nombre = input("Nombre de la sala: ").strip()
            try:
                capacidad = int(input("Capacidad: "))
                insertar_sala(nombre, capacidad)
            except ValueError:
                print("Error: La capacidad debe ser un número entero.")

        elif opcion == 2:
            consultar_salas()

        elif opcion == 3:
            estudiante = input("Nombre del estudiante: ").strip()
            try:
                sala_id = int(input("ID de la sala: "))
                fecha = input("Fecha (DD-MM-AAAA): ").strip()
                registrar_reserva(estudiante, sala_id, fecha)
            except ValueError:
                print("Error: El ID de la sala debe ser un número entero.")
        
        elif opcion == 4:
            consultar_reservas()
        
        elif opcion == 5:
            try:
                id_reserva = int(input("ID de la reserva que desee cancelar: "))
                cancelar_reserva(id_reserva)
            except ValueError:
                print("Error: El ID de la reserva debe ser un número entero.")
        
        elif opcion == 0:
            print("\n\n___Cerrando el sistema de reservas____")
            break
        else:
            print("Error: Opción no válida.")

if __name__ == "__main__":
    main()