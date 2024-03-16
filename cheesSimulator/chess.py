""" 
  Autor: Kevin Jafet Moran Orozco
  Fecha de inicio: 08/03/2024
  Descripcion: Simulador tipo ajedrez en que se busca llegar a la otra esquina del tablero creando todo el árbol de posibilidades
"""

from cheesSimulator.tree import TreeNode

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

def build_board_tree(movements, start = [0, 0]):
  row, col = start
  root = TreeNode(board[row][col])
  root_representation = TreeNode(board_representation[row][col])

  if not movements:
    return root, root_representation

  # Obtenemos las posiciones posibles
  poitions = next_positions(movements[0], col, row)
  # Por cada posición posible invocamos la función recursivamente
  for p in poitions:
    row, col = p
    child = build_board_tree(movements[1:], [row, col])
    root.add_child(child[0])
    root_representation.add_child(child[1])

  return root, root_representation

def next_positions(char, col, row):
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

def cleanSolutions(root, final_node):
  """ Limpia el arbol en busca de las soluciones que contengan al nodo final
      Args:
        root (TreeNode): Nodo raíz
        final_node (TreeNode): Nodo final, el que debe contener la solución
  """
  root_solutions = TreeNode(root.data)
  # Iteramos cada rama del arbol buscando el nodo final
  for child in root.children:
    if find_node(child, final_node):
      solution = cleanSolutions(child, final_node)
      root_solutions.add_child(solution)
  return root_solutions

def find_node(root, node):
  """ Busca el nodo en el arbol
      Args:
        root (TreeNode): Nodo raíz
        node (TreeNode): Nodo a buscar
      Returns:
        bool: True si lo encuentra, False en caso contrario
  """
  if root.data == node.data and root.children == []:
    return True
  for child in root.children:
    if find_node(child, node):
      return True
  return False

# --------Creamos el arbol y probamos---------
""" movements = "BWBWBW"
root, root_representation = build_board_tree(movements)
root.print_tree()
print()
root_representation.print_tree()
root_representation.save_tree("board_representation.txt")
print()
root_solutions = cleanSolutions(root_representation, TreeNode(16))
root_solutions.print_tree()
root_solutions.save_tree("board_representation_solutions.txt")
root_solutions.save_tree_pickle("board_representation_solutions.pkl") """