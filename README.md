# ProyectoML2025
# Proyecto de Predicción de Riesgo de Hipertensión Arterial
#### Carmen casco
#### Melany ramirez
#### Samuel Colmenarez 

 ## Descripción general
Este proyecto desarrolla una solución de Machine Learning que predice el riesgo de hipertensión arterial basado en datos clínicos. Utiliza un modelo de AdaBoost entrenado sobre el dataset Hipertension_Arterial_Mexico.csv.
Se incluyen scripts para reentrenamiento automático con una interfaz gráfica web usando Streamlit y pipelines de CI/CD para automatizar el flujo de trabajo.

 ## Estructura del repositorio

PROYECTO/
├── .github/workflows/main.yml       # Pipeline de CI/CD con GitHub Actions
├── model/Adaboost.pkl                # Modelo entrenado
├── app.py                            # Aplicación web con Streamlit
├── main.py                           # API con FastAPI para consumo del modelo
├── retraining.py                     # Script de reentrenamiento del modelo
├── descargar_data.py                 # Script para descarga de datos
├── Dockerfile                        # Dockerización del proyecto
├── Hipertension_Arterial_Mexico.csv  # Dataset base
├── metrics.txt                       # Resultados de evaluación del modelo
├── .deepsource.toml                  # Configuración de análisis de código (DeepSource)
├── requirements.txt                  # Dependencias del proyecto
├── README.md                         # Este documento
├── LICENSE                           # Licencia del proyecto
└── otros archivos de configuración (.gitignore, .dockerignore, etc.)


## La interfaz estará disponible en el navegador.

http://ec2-3-86-189-113.compute-1.amazonaws.com/

### Links relacionados 
 [Docker Hub](https://hub.docker.com/repositories/samcfer)


## Reentrenamiento automático (CI/CD)
Cada vez que se detectan cambios en develop y se fusionan a staging, GitHub Actions ejecuta el reentrenamiento automático usando el workflow .github/workflows/main.yml.

 ## Inputs y Outputs del Modelo
Inputs esperados (features de entrada):

| sexo | edad | concentracion_hemoglobina | temperatura_ambiente | valor_acido_urico | valor_albumina | valor_colesterol_hdl | valor_colesterol_ldl | valor_colesterol_total | valor_creatina | resultado_glucosa | valor_insulina | valor_trigliceridos | resultado_glucosa_promedio | valor_hemoglobina_glucosilada | valor_ferritina | valor_folato | valor_homocisteina | valor_proteinac_reactiva | valor_transferrina | valor_vitamina_bdoce | valor_vitamina_d | peso  | estatura | medida_cintura | segundamedicion_peso | segundamedicion_estatura | distancia_rodilla_talon | circunferencia_de_la_pantorrilla | segundamedicion_cintura | tension_arterial | sueno_horas | masa_corporal | actividad_total | riesgo_hipertension |
|------|------|---------------------------|----------------------|-------------------|----------------|----------------------|----------------------|------------------------|----------------|-------------------|----------------|---------------------|----------------------------|------------------------------|-----------------|--------------|-------------------|--------------------------|---------------------|----------------------|-----------------|-------|----------|----------------|----------------------|-------------------------|------------------------|--------------------------------|------------------------|-----------------|-------------|---------------|----------------|---------------------|
| 2    | 35   | 14.2                      | 22                   | 4.8               | 4              | 34                   | 86                   | 139                    | 0.58           | 92                | 4              | 123                 | 103                        | 5.2                          | 2.7             | 23.4         | 4.9               | 0.02                     | 1.1                 | 167                  | 20.8            | 98.7  | 159.4    | 125.2          | 64.7                 | 154                     | 48.5                  | 33.5                         | 222.2                  | 105             | 2           | 37.41239517   | 120            | Si tiene hipertension                   |
| 2    | 53   | 14.2                      | 22                   | 4.8               | 4              | 34                   | 86                   | 139                    | 0.58           | 92                | 4              | 123                 | 103                        | 5.2                          | 2.7             | 23.4         | 4.9               | 0.02                     | 1.1                 | 167                  | 20.8            | 55.9  | 151.4    | 222.2          | 64.7                 | 154                     | 48.5                  | 33.5                         | 222.2                  | 121             | 3           | 23.40945307   | 540            | NO tiene hipertension                   |


etc.

(La lista exacta depende del dataset Hipertension_Arterial_Mexico.csv usado.)

Output:

Predicción binaria:

0: Bajo riesgo de hipertensión

1: Alto riesgo de hipertensión

Versionamiento y flujo de trabajo
El proyecto sigue el siguiente esquema de ramas:

main: Rama principal estable (producción).

develop: Desarrollo principal del equipo.

staging: Preparación para producción, pruebas de integración.

Cada cambio se integra mediante Pull Requests siguiendo buenas prácticas de colaboración.

CI/CD Automatización
Se utiliza GitHub Actions para:

Reentrenar el modelo en cada push a develop o staging.

Ejecutar pruebas automáticas.

Análisis estático del código (DeepSource).

Despliegue automático a servidor en la nube.

### Análisis de Seguridad del Código
Se realiza análisis estático y control de calidad mediante:

DeepSource configurado en .deepsource.toml.
No code was selected to improve.