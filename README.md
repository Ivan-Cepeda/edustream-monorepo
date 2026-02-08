# 🎓 EduStream: Monorepo Architecture Demo

Este repositorio demuestra una implementación práctica de una arquitectura Monorepo para un sistema de Machine Learning end-to-end.

Simula el entorno de EduStream, una startup educativa donde los equipos de Data Science (ML) y Desarrollo Backend (API) conviven en el mismo repositorio para maximizar la velocidad de desarrollo y la reutilización de código.

## 🏗️ Arquitectura del Proyecto
En este diseño, todos los componentes del sistema residen bajo un mismo control de versiones. Esto permite una Alta Cohesión entre módulos:

🟢 **Core (/core)**: Librería compartida (Shared Library). Contiene lógica de negocio y funciones de limpieza de datos que deben ser idénticas tanto en el entrenamiento como en la producción.

🟡 **ML Pipeline (/ml)**: Módulo encargado del entrenamiento. Importa el core, procesa datos y genera el modelo serializado (.pkl).

🔵 **API Service (/api)**: Módulo de inferencia. Consume el modelo generado por el equipo de ML leyendo directamente del disco local.

Estructura de Carpetas
Bash
edustream-monorepo/
├── core/               # 🧠 Lógica Compartida (Single Source of Truth)
│   ├── __init__.py
│   └── transform.py    # Funciones de normalización de datos
├── ml/                 # 🍳 Cocina de Datos (Training)
│   ├── models/         # Carpeta donde se guardan los .pkl (Artefactos)
│   ├── train_monorepo.py # Script de entrenamiento
│   └── __init__.py
├── api/                # 🍽️ Servicio Web (Inference)
│   ├── app_monorepo.py   # Script de simulación de API
│   └── __init__.py
└── README.md           # Documentación

## 🚀 Guía de Inicio Rápido
Sigue estos pasos para replicar el ciclo de vida de ML Ops (Entrenamiento -> Despliegue) en tu máquina local.

1. **Prerrequisitos**
Asegúrate de tener instalado Python 3.8+.

2. **Clonar el Repositorio**
Bash
git clone https://github.com/TU_USUARIO/edustream-monorepo.git
cd edustream-monorepo
3. **Ejecutar el Pipeline de Entrenamiento (Equipo ML)**
El equipo de ML utiliza las funciones del core para limpiar los datos y entrena el modelo.

#### Comando:

Bash
python ml/train_monorepo.py
Salida esperada: Verás cómo el script importa core.transform, procesa los datos y guarda un archivo churn_model.pkl dentro de la carpeta ml/models.

**Nota**: Observa en el código cómo usamos sys.path.append para acceder a la carpeta hermana core.

4. **Ejecutar el Servicio de API (Equipo Backend)**
Una vez entrenado el modelo, la API simula levantar un servicio que carga ese modelo desde el disco.

#### Comando:

Bash
python api/app_monorepo.py
Salida esperada: La API encontrará el archivo .pkl generado en el paso anterior y confirmará que está lista para hacer predicciones.

## 🧠 Conceptos Clave para Estudiantes
Al revisar el código de este repositorio, presta atención a los siguientes puntos de ML Ops:

1. **Single Source of Truth (Fuente Única de Verdad)**
Abre ml/train_monorepo.py y api/app_monorepo.py. Notarás que ambos hacen:

Python
from core.transform import normalize_data
Esto garantiza que si cambiamos la lógica de limpieza en el core, ambos sistemas se actualizan automáticamente sin versiones desalineadas.

2. **Dependencia de Rutas (High Coupling)**
La API carga el modelo así:

Python
Path(__file__).parent.parent / 'ml' / 'models' / 'churn_model.pkl'
**Reflexión**: Esto es muy rápido (cero latencia de red), pero crea un acoplamiento fuerte. Si el equipo de ML decide cambiar el nombre de la carpeta models a artefactos, la API se romperá inmediatamente.

3. **Ciclo de Vida Simplificado**
En un Monorepo, no necesitamos un "Artifact Registry" (como S3 o MLflow) obligatoriamente para empezar. El sistema de archivos local actúa como nuestro medio de intercambio.

### 🛠️ Troubleshooting
*Error*: ModuleNotFoundError: No module named 'core' Si obtienes este error, asegúrate de estar ejecutando los comandos desde la raíz del repositorio (edustream-monorepo/), no desde dentro de las carpetas ml o api.

*Error*: No se encuentra el artefacto al correr la API Recuerda que primero debes ejecutar el entrenamiento (ml/train_monorepo.py) para que el archivo .pkl exista físicamente.

#### gi📝 Licencia
Este proyecto es parte del material educativo de Soy Henry - Carrera de Data Science - Módulo 5.
