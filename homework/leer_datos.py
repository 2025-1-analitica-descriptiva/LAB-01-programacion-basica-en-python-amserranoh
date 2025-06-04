import glob
import fileinput

def load_input(datos):
    
    sequence = []
    archivo = glob.glob(f"{datos}/*")

    with fileinput.input(files = archivo) as d:
        #print("imprime:d "+ str(d))
        for line in d:
            sequence.append((fileinput.filename(), line))
    return sequence

"""
if __name__ == "__main__":
    load_input("files/input")
"""