from flask import Flask

app = Flask(__name__)

# Asegúrate de importar las rutas aquí, después de crear la instancia de la aplicación
from app import routes
