"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.leer_datos import load_input
from homework.pregunta_02 import extraer_columna
from homework.pregunta_05 import agrupar 
from homework.pregunta_05 import max_min_para_x

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    sequence = load_input ("files/input")
    sequence = extraer_columna(sequence,4)
    sequence = [linea.strip() for linea in sequence] # Asegura que no haya saltos de línea
    sequence = [linea.split(",") for linea in sequence]
    sequence = construir_tuplas(sequence)
    sequence = agrupar(sequence)
    sequence = max_min_para_x(sequence,"ascendente")
    
    print((sequence))
    return(sequence)
    
    
def construir_tuplas (sequence):
    tuplas = []
    for lista in sequence:
        for par in lista:
            clave, valor = par.split(":")
            tuplas.append((clave, int(valor)))
    return tuplas
    
    
    

    


if __name__ == "__main__":
    pregunta_06()