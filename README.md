# Proyecto individual nro. 1 - MLOps

Para este desarrollo se utilizó un conjunto de datos para crear una API que entrega resultados específicos. En la carpeta *desarrollo* podrán encontrar archivos .csv con los datos ya trabajados y que corresponden a cada requerimiento explicado mas abajo. También se encuentra un archivo .ipynb que describe el proceso de limpieza de datos realizado para obtener dichos resultados.

El desarrollo de una API con datos limpios es un proceso importante para garantizar la calidad y confiabilidad de los datos que se entregan. En este caso, trabaje sobre las fuentes de datos para obtener ciertos resultados que serán entregados mediante la API.

El proceso de limpieza de datos es una tarea fundamental para garantizar la calidad de los datos. En este desarrollo, se realizaron las siguientes tareas de limpieza:

+ Eliminación de filas duplicadas: Se eliminan las filas que se repiten en las fuentes de datos.
+ Eliminación de valores nulos: Se eliminan los valores nulos de las columnas que son necesarias para las consultas.
+ Corrección de errores de formato: Se corrigen los errores de formato en las columnas de las fuentes de datos.
+ Normalización de los datos: Se normalizan los datos para que tengan el mismo formato.

## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo que requieren ser procesados, tengan en cuenta que hay datos que están anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
<br/>

## **Requerimientos**

+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
+ def **UsersNotRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  
+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 

+ Análisis exploratorio de los datos.
  
+ Modelo de aprendizaje automático.


## **Resolución**

El proyecto se implementó completamente en Python, utilizando las siguientes librerías:

+ Pandas para el procesamiento de datos, que permite cargar y manipular datos en formato tabular.
+ TextBlob para el análisis de sentimiento, que permite identificar el sentimiento de un texto.
+ FastAPI y render para la presentación, que permiten crear una API REST y generar una presentación HTML, respectivamente.

-------------------------------

Se entrega un link de acceso al deploy de la api y un video mostrando el funcionamiento de la misma por si deja de funcionar el servicio gratuito utilizado.

[video](https://youtu.be/-fgHKAYfnYk)

[API](https://matiasemanuelbaez-mlopssteam.onrender.com/docs)