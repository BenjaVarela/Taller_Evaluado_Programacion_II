from modelos import Base
from conexion import engine

def crear_tablas():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    crear_tablas()