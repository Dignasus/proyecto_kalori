# Kalori - Predictor de Impacto Calórico

Aplicación de escritorio desarrollada en Python que permite estimar visualmente la proyección de peso corporal a largo plazo. El objetivo del software es fomentar la conciencia sobre el impacto acumulativo del consumo calórico, transformando números abstractos en gráficos visuales de déficit o superávit.

## Tecnologías y Arquitectura
* **Lenguaje:** Python
* **Arquitectura:** Patrón MVC (Modelo-Vista-Controlador)
* **Interfaz Gráfica:** Tkinter
* **Visualización de Datos:** Matplotlib (Generación de curvas de tendencia)
* **Base de Datos:** MySQL (Almacenamiento de historial de simulaciones)
* **Integración:** Preparado para consumo de datos nutricionales mediante API (FatSecret).

## Lógica y Modelo Matemático
El motor de predicción del sistema se basa en principios fisiológicos y matemáticos comprobados:
* Cálculo del Gasto Energético Basal (GEB) mediante la **Fórmula de Harris-Benedict**.
* Aplicación de factores de actividad física para obtener el Gasto Energético Total (GET).
* Ajuste lineal para proyecciones a corto plazo, utilizando la conversión estándar de balance energético (7.700 kcal = 1 kg de variación de peso).

## Características Principales
* Ingreso de perfil fisiológico del usuario (peso, altura, edad, sexo, factor de actividad).
* Cálculo automático del metabolismo basal y gasto calórico total en tiempo real.
* Generación de gráficos interactivos con la tendencia de peso a 4 semanas.
* Persistencia de datos en base de datos relacional para guardar el historial de las simulaciones.

## Estructura del Proyecto
* `main.py`: Controlador principal que orquesta la aplicación y la lógica de negocio.
* `modelo.py`: Gestión de conexión a base de datos MySQL y cálculos matemáticos puros.
* `vista.py`: Interfaz gráfica de usuario (GUI) e integración de gráficos interactivos.

## Instalación y Ejecución
1. Clona este repositorio.
2. Instala las dependencias necesarias ejecutando: 
   `pip install mysql-connector-python matplotlib`
3. Asegúrate de tener tu servidor local MySQL activo (ej. a través de XAMPP).
4. Ejecuta el archivo principal: `python main.py` 
*(Nota: La base de datos `kalori_db` y sus tablas se crearán e inicializarán automáticamente al correr el programa).*
