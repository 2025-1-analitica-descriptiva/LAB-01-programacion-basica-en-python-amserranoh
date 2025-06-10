"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.leer_datos import load_input
from homework.pregunta_03 import extraer_tupla
from homework.pregunta_02 import shuffle
from homework.pregunta_02 import reducer


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sequence = load_input ("files\input")
    sequence = extraer_tupla(sequence,[3,1])
    sequence = combinaciones (sequence)
    sequence = shuffle(sequence)
    sequence = reducer(sequence) 
    sequence = dict(sequence)

    print(sequence)
    return(sequence)

def combinaciones (sequence):
    resultado = []
    for x,y in sequence:
        for x in x.split(","):
            resultado.append((x, int(y)))
    return resultado

if __name__ == "__main__":
    pregunta_11()