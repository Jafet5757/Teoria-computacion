from automata import Automata
import get_noticia as getter

def main(random = False):
  words = ''
  if not random:
    words = getter.get_noticia()
  else:
    opc = input('1. Introducir la url de la noticia \n2. Seleccionar el archivo de texto test_text.txt \nSeleccione una opción:')
    if opc == '1':
      url = input('Introduzca la url de la noticia: ')
      words = getter.get_noticia(url)
    else:
      with open('test_text.txt', 'r', encoding='utf-8') as file:
        words = file.read()
  buscador = Automata('tablaDFA.csv')
  buscador.run(words)
  print('Se ha creado el archivo registro_estados.txt')
  opc = input('\nDesea visualizar el autómata? (S/n): ')
  if opc == 's' or opc == 'S':
    buscador.draw()


if __name__ == "__main__":
  main(True)