import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class Automata:
  def __init__(self, transitions_current_name):
    self.transitions = pd.read_csv(transitions_current_name, index_col=0)
    self.intial_state = '1'
    # e,s,c,u,l,a,t,d,i,n,r,o,f,m,z
    self.alphabet = ('e','s','c','u','l','a','t','d','i','n','r','o','f','m','z')
    self.final_states = {
      '1,8': 'escuela',
      '1,3,28': 'estudiantes',
      '1,3,27': 'rifles', 
      '1,34': 'crimen',
      '1,17,22': 'rencor',
      '1,41': 'matanza'
    }
    self.register_filename = 'registro_estados.txt'

  def run(self, input_string):
    """ 
      Corre el automata con la palabra dada, usa la tabla de transiciones para moverse entre estados segun la palabra
      args:
        input_string: str - palabra a analizar 
    """
    current_state = self.intial_state
    register = current_state
    final_state_counter = 0
    for i, symbol in enumerate(input_string):
      # Verificamos si el simbolo esta en el alfabeto
      if symbol not in self.alphabet:
        # lo ponemos como Sigma
        symbol = 'Sigma'
      current_state = str(self.transitions[symbol][current_state])
      register += '\n' + current_state
      # Si el estado actual es un estado final, lo imprimimos
      if self.final_states.get(current_state):
        print(f'current_state: {current_state}/f{i+1}-{self.final_states[current_state]}') 
        # señalamos en el registro que es un estado final y agregamos la longitud de la palabra que se ha leido
        register += f'/f{i+1}'
        final_state_counter += 1
    # escribimos en un documento el registro de estados
    with open(self.register_filename, 'w') as file:
      file.write(register)
    print(f'final_state_counter: {final_state_counter}')

  def draw(self):
    """ 
      Dibuja el automata en una ventana emergente
    """
    G = nx.DiGraph()
    for i in self.transitions.columns:
      for j in self.transitions.index:
        G.add_edge(j, str(self.transitions[i][j]), label=i)
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="mediumpurple", font_size=10, font_color="black", font_weight="bold", width=2, edge_color="gray")
    edge_labels = dict([((u, v,), d['label']) for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=10)
    plt.title('Autómata')
    plt.show()

  def draw_register(self):
    """ 
      Dibuja el registro de estados en una ventana emergente
    """
    with open(self.register_filename, 'r') as file:
      register = file.read()
    G = nx.DiGraph()
    register = register.split('\n')
    for i in range(len(register)-1):
      G.add_edge(register[i], register[i+1])
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="c", font_size=10, font_color="black", font_weight="bold", width=2, edge_color="gray")
    plt.title('Registro de estados')
    plt.show()

  def __str__(self):
    return str(self.transitions)
    
  

if __name__ == "__main__":
  #df = pd.read_csv('tablaDFA.csv', index_col=0)
  #print('palabra e estado 1,5: ', df['e']['1,5'])

  word = 'asddrifle;lsmdriflessdfldknfgkl'
  automata = Automata('tablaDFA.csv')
  automata.run(word)
  automata.draw()
  automata.draw_register()