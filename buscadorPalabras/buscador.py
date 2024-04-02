import sys

sys.path.append('/buscadorPalabras/')

from buscadorPalabras.automata import Automata
import buscadorPalabras.get_noticia as getter

def start(random = False):
  words = ''
  if random:
    words = getter.get_noticia()
  else:
    opc = input('\n1. Introducir la url de la noticia \n2. Seleccionar el archivo de texto test_text.txt \n3. Ingresar palabra \nSeleccione una opción:')
    if opc == '1':
      url = input('Introduzca la url de la noticia: ')
      words = getter.get_noticia(url)
    elif opc == '3':
      words = input('Introduzca la palabra: ')
    else:
      with open('test_text.txt', 'r', encoding='utf-8') as file:
        words = file.read()
  buscador = Automata('tablaDFA.csv')
  buscador.run(words)
  print('Se ha creado el archivo registro_estados.txt')
  opc = input('\nDesea visualizar el autómata? (S/n): ')
  if opc == 's' or opc == 'S':
    buscador.draw()
    buscador.draw_register()


if __name__ == "__main__":
  start(True)