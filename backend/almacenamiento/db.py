"""
Módulo de almacenamiento.

Responsable: Integrante 3.

Guarda el histórico de variables ambientales en una base de datos SQLite
local (simple y suficiente para el prototipo inicial; se puede migrar a
otra base de datos más adelante si el proyecto lo requiere).
"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "semva.db")


def inicializar_db():
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lecturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temperatura REAL NOT NULL,
                fecha_hora TEXT NOT NULL
            )
        """)
        conexion.commit()
    except sqlite3.Error as error:
        print(f"[Almacenamiento] Error al inicializar la base de datos: {error}")
    finally:
        if conexion:
            conexion.close()


def guardar_lectura(temperatura):
    inicializar_db()
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO lecturas (temperatura, fecha_hora) VALUES (?, ?)",
            (temperatura, datetime.now().isoformat()),
        )
        conexion.commit()
        print(f"[Almacenamiento] Lectura guardada: {temperatura} °C")
    except sqlite3.Error as error:
        print(f"[Almacenamiento] Error al guardar la lectura ({temperatura} °C): {error}")
    finally:
        if conexion:
            conexion.close()


def obtener_historico(limite=20):
    inicializar_db()
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT temperatura, fecha_hora FROM lecturas ORDER BY id DESC LIMIT ?",
            (limite,),
        )
        return cursor.fetchall()
    except sqlite3.Error as error:
        print(f"[Almacenamiento] Error al obtener el histórico: {error}")
        return []
    finally:
        if conexion:
            conexion.close()
