"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby
from homework.leer_datos import load_input

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    sequence = load_input("files/input")
    sequence = extraer_columna(sequence,0)
    sequence = mapper(sequence)
    sequence = shuffle(sequence)
    sequence = reducer(sequence)
    print(sequence)
    return(sequence)

def extraer_columna (sequence, col):
    return [linea.split("\t")[col] for _, linea in sequence]

def mapper(sequence):
    return [(word, 1) for value in sequence for word in value.split()]

def shuffle(word):
    return sorted(word, key=lambda x: x[0])

def reducer(sequence):
    result = []
    for key, group in groupby(sequence, lambda x: x[0]):
        result.append(
            (
                key, sum(value for _, value in group)
            )
        )
    return result
    
if __name__ == "__main__":
    pregunta_02()