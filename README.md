# Taller Evaluado Programación 2

Sistema de reservas de salas de estudio

## Guía para la instalación y Ejecución Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/BenjaVarela/Taller_Evaluado_Programacion_2.git
cd Taller_Evaluado_Programación_2
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
# Luego el siguiente comando, que en Windows es:
source venv/Scripts/activate
```

### 3. Instalar el ORM
```bash
python -m pip install sqlalchemy
```

### 4. Ejecutar el sistema de reservas
```bash
python main.py
```

El sistema cuenta con cinco funcionalidades enumeradas del 1-5. Cada una de ellas con una función única, en las cuales se encuentran:
* `1. Registrar sala`
* `2. Consultar salas`
* `3. Registrar reserva`
* `4. Consultar reservas`
* `5. Cancelar reserva`
* `0. Salir`

## Pruebas

Para realizar las pruebas, se debe elegir una opción de las disponibles.