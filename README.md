# Proyecto individual nro. 1 - MLOps

En este desarrollo, se utilizó un conjunto de datos para crear una API que entrega resultados específicos. En la carpeta *desarrollo* podrán encontrar archivos .csv con los datos ya trabajados y que corresponden a cada requerimiento explicado mas abajo. También se encuentra un archivo .ipynb que describe el proceso de limpieza de datos realizado para obtener dichos resultados.

El desarrollo de una API con datos limpios es un proceso importante para garantizar la calidad y confiabilidad de los datos que se entregan. En este caso, trabaje sobre las fuentes de datos adjuntos para obtener ciertos resultados que serán entregados mediante una API.

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

<sub> Debes crear las siguientes funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).<sub/>

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

> `Importante`<br>
El MVP _debe_ ser una API que pueda ser consumida segun los criterios de [API REST o RESTful](https://rockcontent.com/es/blog/api-rest/) desde cualquier dispositivo conectado a internet. Algunas herramientas como por ejemplo, Streamlit, si bien pueden brindar una interfaz de consulta, no cumplen con las condiciones para ser consideradas una API, sin workarounds.

+ Análisis exploratorio de los datos:
  
Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables del dataset, ver si hay outliers o anomalías, y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Las nubes de palabras dan una buena idea de cuáles palabras son más frecuentes en los títulos, ¡podría ayudar al sistema de predicción! En esta ocasión vamos a pedirte que no uses librerías para hacer EDA automático ya que queremos que pongas en práctica los conceptos y tareas involucrados en el mismo.

+ Modelo de aprendizaje automático:

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un **sistema de recomendación**. Para ello, te ofrecen dos propuestas de trabajo: En la primera, el modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar la *similitud del coseno*. 
La otra propuesta para el sistema de recomendación debe aplicar el filtro user-item, esto es tomar un usuario, se encuentran usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron. En este caso el input es un usuario y el output es una lista de juegos que se le recomienda a ese usuario, en general se explican como “A usuarios que son similares a tí también les gustó…”. 
Deben crear al menos **uno** de los dos sistemas de recomendación.

## **Resolución**
Se entrega un link de acceso al deploy de la api y un video mostrando el funcionamiento de la misma por si deja de funcionar el servicio gratuito utilizado.

[API REST o RESTful](https://rockcontent.com/es/blog/api-rest/)

[API REST o RESTful](https://rockcontent.com/es/blog/api-rest/)