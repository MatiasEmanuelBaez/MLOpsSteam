# Proyecto MLOps con dataset de Steam

## 📋 Descripción del Proyecto

El proyecto consiste en el desarrollo de una API que procesa y entrega información específica a partir de un conjunto de datos de steam. Incluye procesos de limpieza de datos, análisis exploratorio y un modelo de machine learning.

## 🛠️Limpieza de Datos

Para garantizar la calidad y confiabilidad de los datos, se realizaron las siguientes tareas:

* Eliminación de filas duplicadas
* Manejo de valores nulos en columnas críticas
* Corrección formato
* Normalización de datos para consistencia
* Procesamiento de datos anidados (diccionarios y listas)

## 🎯 Endpoints de la API

### 1. PlayTimeGenre

*Retorna el año con más horas jugadas para un género específico.*

### 2. UserForGenre

*Encuentra el usuario con más horas jugadas en un género y muestra la acumulación por año.*

### 3. UsersRecommend

*Top 3 de juegos más recomendados por usuarios en un año específico.*

### 4. UsersNotRecommend

*Top 3 de juegos menos recomendados por usuarios en un año específico.*

### 5. sentiment_analysis

*Análisis de sentimiento de reseñas por año de lanzamiento.*

## 📊 Fuentes de Datos

* Dataset Principal. [Aquí.](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

* Diccionario de Datos. [Aquí.](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link)

## 🚀 Tecnologías Utilizadas

* **Pandas**: Procesamiento y manipulación de datos
* **TextBlob**: Análisis de sentimiento
* **FastAPI**: Desarrollo de la API REST
* **Render**: Deployment y hosting

## 🔗 Deployment

La API está desplegada y disponible. [Aquí.](https://matiasemanuelbaez-mlopssteam.onrender.com/docs)

<br>

*`Proyecto desarrollado como parte de un challenge individual de MLOps`*
