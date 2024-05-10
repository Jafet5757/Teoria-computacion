import random

class Grammar:

  def __init__(self):
    self.grammar = {
      'S': 'iCSeA',
      'A': ['S', ''],
    }
    self.register = ''

  def generate_if(self, size):
    production = self.grammar['S']
    if_counter = 0
    while if_counter < size-1:
      self.register += f'{production}\n'
      if 'S' in production:
        production = production.replace('S', '('+self.grammar['S']+')')
        if_counter += 1
      if 'A' in production: # este no agrega if, por eso no se incrementa el contador
        production = production.replace('A', random.choice(self.grammar['A']), 1)
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
        code += '} else { \n' + ('\t'*tabs)
      elif c == 'S':
        tabs -= 2
        code += '<statement> \n' + ('\t'*tabs)
      elif c == 'C':
        code += '<condition> {\n'+('\t'*tabs)
        tabs += 2
      elif c == 'A':
        code += '}'
    with open(filename, 'w') as f:
      f.write(code)
    return code

      

if __name__ == '__main__':
  g = Grammar()
  ifs = g.generate_if(5)
  #g.write_register()
  print(ifs)
  print(g.ifs_to_code(ifs))