
def automata(string, states = ['q0', 'q1', 'q2']):
  positionMatrix = [[[] for i in range(len(string))] for i in range(len(string))]
  j = 0 # Indica la fila pero tmbién el estado
  i = 0 # Indica la columna y el automata
  lastAtomata = 0 # Indica el último automata que se usó
  for c in string:
    if c == '1':
      positionMatrix[i][j] = states[0]
    elif c == '0':
      # Pueden ser q0 o q1
      # Para q0 se queda en el mismo estado este automata
      positionMatrix[i][j] = states[0]
      # Para q1 cambia de estado y de automata
      positionMatrix[lastAtomata+1][j] = states[1]
      lastAtomata += 1
      # Si el siguiente caracter es 0, se detiene el automata
      if string[j] == '0':
        positionMatrix[lastAtomata][j] = 'x'
      else:
        positionMatrix[lastAtomata][j] = states[2]
    j += 1
  return positionMatrix


def write_Matrix(filename, positionMatrix):
  with open(filename, 'w') as file:
    for row in positionMatrix:
      for element in row:
        file.write(str(element) + ' ')
      file.write('\n')

matrix = automata('010101')
print(matrix)
write_Matrix('matrix.txt', matrix)