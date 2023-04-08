#librerias:
import numpy as np
from sklearn.linear_model import LinearRegression


def regresion_lineal(x:list, y:list):
    X = np.array(x)
    Y = np.array(y)

    X = X.reshape(-1,1)
    reg = LinearRegression().fit(X,Y)
    return reg


def ley_de_ohm(n:int, pendiente, x,y) -> str:
    if n == 1:
        resistencia = 1/pendiente
        return f"Resistencia: {round(float(resistencia), 3)}"
    elif n == 2:
        i = x[0]/y[0]
        for n in range(1, len(x)):
            new_i = x[n]/y[n]
            i = (i+new_i)/2
        return f"Corriente: {round(float(i), 3)}"
    elif n == 3:
        v = x[0]*y[0]
        for n in range(1,len(x)):
            new_v = x[n]*y[n]
            v = (v+new_v)/2
        return f"Voltaje: {round(float(v), 3)}"