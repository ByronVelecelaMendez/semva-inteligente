# SEMVA Inteligente

Sistema Embebido para el Monitoreo de Variables Ambientales (SEMVA), evolucionado
para incorporar procesamiento y funciones inteligentes sobre las variables
ambientales adquiridas, aplicado a procesos agrícolas.

**Arquitectura y Organización de Computadores — Grupo 4**

- Del Pezo Rodríguez Julio José
- Dave Javier Carvajal González
- Byron Andrés Velecela Méndez
- Mike Neiman Tomalá Tumbaco
- Jean Pierre Correa Asencio

## Propósito

Transformar datos ambientales crudos (temperatura, humedad, luminosidad, etc.)
en información útil para monitorear, detectar condiciones relevantes y apoyar
decisiones en procesos agrícolas, en lugar de solo mostrarlos sin analizarlos.

## Arquitectura del sistema

    Sensores (entrada) → Procesador → Memoria (buffer temporal)
                                     → Almacenamiento (histórico)
                                           ↓
                                  Salida (pantalla / alertas)

El proyecto separa el código en dos grandes bloques:

- **backend/** — toda la lógica del sistema: adquisición de datos, procesamiento,
  almacenamiento y generación de alertas. Es donde se adquiere, interpreta y
  guarda la información.
- **frontend/** — la capa de visualización, donde el usuario ve los resultados.
  Hoy es una salida por consola; puede evolucionar a un dashboard web sin
  afectar el backend.

| Módulo | Carpeta | Responsable | Descripción |
|---|---|---|---|
| Adquisición de datos | `backend/adquisicion/` | Del Pezo Rodríguez Julio José | Captura/simulación de variables ambientales (entrada). |
| Procesamiento | `backend/procesamiento/` | Dave Javier Carvajal González | Interpreta y analiza los datos (umbrales, reglas, promedios). |
| Almacenamiento | `backend/almacenamiento/` | Byron Andrés Velecela Méndez | Guarda el histórico de variables en base de datos. |
| Visualización | `frontend/visualizacion/` | Mike Neiman Tomalá Tumbaco | Interfaz donde se muestran variables en tiempo real e históricas. |
| Alertas / análisis inteligente | `backend/alertas/` | Jean Pierre Correa Asencio | Detección de condiciones relevantes/anomalías y generación de alertas. |

## Camino mínimo funcional (primer hito)

Antes de conectar sensores reales, el objetivo del primer prototipo es lograr
que **un solo dato simulado** viaje de punta a punta por el sistema:

    dato simulado → se guarda en la base de datos → se muestra en consola/pantalla

Una vez que ese camino funcione, se reemplaza la simulación por el sensor real
y se agregan las alertas/análisis inteligente.

## Requisitos

- Python 3.10+
- pip

## Instalación

    git clone https://github.com/ByronVelecelaMendez/semva-inteligente.git
    cd semva-inteligente
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Ejecución del prototipo mínimo

    python backend\adquisicion\simulador_sensor.py
    python frontend\visualizacion\dashboard.py

## Estructura del repositorio

    semva-inteligente/
    ├── backend/
    │   ├── adquisicion/       # Captura/simulación de sensores (entrada)
    │   ├── procesamiento/     # Lógica de interpretación y análisis
    │   ├── almacenamiento/    # Base de datos / histórico
    │   └── alertas/           # Detección de condiciones y alertas
    ├── frontend/
    │   └── visualizacion/     # Interfaz de visualización
    ├── docs/                  # Documentación, talleres, esquemas
    ├── tests/                 # Pruebas
    ├── requirements.txt
    └── README.md

## Flujo de trabajo en Git

El proyecto usa dos ramas principales:

- **`main`** — siempre estable, lista para mostrar o entregar.
- **`develop`** — donde se integran los módulos de todos mientras están en desarrollo.

Cada integrante trabaja en su propia rama, creada a partir de `develop`:

    git clone https://github.com/ByronVelecelaMendez/semva-inteligente.git
    cd semva-inteligente
    git fetch origin
    git checkout develop
    git checkout -b nombre-del-modulo
    git push -u origin nombre-del-modulo

Flujo diario de trabajo:

    git add .
    git commit -m "descripción breve del cambio"
    git push

1. Hacer commits pequeños y descriptivos.
2. Al terminar un avance, abrir un Pull Request de tu rama hacia **`develop`** (no hacia `main`).
3. `develop` se fusiona hacia `main` solo cuando el sistema integrado funciona de punta a punta (por ejemplo, antes de cada entrega del taller).
4. No hacer `push` directo a `main` ni a `develop` (la rama `develop` está protegida y requiere Pull Request con aprobación).

## Métricas a medir

Tiempos de procesamiento, uso de memoria, almacenamiento, comunicaciones y
desempeño general de la plataforma seleccionada (ver `docs/` para el detalle
de los talleres de Arquitectura de Computadores).
