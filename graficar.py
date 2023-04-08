import matplotlib.pyplot as plt


def graficar(x:list, y:list, x_label:str, y_label:str, title:str, pendiente, resultado:str):

    regresion = [pendiente.coef_*x_valor +pendiente.intercept_ for x_valor in x]

    plt.scatter(x, y)
    plt.plot(x, regresion, 'r-', label=resultado)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()


    plt.show()