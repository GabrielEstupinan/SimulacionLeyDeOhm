#Librerias:
import os
import numpy as np

#Modulos:
from input_datos import input_datos
from graficar import graficar
from calcular import ley_de_ohm, regresion_lineal


def base(x_nombre:str, y_nombre:str, title, n):
    os.system("cls")
    print(f"{title}")
    print(f"\033[33m{x_nombre}:\033[0m")
    x = input_datos()
    print(f"\n\033[33m{y_nombre}:\033[0m")
    y = input_datos()
    if len(x) != len(y):
        print("La cantidad de datos suministrados difiere en cada lista.\nIntentalo nuevamente.")
    else:
        pendiente = regresion_lineal(x, y)
        resultado = ley_de_ohm(n, pendiente.coef_, x, y)
        graficar(x, y, x_nombre, y_nombre, title, pendiente, resultado)