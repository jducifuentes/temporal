#!/usr/bin/python
import time
import board
import adafruit_ahtx0
from datetime import datetime
import os

# Configuración del archivo
CSV_FILE = "/root/repos/temporal/data.csv"

try:
    # Crear objeto sensor
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)

    # Obtener fecha y lecturas
    now = datetime.now()
    temp = sensor.temperature
    hum = sensor.relative_humidity

    # Formatear la línea exactamente como la pediste
    # Formato: FECHA ; TEMP ; HUM
    linea = f"{now} ; {temp} ; {hum}\n"

    # Escribir en el archivo (modo 'a' para append/añadir)
    with open(CSV_FILE, "a") as f:
        f.write(linea)

except Exception as e:
    # Opcional: registrar errores en un log aparte si el sensor falla
    with open("/root/sensor_error.log", "a") as f:
        f.write(f"{datetime.now()} - Error: {e}\n")

