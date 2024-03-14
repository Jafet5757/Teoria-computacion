""" 
  Genera un universo de lenguaje hasta el k-ésimo nivel
  las palabras binarias (*,.) hasta la longitud k
  k es la cantidad de simbolos que tiene la palabra
"""
import time
import numpy as np


def generateCombinations(k, symbols, filename='combinations.csv'):
  """
    Genera todas las combinaciones de los simbolos para un alfabeto binario
  """
  # Vaciando el archivo
  with open(filename, 'w') as file:
    file.write('')

  # Generando las combinaciones
  with open(filename, 'a') as file:
    file.write('combination\n')
    for i in range(2**k):
      # convertimos el número a binario y lo rellenamos con ceros
      binary_str = bin(i)[2:].zfill(k)

      # convertimos el número a una palabra
      word = ''.join(symbols[int(char)] for char in binary_str)
      print(word)
      file.write(word+'\n')


def start():
  symbols = ['*', '.']
  # Generamos el k-ésimo nivel aleatorio
  k = np.random.randint(5, 10)
  generateCombinations(k, symbols)
  return k


if __name__ == "__main__":
  # probamos
  inicio = time.time()
  symbols = ['*', '.']
  k = 5
  generateCombinations(k, symbols)
  fin = time.time()
  print(f'Tiempo de ejecución: {fin-inicio} segundos')