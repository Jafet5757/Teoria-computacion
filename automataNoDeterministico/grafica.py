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