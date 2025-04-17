# Nombre del Proyecto

*"Aplicación gráfica creada con PyQt6 para gestionar tareas personales."*

## ✅ Requisitos basicos

- Python 3.x
- Asegurate de tener Python agregado al PATH.

## 🛠️ Cómo instalar y ejecutar

Paso 1: Clonar el repositorio o descargar.

    git clone https://github.com/Nosomute/app.git

Paso 2: Crear y activar un entorno virtual

En Windows:

    python -m venv venv
    venv\Scripts\activate

¡Si la ejecución de scripts está deshabilitada!

    et-ExecutionPolicy RemoteSigned -Scope CurrentUser
    venv\Scripts\activate


En macOS / Linux:

    python -m venv venv
    source venv/bin/activate

Paso 3: Instalar las dependencias

    pip install -r requirements.txt

Paso 4: Ejecutar la aplicación

    python src\main.py

## 📂 Estructura del Proyecto
app/ 🖥️
│
├── data/ 📊                # Carpeta para los datos (train, test)
│   ├── train.csv 📈        # Datos de entrenamiento
│   └── test.csv 🧪         # Datos de prueba
│
├── models/ 🤖              # Carpeta para el modelo guardado
│   └── model.pkl 🗃️        # Modelo entrenado guardado
│
├── assets/ 🎨           # Carpeta para los recursos (imágenes, iconos, etc.)
│   ├── icons/ 🖼️           # Carpeta para iconos
│   │   └── icon.qrc 💡 # Icono para guardar archivo
│   │
│   └── img/ 📸          # Carpeta para otras imágenes
│       └── background.png 🌄
│
├── src/ 💻                 # Código fuente de la app
│   ├── ui/ 🖥️              # Archivos relacionados con la interfaz de usuario
│   │   └── mainwindow.ui 🖱️      # Archivo .ui generado por Qt Designer
│   │
│   ├── main.py 📝           # Script principal de la app (PyQt6)
│   ├── ml_model.py 🤓      # Funciones para cargar y usar el modelo de ML
│   └── ui_handler.py ⚙️    # Código para manejar la interfaz desde el archivo .ui
│
├── notebooks/ 📓           # Carpeta para Jupyter Notebooks (opcional)
│   └── training.ipynb 🧑‍🏫   # Notebook para entrenar el modelo
│
├── requirements.txt 📜     # Dependencias del proyecto
└── README.md 📚            # Documentación del proyecto


## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consultá el archivo LICENSE para más información.