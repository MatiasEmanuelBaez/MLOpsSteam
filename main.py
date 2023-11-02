from typing import Optional
from fastapi import FastAPI

import csv

app = FastAPI()



@app.get("/PlayTimeGenre/{genero}")
def PlayTimeGenre( genero : str ):
    with open('Desarrollo/Resultados/PConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        
        encontrar = 0
        
        for fila in reader:
            if genero == fila[1]:
                return ("Año de lanzamiento con más horas jugadas para Género", fila[1] ,":", fila[2])
                encontrar = 1
                break
        
        if encontrar == 0:
            return("Género no encontrado.")



@app.get("/UserForGenre/{genero}")
def UserForGenre( genero : str ):
    with open('Desarrollo/Resultados/SConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        
        encontrar = 0
        horas = []
        cadena = ''
        
        for fila in reader:
            if genero == fila[3]:
                encontrar = 1
                usuario = fila[1]
                cadena = 'año ' + fila[2] + ": " + str(round(int(fila[4])/60,2)) + ' horas'
                horas.append(cadena)
                
        if encontrar == 0:
            return("Género no encontrado.")
        else:
            return ("Usuario con más horas jugadas para Género", genero,":", usuario, horas)



@app.get("/UsersRecommend/{anio}")
def UsersRecommend( anio : int ):
    with open('Desarrollo/Resultados/TConsulta.csv', newline='') as File:
        reader = csv.reader(File, delimiter=',')
        
        encontrar=0
        puestoU = ""
        uno = 0
        puestoD = ""
        dos = 0
        puestoT = ""
        tres = 0
        x = 0
            
        for fila in reader:
            
            if  fila[4].isnumeric():
                x = int(fila[4]) + int(fila[5])
                
                if anio == int(fila[2]):
                    if fila[1] == "True":                    
                        encontrar = 1
                        if uno == 0:
                            uno = x
                            puestoU = fila[3]
                        else:
                            if int(x) > int(uno):
                                tres = dos
                                puestoT = puestoD
                                dos = uno
                                puestoD = puestoU
                                uno = x
                                puestoU = fila[3]
                            else:
                                if int(x) > int(dos):
                                    tres = dos
                                    puestoT = puestoD
                                    dos = x
                                    puestoD = fila[3]
                                else:
                                    if int(x) > int(tres):
                                        tres = x
                                        puestoT = fila[3]

        if encontrar == 1:
            return ("Puesto 1: ", puestoU, "- Puesto 2: ", puestoD, "- Puesto 3: ", puestoT)  
        else:
            return ("No se encontraron recomendaciones positivas para el año ingresado.")



@app.get("/UsersNotRecommend/{anio}")
def UsersNotRecommend( anio : int ):
    with open('Desarrollo/Resultados/TConsulta.csv', newline='') as File:
        reader = csv.reader(File, delimiter=',')
        
        encontrar = 0
        puestoU = ""
        uno = 0
        puestoD = ""
        dos = 0
        puestoT = ""
        tres = 0
        x = 0
            
        for fila in reader:
            
            if  fila[6].isnumeric():
                x = int(fila[6])
                
                if anio == int(fila[2]):
                    if fila[1] == "False":                    
                        encontrar = 1
                        if uno == 0:
                            uno = x
                            puestoU = fila[3]
                        else:
                            if int(x) > int(uno):
                                tres = dos
                                puestoT = puestoD
                                dos = uno
                                puestoD = puestoU
                                uno = x
                                puestoU = fila[3]
                            else:
                                if int(x) > int(dos):
                                    tres = dos
                                    puestoT = puestoD
                                    dos = x
                                    puestoD = fila[3]
                                else:
                                    if int(x) > int(tres):
                                        tres = x
                                        puestoT = fila[3]

        if encontrar == 1:
            return ("Puesto 1: ", puestoU, "- Puesto 2: ", puestoD, "- Puesto 3: ", puestoT)  
        else:
            return ("No se encontraron recomendaciones negativas para el año ingresado.")



@app.get("/sentiment_analysis/{anio}")
def sentiment_analysis( anio : int ):
    with open('Desarrollo/Resultados/QConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        
        encontrar = 0
        cadena = ''
        
        for fila in reader:
            if  fila[1].isnumeric():
                if anio == fila[1]:
                    cadena = 'Negative= ' + fila[4] + ', Neutral=' + fila[2] + ', Positive=' + fila[3]
                    return (cadena)
                    encontrar = 1
                    break
        
        if encontrar == 0:
            return("Año no encontrado.")
