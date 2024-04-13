import platform
import sys
import subprocess

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sistema_operativo', methods=['GET'])
def obtener_datos_sistema():
    # Obtener datos del sistema operativo utilizando el módulo 'platform'
    sistema_operativo = platform.system()
    version = platform.version()
    arquitectura = platform.architecture()

    # Crear un diccionario con los datos del sistema operativo
    datos_sistema = {
        "sistema_operativo": sistema_operativo,
        "version": version,
        "arquitectura": arquitectura
    }

    # Devolver los datos del sistema operativo como JSON
    return jsonify(datos_sistema)

if __name__ == '__main__':
    app.run(debug=True)
