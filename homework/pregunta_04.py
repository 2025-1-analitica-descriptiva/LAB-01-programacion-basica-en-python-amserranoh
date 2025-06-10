"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

"""

from homework.leer_datos import load_input
from homework.pregunta_02 import extraer_columna
from homework.pregunta_02 import mapper
from homework.pregunta_02 import shuffle
from homework.pregunta_02 import reducer

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    sequence = load_input ("files/input")
    sequence = extraer_columna(sequence,2)
    sequence = [mes.split("-")[1] for mes in sequence]
    sequence = mapper(sequence)
    sequence = shuffle(sequence)
    sequence = reducer(sequence)
    print(sequence)
    return(sequence)


if __name__ == "__main__":
    pregunta_04()
