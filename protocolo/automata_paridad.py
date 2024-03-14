class ParityDetector:
  def __init__(self):
    self.states = ('q0', 'q1', 'q2', 'q3',)
    self.alphabet = ('0', '1',)
    self.transitions = {
      'q0': {'0': 'q2', '1': 'q1'},
      'q1': {'0': 'q3', '1': 'q0'},
      'q2': {'0': 'q0', '1': 'q3'},
      'q3': {'0': 'q1', '1': 'q2'}
    }
    self.initial_state = 'q0'
    self.final_states = ('q0',)

  def run(self, input_string):
    """ 
      Ejecuta el autómata sobre la cadena de entrada.
      Args:
        input_string (str): La cadena de entrada.
      Returns:
        bool: True si la cadena es aceptada, False en caso contrario.
        str: El registro de estados por los que pasó el autómata. 
    """
    current_state = self.initial_state
    register = current_state
    for symbol in input_string:
      current_state = self.transitions[current_state][symbol]
      register += '-' + current_state
    return (current_state==self.initial_state),register
  
  def generate_string(self, length):
    """ 
      Genera una cadena de longitud dada.
      Args:
        length (int): La longitud de la cadena a generar.
      Returns:
        str: La cadena generada.
    """
    import random
    return ''.join(random.choice(self.alphabet) for _ in range(length))
  
  def start_random(self):
    """ 
      Ejecuta el autómata sobre una cadena aleatoria.
      Returns:
        bool: True si la cadena es aceptada, False en caso contrario.
        str: La cadena generada.
        str: El registro de estados por los que pasó el autómata. 
    """
    string = self.generate_string(10)
    result,register = self.run(string)
    # Pintamos los resultados
    print(f'La cadena {string} es {"aceptada" if result else "rechazada"}')
    print(f'Registro de estados: {register}')
    return result,string,register
  

if __name__ == "__main__":
  automata = ParityDetector()
  input_string = '1001'
  result,register = automata.run(input_string)
  print(f'La cadena {input_string} es {"aceptada" if result else "rechazada"}')
  print(f'Registro de estados: {register}')