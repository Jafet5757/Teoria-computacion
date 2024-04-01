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
  # Vaciando el archivo si k es 1
  if k == 1:
    with open(filename, 'w') as file:
      file.write('')

  # Generando las combinaciones
  with open(filename, 'a') as file:
    file.write(f'combination\n')
    for i in range(2**k):
      # convertimos el número a binario y lo rellenamos con ceros
      binary_str = bin(i)[2:].zfill(k)

      # convertimos el número a una palabra
      word = ''.join(symbols[int(char)] for char in binary_str)
      print(word, end=',\n')
      file.write(word+'\n')


def start(random=True):
  """
    Inicia el programa
  """
  k = 2
  if random:
    # Generamos el k-ésimo nivel aleatorio
    k = np.random.randint(5, 13)
  else:
    k = int(input('Ingrese el nivel k: '))
  symbols = ['*', '.']
  print('{')
  for i in range(1, k+1):
    generateCombinations(i, symbols)
  print('}')
  return k


if __name__ == "__main__":
  # probamos
  inicio = time.time()
  symbols = ['*', '.']
  k = 28
  generateCombinations(k, symbols)
  fin = time.time()
  print(f'Tiempo de ejecución: {fin-inicio} segundos')