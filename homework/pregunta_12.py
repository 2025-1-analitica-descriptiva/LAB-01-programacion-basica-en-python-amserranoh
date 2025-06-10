"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.leer_datos import load_input
from homework.pregunta_03 import extraer_tupla
from homework.pregunta_02 import reducer
from homework.pregunta_02 import shuffle


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sequence = load_input ("files/input")
    sequence = extraer_tupla(sequence,[0,4])
    sequence = limpieza (sequence)
    sequence = shuffle(sequence)
    sequence = reducer(sequence)
    sequence = dict(sequence)
    print(sequence)
    return(sequence)

def limpieza (sequence):

    resultado =[]

    for x, y in sequence:
        for l1 in y.strip().split(","):
            for l2 in l1.split(":"):
                if l2.isdigit():
                    resultado.append((x, int(l2)))
            
    print (resultado)
    return resultado
    



   

   


if __name__ == "__main__":
    pregunta_12()