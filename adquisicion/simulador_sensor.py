"""
Módulo de adquisición de datos (entrada).

Responsable: Integrante 1.

Primer hito del proyecto: en lugar de esperar al sensor físico, este script
simula lecturas de temperatura ambiental para poder desarrollar el resto del
sistema (procesamiento, almacenamiento, visualización) desde ya.

Cuando el sensor real esté disponible, reemplazar `leer_sensor()` por la
lectura real (por ejemplo, de un DHT22 u otro sensor ambiental), sin tener
que cambiar el resto del sistema.
"""

import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from procesamiento.procesador import procesar_dato


def leer_sensor():
    """Simula una lectura de temperatura ambiental en grados Celsius."""
    return round(random.uniform(15.0, 38.0), 1)


def iniciar_adquisicion(intervalo_segundos=3, iteraciones=10):
    """Genera lecturas simuladas y las envía al procesador."""
    print("Iniciando adquisición simulada de datos ambientales...")
    for i in range(iteraciones):
        temperatura = leer_sensor()
        print(f"[Sensor] Lectura #{i + 1}: {temperatura} °C")
        procesar_dato(temperatura)
        time.sleep(intervalo_segundos)


if __name__ == "__main__":
    iniciar_adquisicion()
