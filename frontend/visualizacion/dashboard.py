"""
Módulo de visualización (frontend).

Responsable: Integrante 4.

Punto de partida simple: muestra el histórico de lecturas en consola.
Se puede evolucionar hacia una interfaz web (Flask/Streamlit) o una
pantalla dedicada más adelante.
"""

import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(ROOT, "backend"))

from almacenamiento.db import obtener_historico


def mostrar_historico():
    lecturas = obtener_historico()
    print("\n=== Histórico de variables ambientales (más recientes primero) ===")
    if not lecturas:
        print("Todavía no hay lecturas registradas.")
        return
    for temperatura, fecha_hora in lecturas:
        print(f"{fecha_hora} -> {temperatura} °C")


if __name__ == "__main__":
    mostrar_historico()
