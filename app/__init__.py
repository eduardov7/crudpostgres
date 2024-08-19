from flask import Flask
from app.db import create_table  # Importa la función para crear la tabla

app = Flask(__name__)

# Crear la tabla cuando se inicializa la aplicación
create_table()

# Asegúrate de importar las rutas aquí, después de crear la instancia de la aplicación
from app import routes
