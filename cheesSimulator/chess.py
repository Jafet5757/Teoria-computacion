from tree import TreeNode

# Tablero
board = [
  ['W', 'B', 'W', 'B'],
  ['B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B'],
  ['B', 'W', 'B', 'W']
]

board_representation = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]

movements = "BWBWBW"

def build_board_tree(movements, board, start = [0, 0]):
  row, col = start
  root = TreeNode(board[row][col])
  root_representation = TreeNode(board_representation[row][col])

  if not movements:
    return root, root_representation

  # Obtenemos las posiciones posibles
  poitions = next_positions(board, movements[0], col, row)
  # Por cada posición posible invocamos la función recursivamente
  for p in poitions:
    row, col = p
    root.add_child(TreeNode(board[row][col]))
    root_representation.add_child(TreeNode(board_representation[row][col]))
    child = build_board_tree(movements[1:], board, [row, col])
    root.add_child(child[0])
    root_representation.add_child(child[1])

  return root, root_representation

def next_positions(board, char, col, row):
  """ Nos movemos a la derecha, abajo, izquierda, arriba o diagonal si es un movimiento válido
      y el caracter es igual al que estamos buscando 
      Args:
        board (list): Tablero
        char (str): Caracter a buscar
        col (int): Columna actual
        row (int): Fila actual
      Returns:
        list: Lista con las posiciones posibles
  """
  poitions = []
  # Derecha
  if col + 1 < len(board[0]) and char == board[row][col + 1]:
    poitions.append([row, col + 1])
  # Abajo
  if row + 1 < len(board) and char == board[row + 1][col]:
    poitions.append([row + 1, col])
  # Izquierda
  if col - 1 >= 0 and char == board[row][col - 1]:
    poitions.append([row, col - 1])
  # Arriba
  if row - 1 >= 0 and char == board[row - 1][col]:
    poitions.append([row - 1, col])
  # Diagonal superior derecha
  if row + 1 < len(board) and col + 1 < len(board[0]) and char == board[row + 1][col + 1]:
    poitions.append([row + 1, col + 1])
  # Diagonal inferior izquierda
  if row - 1 >= 0 and col - 1 >= 0 and char == board[row - 1][col - 1]:
    poitions.append([row - 1, col - 1])
  # Diagonal inferior derecha
  if row + 1 < len(board) and col - 1 >= 0 and char == board[row + 1][col - 1]:
    poitions.append([row + 1, col - 1])
  # Diagonal superior izquierda
  if row - 1 >= 0 and col + 1 < len(board[0]) and char == board[row - 1][col + 1]:
    poitions.append([row - 1, col + 1])
  return poitions

root, root_representation = build_board_tree(movements, board)
root.print_tree()
print()
root_representation.print_tree()
root_representation.save_tree("board_representation.txt")