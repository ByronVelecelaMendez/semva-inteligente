# SEMVA Inteligente

Sistema Embebido para el Monitoreo de Variables Ambientales (SEMVA), evolucionado
para incorporar procesamiento y funciones inteligentes sobre las variables
ambientales adquiridas, aplicado a procesos agrícolas.

**Arquitectura y Organización de Computadores — Grupo 4**

- Del Pezo Rodríguez Julio José
- Dave Javier Carvajal González
- Byron Andrés Velecela Méndez

## Propósito

Transformar datos ambientales crudos (temperatura, humedad, luminosidad, etc.)
en información útil para monitorear, detectar condiciones relevantes y apoyar
decisiones en procesos agrícolas, en lugar de solo mostrarlos sin analizarlos.

## Arquitectura del sistema

```
Sensores (entrada) → Procesador → Memoria (buffer temporal)
                                 → Almacenamiento (histórico)
                                       ↓
                              Salida (pantalla / alertas)
```

| Módulo | Carpeta | Responsable | Descripción |
|---|---|---|---|
| Adquisición de datos | `adquisicion/` | Integrante 1 | Captura/simulación de variables ambientales (entrada). |
| Procesamiento | `procesamiento/` | Integrante 2 | Interpreta y analiza los datos (umbrales, reglas, promedios). |
| Almacenamiento | `almacenamiento/` | Integrante 3 | Guarda el histórico de variables en base de datos. |
| Visualización | `visualizacion/` | Integrante 4 | Interfaz donde se muestran variables en tiempo real e históricas. |
| Alertas / análisis inteligente | `alertas/` | Integrante 5 | Detección de condiciones relevantes/anomalías y generación de alertas. |

## Camino mínimo funcional (primer hito)

Antes de conectar sensores reales, el objetivo del primer prototipo es lograr
que **un solo dato simulado** viaje de punta a punta por el sistema:

```
dato simulado → se guarda en la base de datos → se muestra en consola/pantalla
```

Una vez que ese camino funcione, se reemplaza la simulación por el sensor real
y se agregan las alertas/análisis inteligente.

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
git clone <url-del-repo>
cd semva-inteligente
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución del prototipo mínimo

```bash
python adquisicion/simulador_sensor.py
```

## Estructura del repositorio

```
semva-inteligente/
├── adquisicion/        # Captura/simulación de sensores (entrada)
├── procesamiento/       # Lógica de interpretación y análisis
├── almacenamiento/      # Base de datos / histórico
├── visualizacion/       # Interfaz de visualización
├── alertas/              # Detección de condiciones y alertas
├── docs/                 # Documentación, talleres, esquemas
├── tests/                 # Pruebas
├── requirements.txt
└── README.md
```

## Flujo de trabajo en Git

1. Cada integrante trabaja en una rama propia a partir de `main`:
   ```bash
   git checkout -b nombre-del-modulo
   ```
2. Hacer commits pequeños y descriptivos.
3. Al terminar, abrir un Pull Request hacia `main` para revisión del equipo.
4. No hacer `push` directo a `main`.

## Métricas a medir

Tiempos de procesamiento, uso de memoria, almacenamiento, comunicaciones y
desempeño general de la plataforma seleccionada (ver `docs/` para el detalle
de los talleres de Arquitectura de Computadores).
