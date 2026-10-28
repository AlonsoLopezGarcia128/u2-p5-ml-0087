# Alonso Lopez Garcia NC = 0087 | Fecha 28/10/2026
import numpy as np
import pandas as pd

# Datos matriz 4 x 3
datos_alumnos = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# Poner nombre a las columnas
# Y almacenar la tabla en la variable df  dataframe 
print("--- Datos a partir de una matriz 4x3 0087 ---")
df = pd.DataFrame(datos_alumnos, columns= ["ci", "marcas", "paquete"])
print(df)

#Datos a partir de un diccionario
print(" ")
print("--- Datos a partir de un diccionario 0087 ---")
aluumno_diccionario = {
    "nombre":["Alonso", "Matias", "Pedro", "Andres", "Catherine"],
    "calificaciones":[100, 67, 60, 99, 65],
    "edad": [16, 5, 20, 15, 4]
}
estudiantes =  pd.DataFrame(aluumno_diccionario)

print(estudiantes)

print(" ")
print("Alonso Lopez Garcia NC = 0087 | Fecha 28/10/2026")