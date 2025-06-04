"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.leer_datos import load_input
from homework.pregunta_02 import extraer_columna
from homework.pregunta_06 import construir_tuplas
from homework.pregunta_02 import mapper
from homework.pregunta_02 import shuffle
from homework.pregunta_02 import reducer

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    sequence = load_input ("files\input")
    sequence = extraer_columna(sequence,4)
    sequence = [linea.strip() for linea in sequence] 
    sequence = [linea.split(",") for linea in sequence]
    sequence = construir_tuplas(sequence)
    sequence = [clave for clave, _ in sequence]  
    sequence = mapper(sequence)
    sequence = shuffle(sequence)
    sequence = reducer(sequence) 
    sequence = dict(sequence)

    print(sequence)
    return(sequence)

if __name__ == "__main__":
    pregunta_09()