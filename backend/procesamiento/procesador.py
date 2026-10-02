"""
Módulo de procesamiento.

Responsable: Integrante 2.

Interpreta y analiza los datos recibidos desde la adquisición: aplica reglas
simples (umbrales) y decide qué hacer con cada lectura antes de guardarla y
antes de pasarla al módulo de alertas.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from almacenamiento.db import guardar_lectura
from alertas.alertas import evaluar_condicion

UMBRAL_MIN = 10.0
UMBRAL_MAX = 35.0


def procesar_dato(temperatura):
    """Procesa una lectura: la guarda y evalúa si amerita una alerta."""
    guardar_lectura(temperatura)
    evaluar_condicion(temperatura, UMBRAL_MIN, UMBRAL_MAX)
