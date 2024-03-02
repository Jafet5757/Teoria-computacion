import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos
G.add_node(1)
G.add_nodes_from([2, 3, 4, 5])

# Agregar aristas
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4), (3, 4), (4, 5), (5, 1), (1, "q0")])

# Dibujar el grafo
pos = nx.circular_layout(G) # Puedes probar otros layouts como 'random', 'circular', 'shell', 'spring', etc.
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=20)

# Mostrar el gráfico
plt.show()
