"""
Módulo de alertas / análisis inteligente.

Responsable: Integrante 5.

Evalúa si una lectura representa una condición relevante y genera una
alerta. Este es el punto de partida sobre el cual más adelante se puede
construir detección de anomalías o predicción (ver "¿Hasta dónde puede
crecer?" en la matriz del proyecto).
"""


def evaluar_condicion(temperatura, umbral_min, umbral_max):
    if temperatura < umbral_min:
        print(f"[ALERTA] Temperatura baja: {temperatura} °C (posible riesgo de helada)")
    elif temperatura > umbral_max:
        print(f"[ALERTA] Temperatura alta: {temperatura} °C (posible estrés térmico)")
    else:
        print(f"[OK] Temperatura dentro de rango normal: {temperatura} °C")
