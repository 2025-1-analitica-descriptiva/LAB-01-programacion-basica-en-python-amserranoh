"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

"""
from homework.leer_datos import load_input
from homework.pregunta_02 import reducer
from homework.pregunta_02 import shuffle

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    sequence = load_input("files/input")
    sequence = extraer_tupla(sequence,[0,1])
    sequence = [(letra,int(valor))for letra, valor in sequence]
    sequence = shuffle(sequence)
    sequence = reducer(sequence)
    print(sequence)
    return (sequence)

def extraer_tupla(sequence, indices):
    return [
        tuple(linea.split("\t")[i] for i in indices)
        for _, linea in sequence
    ]

if __name__ == "__main__":
    pregunta_03()