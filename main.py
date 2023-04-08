""" 
Fundamentos de electricidad y magnetismo.
Maria Fernanda Morillo, Carol Rodriguez, Juan Angel Pinzón y Gabriel Estupiñan.
"""

#Librerias:
import os
import matplotlib.pyplot as plt

#Modulos:
from flujo import base

def main():

    while True:
        os.system("cls")
        print("\033[91;1mSimulación Ley de Ohm.\033[0m")
        dato = input("¿Que tipo de datos tienes? \n[1]-Corriente y voltaje. \n[2]-Resistencia y voltaje. \n[3]-Corriente y resistencia.\n[4]-Salir. \n")

        if dato == "1":
            base("Voltaje", "Corriente", "Grafica corriente y voltaje.", 1)

        elif dato == "2":
            base("Voltaje","Resistencia" , "Grafica resistencia y voltaje.", 2)

        elif dato == "3":
            base("Corriente", "Resistencia", "Grafica corriente y resistencia.", 3)

        elif dato == "4":
            return

        else:
            print("Por favor ingrese uno de los numeros disponibles.")
        input("")


if __name__ == "__main__":
    main()