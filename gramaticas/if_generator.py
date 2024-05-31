import random

#random.seed(10)

class Grammar:

  def __init__(self):
    self.grammar = {
      'S': 'iCtSA',
      'A': ['eS', ''],
    }
    self.register = ''\
    
  def count(self, string, char):
    return string.count(char)

  def generate_if(self, size):
    production = self.grammar['S']
    if_counter = 0
    while if_counter < size-1:
      self.register += f'{production}\n'
      if 'S' in production:
        production = self.change_character_in_index(production, 'S', self.grammar['S'])
        if_counter += 1

      if 'A' in production: # este no agrega if, por eso no se incrementa el contador
        production = self.change_character_in_index(production, 'A', random.choice(self.grammar['A']))
    self.register += f'{production}\n'
    return production
  
  def write_register(self, filename='output_ifs.txt'):
    with open(filename, 'w') as f:
      f.write(self.register)

  def ifs_to_code(self, ifs, filename='output_ifs_code.txt'):
    tabs = 1
    code = ''
    for c in ifs:
      if c == 'i':
        code += 'if '
      elif c == 'e':
        tabs -= 2
        code += ' else  \n' + ('\t'*tabs)
      elif c == 'S':
        tabs -= 2
        code += '<statement> \n' + ('\t'*tabs)
      elif c == 'C':
        tabs += 2
        code += '<condition> '
      elif c == 't':
        code += 'then \n'+('\t'*tabs)
      elif c == 'A':
        code += 'end\n'
    code += '\n'
    with open(filename, 'w') as f:
      f.write(code)
    return code

  def change_character_in_index(self, string, char, new_char):
    # calculamos la cantidad de veces que aparece el caracter en la cadena
    indices = []
    for i, c in enumerate(string):
        if c == char:
            indices.append(i)
    # seleccionamos un indice aleatorio
    index = random.choice(indices)
    # cambiamos el caracter en el indice seleccionado
    return string[:index] + ('('+new_char+')' if new_char != '' else '') + (string[index + 1:] if index + 1 < len(string) else '')
      

if __name__ == '__main__':
  g = Grammar()
  ifs = g.generate_if(1000)
  g.write_register()
  print(ifs)
  print(g.ifs_to_code(ifs))