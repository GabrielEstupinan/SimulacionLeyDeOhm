def input_datos():

    datos_str = input("Escribe todos los datos que obtuviste colocando una coma entre ellos:\n")
    datos_array = datos_str.split(",")
    datos = list(map(float, datos_array))
    return datos