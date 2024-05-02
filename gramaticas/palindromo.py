import random

#random.seed(30)

class Grammar:
  """ 
    Gramatica que comprueba si una cadena es palindromo 
    tambien genera palindromos con esa gramatica
  """  
  def __init__(self):
    self.grammar = {
      "S": ["", "0", "1", "0S0", "1S1"]
    }
    self.alphabet = ["0", "1"]

  def generate_palindrome(self):
    # seleccionamos una produccion aleatoria
    production = random.choice(self.grammar["S"])
    counter = 0 # contador para evitar bucles infinitos
    while True or counter < 100000000:
      # si hay un simbolo no terminal en la produccion
      if "S" in production:
        aux = random.choice(self.grammar["S"])
        # reemplazamos el simbolo no terminal por una produccion aleatoria
        production = production.replace("S", aux)
      else:
        # si no hay simbolos no terminales en la produccion
        # retornamos la produccion
        return production
    
  def is_palindrome(self, word):
    # si la longitud de la cadena es 0 o 1
    if len(word) <= 1:
      return True
    # si el primer y ultimo caracter son iguales
    if word[0] == word[-1]:
      # llamamos recursivamente a la funcion
      return self.is_palindrome(word[1:-1])
    else:
      return False
    
  def belongs_to_grammar(self, word):
    # iteramos la cadena
    for (i, c) in enumerate(word):
      # si el caracter no pertenece al alfabeto
      if c not in self.alphabet:
        return False
      if c == "0" and word[-(i+1)] != "0":
        return False
      if c == "1" and word[-(i+1)] != "1":
        return False
    return True
      
    
  
# Probamos
g = Grammar()
pali = g.generate_palindrome()
print(pali)
print(g.is_palindrome(pali))
print(g.belongs_to_grammar(pali))