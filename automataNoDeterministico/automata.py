import numpy as np

def automata(string, branching = False):
  """ Verifica si termina en 01 la cadena dada """
  matrix = []
  counter = 0
  for c in string:
    if c == '1':
      matrix.append('q0')
    elif c == '0' and not branching:
      matrix.append('q0') # para la primer rama
      # Para la segunda rama lo hacemos recursivamente
      matrix.append(automata(string[counter:], True))
    else: # branching
      matrix.append('q1')
      try:
        if string[1] == '1' and len(string) == 2:
          matrix.append('q2')
        else:
          matrix.append('x')
      except:
        matrix.append('x')
      return matrix
    counter += 1
  return matrix

def formatMatrix(matrix, string):
  """ Formateamos la matriz para darle forma de tabla a cada uno de los automatas """
  formattedMatrix = [[[] for i in range(len(matrix))] for i in range(len(matrix))]
  for i in range(len(matrix)):
    if matrix[i] != 'q0':
      for j in range(len(matrix[i])):
        if formattedMatrix[i-1][j] == []:
          formattedMatrix[i-1][j] = matrix[i]
    else:
      formattedMatrix[i][0] = matrix[i]
  return formattedMatrix


def write_Matrix(filename, positionMatrix):
  with open(filename, 'w') as file:
    for row in positionMatrix:
      for element in row:
        file.write(str(element))
      file.write('\n')

string = '01010111'
matrix = automata(string)
#matrix = formatMatrix(matrix, string)
print(matrix)
write_Matrix('matrix.txt', matrix)