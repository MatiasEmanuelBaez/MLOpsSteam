from typing import Optional
from fastapi import FastAPI

import csv

app = FastAPI()



@app.get("/PlayTimeGenre/{genero}")
def PlayTimeGenre( genero : str ):
    with open('Desarrollo/Resultados/PConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        encontrar=0
        for fila in reader:
            if genero == fila[1]:
                return ("Año de lanzamiento con más horas jugadas para Género",fila[1] ,":", fila[2])
                encontrar=1
                break
        
        if encontrar == 0:
            return("Género no encontrado.")



@app.get("/UserForGenre/{genero}")
def UserForGenre( genero : str ):
    with open('Desarrollo/Resultados/SConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        encontrar=0
        for fila in reader:
            if genero == fila[3]:
                return ("Usuario con más horas jugadas para Género",fila[3] ,":", fila[1])
                encontrar=1
                break
        
        if encontrar == 0:
            return("Género no encontrado.")



@app.get("/UsersRecommend/{anio}")
def UsersRecommend( anio : int ):
    with open('Desarrollo/Resultados/TConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        
        encontrar=0
        
        puestoU = ""
        uno = 0
        
        puestoD = ""
        dos = 0
        
        puestoT = ""
        tres = 0
        
        x = 0
        
        for fila in reader:
            x == fila[4]+fila[5]
            if anio == fila[2]:
                if fila[1] == True:
                    encontrar = 1
                    if uno == 0:
                        uno == x
                        puestoU == fila[3]
                    else:
                        if x > uno:
                            tres == dos
                            puestoT == puestoD
                            dos == uno
                            puestoD == puestoU
                            uno == x
                            puestoU == fila[3]
                        else:
                            if x > dos:
                                tres == dos
                                puestoT == puestoD
                                dos == x
                                puestoD == fila[3]
                            else:
                                if x > tres:
                                    tres == x
                                    puestoT == fila[3]

    if encontrar == 1:
        print ("Puesto 1: ", puestoU, "- Puesto 2: ", puestoD, "- Puesto 3: ", puestoT)  
    else:
        print ("No se encontraron recomendaciones positivas para el año ingresado.")



@app.get("/UsersNotRecommend/{anio}")
def UsersNotRecommend( anio : int ):
    with open('Desarrollo/Resultados/TConsulta.csv', newline='') as File:
        reader = csv.reader(File)
        
        encontrar=0
        
        puestoU = ""
        uno = 0
        
        puestoD = ""
        dos = 0
        
        puestoT = ""
        tres = 0
        
        x = 0
        
        for fila in reader:
            x == fila[6]
            if anio == fila[2]:
                if fila[1] == False:
                    encontrar = 1
                    if uno == 0:
                        uno == x
                        puestoU == fila[3]
                    else:
                        if x > uno:
                            tres == dos
                            puestoT == puestoD
                            dos == uno
                            puestoD == puestoU
                            uno == x
                            puestoU == fila[3]
                        else:
                            if x > dos:
                                tres == dos
                                puestoT == puestoD
                                dos == x
                                puestoD == fila[3]
                            else:
                                if x > tres:
                                    tres == x
                                    puestoT == fila[3]

    if encontrar == 1:
        print ("Puesto 1: ", puestoU, "- Puesto 2: ", puestoD, "- Puesto 3: ", puestoT)  
    else:
        print ("No se encontraron recomendaciones negativas para el año ingresado.")