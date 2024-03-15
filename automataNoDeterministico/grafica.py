import networkx as nx
import matplotlib.pyplot as plt

def show():
  # Crear un grafo dirigido
  G = nx.DiGraph()

  # Agregamos los nodos
  G.add_nodes_from(['q0', 'q1', 'q2'])

  # Agregamos las aristas
  G.add_edges_from([('q0', 'q1'), ('q1', 'q2'), ('q0', 'q0')])


  # Dibujamos el grafo
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=20)

  # Mostramos el gráfico
  plt.show()

def show_register(matrix):
  """ Muestra el registro de la matriz 
  Args:
    matrix (list): Matriz con los estados del autómata (['q0', ['q1', 'x'], 'q0', ['q1', 'x'], 'q0', 'q0', 'q0', 'q0', 'q0', 'q0', 'q0', 'q0', ['q1', 'x']])
  """
  # Creamos un grafo dirigido`
  G = nx.Graph()

  # Agregamos los nodos
  G.add_nodes_from(['q0', 'q1', 'q2'])

  # Recorremos la matriz para extraer las aristas
  edges = []
  for i in range(len(matrix)):
    if matrix[i] != 'q0':
      if type(matrix[i]) == list:
        for j in range(0, len(matrix[i]), 2):
          if matrix[i][j] != 'x' and i < len(matrix)-1:
            edges.append((matrix[i][j], matrix[i][j+1]))
      else:
        edges.append((matrix[i], matrix[i+1] if type(matrix[i+1]) != list else matrix[i+1][0]))
    else:
      if i < len(matrix)-1:
        edges.append((matrix[i], matrix[i+1] if type(matrix[i+1]) != list else matrix[i+1][0]))

  print(edges)
    
  
  # Agregamos las aristas
  G.add_edges_from(edges)

  # Dibujamos el grafo
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=20)

  # Mostramos el gráfico
  plt.show()