# Clasificador de Propinas para Viajes en Taxi en NYC (2020)

Este proyecto implementa un modelo de clasificación binaria que predice si un viaje en taxi en Nueva York tuvo una propina alta (mayor al 20% de la tarifa). Se basa en los datos públicos de NYC Taxi & Limousine Commission para el año 2020 y sigue buenas prácticas de ingeniería de software aplicadas a ciencia de datos.

## 📁 Estructura del Proyecto
Tarea-1-DP/

├─ data/
│ └── processed/ # Datos preprocesados (taxi_train.parquet)

├── models/ # Modelo entrenados (joblib)

├── notebooks/

│ ├── 01_data_prep.ipynb # Carga y preprocesamiento de datos

│ ├── 02_model_train.ipynb # Entrenamiento y evaluación inicial

│ └── 03_eval.ipynb # Evaluación del modelo en múltiples meses

├── src/

│ ├── data/

│ │ └── dataset.py # Función para cargar datos desde parquet

│ ├── features/

│ │ └── build_features.py # Limpieza, variables y creación de target

│ ├── modeling/

│ │ └── train.py # Entrenamiento del modelo

│ │ └── predict.py # Evaluación del modelo y cálculo de F1-score

│ └── visualization/

│ └── plots.py # Gráficos de resultados y distribución de clases

└── README.md

## Cómo ejecutar el proyecto

### 1. Preprocesamiento de datos ('01_data_prep.ipynb')
- Descarga los datos de enero desde la URL pública.
- Aplica la función `preprocess()`.
- Guarda un subset de 100.000 ejemplos en 'data/processed/taxi_train.parquet'.

### 2. Entrenamiento del modelo ('02_model_train.ipynb')
- Carga el dataset procesado.
- Entrena un modelo 'RandomForestClassifier'.
- Calcula el F1-score de entrenamiento.
- Guarda el modelo en 'models/random_forest.joblib'.

### 3. Evaluación mensual (`03_eval.ipynb`)
- Evalúa el modelo en los datos de febrero a septiembre de 2020.
- Calcula F1-score y distribución de clases por mes.
- Genera visualizaciones de rendimiento y clases.
- Analiza patrones temporales en el rendimiento del modelo.


## Ejemplo de tabla de resultados 

| Mes      | Ejemplos | F1-score | % High Tip | % Low Tip |
|----------|----------|----------|-------------|------------|
| 2020-02  | 6,276,854 | 0.3593   | 57.35%      | 42.65%     |
| 2020-04  |   236,611 | 0.5194   | 42.29%      | 57.71%     |
| 2020-06  |   546,843 | 0.4763   | 44.63%      | 55.37%     |
| 2020-09  | 1,334,414 | 0.4493   | 51.64%      | 48.36%     |

## Análisis y conclusiones

- El F1-score fue bajo en febrero-marzo, aumentó en abril y luego se estabilizó entre mayo y septiembre.
- Cambios abruptos en proporciones de clases y cantidad de datos reflejan eventos externos (pandemia, confinamiento, etc.).
- Se recomienda:
  - Entrenar con múltiples meses de datos.
  - Reentrenar periódicamente.
  - Evaluar variables contextuales (clima, feriados, etc.).

## Requisitos

- Python 3.8+
- pandas
- scikit-learn
- joblib
- matplotlib

Desarrollado por Vicente Gallardo.