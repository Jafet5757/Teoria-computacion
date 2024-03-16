""" 
  Autor: Kevin Jafet Moran Orozco
  Fecha de inicio: 09/03/2024
  Descripcion: Simulador tipo ajedrez en que se busca llegar a la otra esquina del tablero creando todo el árbol de posibilidades,
  si un jugador es tapado en u paso puede hacer un rebase y un segundo movimiento (ventaja) con el que puede usar una casilla ocupada
"""

from cheesSimulator.tree import TreeNode
import cheesSimulator.grapher as grapher
import cheesSimulator.chess as chess
import random

#semilla = 4002
#random.seed(semilla)

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
  grapher.show_board(final_solution)


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
    # i alguno ya no tiene hijos, termina el juego
    if not root1.children or not root2.children:
      break
    # Turno actual y siguiente
    turn_actual = i % 2
    turn_next = (i + 1) % 2
    if i % 2 == 0:
      # Turno del jugador 1, seleccionamos un movimiento aleatorio de las soluciones
      root1_child = random.choice(root1.children)
      movement_data = f"{turn_actual}-{root1_child.data}"
      contrincant_data = f"{turn_next}-{root1_child.data}"

      movement = TreeNode(movement_data)
      contrincant = TreeNode(contrincant_data)

      # Verificamos si hay colisiones con el contrincante
      if collisions(final_solution, contrincant):
        print("colision")
        # Si hay colisiones, el jugador 1 busca rebasar al jugador 2
        new_node = toPass(final_solution, root1, i)
        root1 = new_node if new_node else root1
      else:
        final_solution.add_child(movement)
        root1 = root1_child
    else:
      # Turno del jugador 2, seleccionamos un movimiento aleatorio de las soluciones
      root2_child = random.choice(root2.children)
      movement_data = f"{turn_actual}-{root2_child.data}"
      contrincant_data = f"{turn_next}-{root2_child.data}"

      movement = TreeNode(movement_data)
      contrincant = TreeNode(contrincant_data)

      # Verificamos si hay colisiones con el contrincante
      if collisions(final_solution, contrincant):
        print("colision")
        # Si hay colisiones, el jugador 2 busca rebasar al jugador 1
        new_node = toPass(final_solution, root2, i)
        root2 = new_node if new_node else root2
      else:
        final_solution.add_child(movement)
        root2 = root2_child
  return final_solution

def collisions(final_solution, movement):
  """ 
    Verifica si hay colisiones entre los movimientos de los jugadores
    Args:
      final_solution (TreeNode): Nodo raíz de la solución final
      movement (TreeNode): Nodo del movimiento
  """
  for child in final_solution.children:
    if child.data == movement.data:
      return True
  return False

def toPass(final_solution, root_player, turn):
  """ 
    Hace un rebase buscando un movivimento posible y avanzando dos casillas
    Args:
      final_solution (TreeNode): Nodo raíz de la solución final
      root_player (TreeNode): Nodo raíz del jugador
      turn (int): Turno actual (0, 1)
    Returns:
      str: Movimiento posible
  """
  turn_actual = turn%2
  turn_next = (turn+1)%2
  childrens = root_player.children
  # Entre lo hijos (siguientes movimientos) buscamos uno que no esté en la solución final
  for child in childrens:
    contrincant_next_move = TreeNode(str(turn_next)+'-'+str(child.data))
    if not collisions(final_solution, contrincant_next_move):
      # Si no hay colisiones, avanzamos dos casillas
      final_solution.add_child(TreeNode(str(turn_actual)+'-'+str(child.data))) # Nodo del movimiento
      final_solution.add_child(TreeNode(str(turn_actual)+'-'+str(child.children[0].data))) # Nodo del siguiente movimiento
      return child.children[0]
  # si siempre colisiona, haz un pass
  return None

if __name__ == "__main__":
  start()