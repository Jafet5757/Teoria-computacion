from tree import TreeNode
import chess
import random

def start():
  """ 
    Inicia una partida creando dos jugadoeres que inician en extremos opuestos del tablero
    con el objetivo de llegar a la otra esquina. 
  """
  movements1 = generate_random_movements(8, append="W")
  movements2 = generate_random_movements(8, append="B")
  start1 = [0, 0]
  start2 = [0, 3] # El tablero es de 4x4
  final_node1 = TreeNode(16)
  final_node2 = TreeNode(13)
  # Generamos sus movimientos
  _, root_representation1 = chess.build_board_tree(movements1, start1)
  _, root_representation2 = chess.build_board_tree(movements2, start2)
  # Filtramos las soluciones
  root_solutions1 = chess.cleanSolutions(root_representation1, final_node1)
  root_solutions2 = chess.cleanSolutions(root_representation2, final_node2)
  # Guardamos las soluciones
  root_solutions1.save_tree("solutions1.txt")
  root_solutions1.save_tree_pickle("solutions1.tree")
  root_solutions2.save_tree("solutions2.txt")
  root_solutions2.save_tree_pickle("solutions2.tree")
  # Compiten las soluciones
  final_solution = competition(root_solutions1, root_solutions2, 9)
  final_solution.print_tree()


def generate_random_movements(size=5, append=""):
  """ 
    Genera movimientos aleatorios para el tablero de ajedrez
    Ejemplo: BWBBWBWWWBW
    Args:
      size (int): Tamaño del string
      append (str): Caracter a añadir al final del string
  """
  movements = ""
  for _ in range(size):
    movements += random.choice(["B", "W"])
  return movements + append

def competition(root1, root2, turns = 6):
  """ 
    Compite dos jugadores para llegar a la otra esquina del tablero
    Args:
      root1 (TreeNode): Nodo raíz del jugador 1
      root2 (TreeNode): Nodo raíz del jugador 2
      turns (int): Número de turnos
  """
  final_solution = TreeNode('solution')
  for i in range(turns*2):
    if i % 2 == 0:
      # Turno del jugador 1, seleccionamos un movimiento aleatorio de las soluciones
      root1	 = random.choice(root1.children)
      final_solution.add_child(TreeNode(str(i%2)+'-'+str(root1.data)))
    else:
      # Turno del jugador 2, seleccionamos un movimiento aleatorio de las soluciones
      root2 = random.choice(root2.children)
      final_solution.add_child(TreeNode(str(i%2)+'-'+str(root2.data)))
  return final_solution

if __name__ == "__main__":
  start()