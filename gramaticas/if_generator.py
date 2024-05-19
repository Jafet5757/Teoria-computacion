import random

class Grammar:

  def __init__(self):
    self.grammar = {
      'S': 'iCSeA',
      'A': ['S', ''],
    }
    self.register = ''\
    
  def count(self, string, char):
    return string.count(char)

  def generate_if(self, size):
    production = self.grammar['S']
    if_counter = 0
    while if_counter < size-1:
      self.register += f'{production}\n'
      # Contamos el numero de S en la cadena
      ss = production.count('S')
      # Contamos el numero de A en la cadena
      aa = production.count('A')
      if 'S' in production:
        production = production.replace('S', '('+self.grammar['S']+')', random.randint(1, ss))
        if_counter += 1
      if 'A' in production: # este no agrega if, por eso no se incrementa el contador
        production = production.replace('A', random.choice(self.grammar['A']), random.randint(1, aa))
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
        code += '<condition> \n'+('\t'*tabs)
      elif c == 'A':
        code += 'A\n'
    code += '\n'
    with open(filename, 'w') as f:
      f.write(code)
    return code

      

if __name__ == '__main__':
  g = Grammar()
  ifs = g.generate_if(10)
  g.write_register()
  print(ifs)
  print(g.ifs_to_code(ifs))