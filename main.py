from typing import Optional
from fastapi import FastAPI

import csv

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/Resultados/{genero}")
def PlayTimeGenre( genero : str ):
    with open('Desarrollo/Resultados/PConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        encontrar=0
        for fila in reader:
            if genero == fila[1]:
                return ("Año de lanzamiento con más horas jugadas para Género",fila[1] ,":", fila[2])
                encontrar=1
                exit
        
        if encontrar == 0:
            return("Género no encontrado")


@app.get("/Resultados/{genero}")
def UserForGenre( genero : str ):
    with open('Desarrollo/Resultados/SConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        encontrar=0
        for fila in reader:
            if genero == fila[1]:
                return ("Año de lanzamiento con más horas jugadas para Género",fila[1] ,":", fila[2])
                encontrar=1
                exit
        
        if encontrar == 0:
            return("Género no encontrado")