"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.leer_datos import load_input

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sequence = load_input("files/input")
    suma = 0
    for x,y in sequence:
        var = y.split("\t")
        suma = suma + int(var[1])      
    print(suma)
    return suma

if __name__ == "__main__":
    pregunta_01()