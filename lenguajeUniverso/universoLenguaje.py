""" 
  Genera un universo de lenguaje hasta el k-ésimo nivel
  las palabras binarias (*,.) hasta la longitud k
  k es la cantidad de simbolos que tiene la palabra
"""
import time


def generateCombinations(k, symbols, filename='combinations.csv'):
  """
    Genera todas las combinaciones de los simbolos para un alfabeto binario
  """
  # Vaciando el archivo
  with open(filename, 'w') as file:
    file.write('')

  # Generando las combinaciones
  with open(filename, 'a') as file:
    file.write('Strings\n')
    for i in range(2**k):
      # convertimos el número a binario y lo rellenamos con ceros
      binary_str = bin(i)[2:].zfill(k)

      # convertimos el número a una palabra
      word = ''.join(symbols[int(char)] for char in binary_str)
      #print(word)
      file.write(word+'\n')

# probamos
inicio = time.time()
symbols = ['*', '.']
k = 5
generateCombinations(k, symbols)
fin = time.time()
print(f'Tiempo de ejecución: {fin-inicio} segundos')