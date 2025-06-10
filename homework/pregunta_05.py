"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.leer_datos import load_input
from homework.pregunta_03 import extraer_tupla

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    sequence = load_input("files/input")
    sequence = extraer_tupla(sequence,[0,1])
    sequence = [(letra,int(valor))for letra, valor in sequence]
    agrupado = agrupar(sequence)
    print(agrupado)
    resultado = max_min_para_x(agrupado,"descendente")
    print(resultado)
    return resultado

def agrupar(sequence):
    agrupado = {}
    for x, y in sequence:
        if x not in agrupado:
            agrupado[x] = []
        agrupado[x].append(y)
    return agrupado

def max_min_para_x(agrupado,orden):
    resultado = []

    for x in sorted(agrupado.keys()):
        valor_max = max(agrupado[x])
        valor_min = min(agrupado[x])

        if orden == 'descendente':
            resultado.append((x,valor_max,valor_min)) 

        else:
            resultado.append((x,valor_min,valor_max)) 
 
    return resultado



if __name__ == "__main__":
    pregunta_05()