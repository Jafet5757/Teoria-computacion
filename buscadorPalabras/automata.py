import pandas as pd

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

  def run(self, input_string):
    current_state = self.intial_state
    register = current_state
    for i, symbol in enumerate(input_string):
      # Verificamos si el simbolo esta en el alfabeto
      if symbol not in self.alphabet:
        # lo ponemos como Sigma
        symbol = 'Sigma'
      current_state = str(self.transitions[symbol][current_state])
      register += '\n' + current_state
      # Si el estado actual es un estado final, lo imprimimos
      if self.final_states.get(current_state):
        print(f'current_state: {current_state}') 
        # señalamos en el registro que es un estado final y agregamos la longitud de la palabra que se ha leido
        register += f'/f{i+1}'
    # escribimos en un documento el registro de estados
    with open('registro_estados.txt', 'w') as file:
      file.write(register)
    
  

if __name__ == "__main__":
  #df = pd.read_csv('tablaDFA.csv', index_col=0)
  #print('palabra e estado 1,5: ', df['e']['1,5'])

  word = 'asddrifle;lsmdriflessdfldknfgkl'
  automata = Automata('tablaDFA.csv')
  automata.run(word)