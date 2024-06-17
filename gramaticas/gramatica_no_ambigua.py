import random

#random.seed(13)

class Grammar:
  """ Clase que genera y verifica cadenas balanceadas de paréntesis. """
  def __init__(self):
    self.grammar = {
      'B': ['(RB', ''],
      'R': [')', '(RR'],
    }
    self.register = ''

  def generate_string_balanced(self, size):
    """ Genera una cadena balanceada de paréntesis. """
    self.register = ''
    production = self.grammar['B'][0]
    for i in range(size):
      self.register += f'{production}\n'
      production = self.change_character_in_index(production, 'B', self.grammar['B'][0] if i < size - 1 else self.grammar['B'][1])
      production = self.change_character_in_index(production, 'R', self.grammar['R'][1] if i < size - 1 else self.grammar['R'][0])
    # Al final reemplaza todas las B por '' y todas las R por ')'
    production = production.replace('B', '').replace('R', ')')
    self.register += f'{production}\n'
    return production

  def change_character_in_index(self, string, char, new_char, index = None):
    # calculamos la cantidad de veces que aparece el caracter en la cadena
    indices = []
    for i, c in enumerate(string):
        if c == char:
            indices.append(i)
    if len(indices) == 0:
        return string
    # seleccionamos un indice aleatorio
    index = random.choice(indices) if index is None else indices[index]
    # cambiamos el caracter en el indice seleccionado
    return string[:index] + (new_char if new_char != '' else '') + (string[index + 1:] if index + 1 < len(string) else '')
  
  def expand_string_balanced(self, string):
    """ Verifica si una cadena de paréntesis está balanceada usando la gramatica. 
      Rules:
        -si expandimos B y el siguientes simbolo es '(' entonces usamos la regla (RB y '' si no hay más.

        -si expandimos R y el siguiente simbolo es ')' entonces usamos la regla ) y (RR si es '('.
    """
    production = 'B'
    self.register = production + '\n'
    string_len = len(string)
    for (i, c) in enumerate(string):
      if i == string_len - 1 and self.get_first_variable_in_string(production, 'BR') == 'B':
        # si llegamos al final de la cadena reemplazamos la primera B por ''
        production = self.change_character_in_index(production, 'B', self.grammar['B'][1], 0)
        # agregamos la regla a registro
        self.register += 'B -> ε; '
      elif c == '(' and self.get_first_variable_in_string(production, 'BR') == 'B':
        # reemplazamos el primer B por (RB
        production = self.change_character_in_index(production, 'B', self.grammar['B'][0], 0)
        # agregamos la regla a registro
        self.register += 'B -> (RB; '
      elif c == ')' and self.get_first_variable_in_string(production, 'BR') == 'R':
        # reemplazamos el primer R por )
        production = self.change_character_in_index(production, 'R', self.grammar['R'][0], 0)
        # agregamos la regla a registro
        self.register += 'R -> ); '
      elif c == '(' and self.get_first_variable_in_string(production, 'BR') == 'R':
        # reemplazamos el primer R por (RR
        production = self.change_character_in_index(production, 'R', self.grammar['R'][1], 0)
        # agregamos la regla a registro
        self.register += 'R -> (RR; '
      self.register += production + '\n'
      # quitamos la ultima B si es necesario
      if i == string_len - 1:
        production = production.replace('B', '')
        self.register += production + '\n'
    return self.verify_string_balanced(production), self.register
  
  def verify_string_balanced(self, string):
    """ Verifica si una cadena de paréntesis está balanceada. """
    stack = []
    for c in string:
      if c == '(':
        stack.append(c)
      elif c == ')':
        if len(stack) == 0:
          return False
        stack.pop()
    return len(stack) == 0
    
  def get_first_variable_in_string(self, string, variables):
    """ Retorna la primera variable en la cadena. """
    for c in string:
      if c in variables:
        return c
    return None
  
  def save_register(self, filename = 'registro_gramatica_no_ambigua.txt'):
    with open(filename, 'w') as f:
      f.write(self.register)
    

if __name__ == '__main__':
  g = Grammar()
  balanced = g.generate_string_balanced(252)
  is_balanced, register = g.expand_string_balanced(balanced)
  print(register)
  print(f'La cadena {balanced} {len(balanced)} está balanceada: {is_balanced}')
  g.save_register()