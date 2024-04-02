import sys
sys.path.append('/automataNoDeterministico/')
sys.path.append('/lenguajeUniverso/')
sys.path.append('/protocolo/')
sys.path.append('/cheesSimulator/')
sys.path.append('/buscadorPalabras/')

import automataNoDeterministico.automata as at
import automataNoDeterministico.grafica as grat
import lenguajeUniverso.universoLenguaje as ul
import lenguajeUniverso.graficador as grul
import protocolo.automata_paridad as ap
from cheesSimulator import play as chees
from buscadorPalabras import buscador as bp

# Limpia la consola
def clear():
  print('\n'*100)
clear()

mode_random = True

# Pregunta si se desea ejecutar en modo random
opcion = input('Desea desactivar el modo random? (s/n): ')
if opcion == 's':
  mode_random = False

# Pintamos las opciones
while(True):
  print('\n\n1. Universo de lenguaje')
  print('2. Autómata no determinístico')
  print('3. Autómata de paridad')
  print('4. Juego tipo ajedrez')
  print('5. Buscador de palabras')
  print(f'r. Cambiar modo (random = {mode_random})')
  print('0. Salir')
  opcion = input('Ingrese la opción: ')
  print('\n')

  if opcion == '1':
    k = ul.start(random=mode_random)
    print(f'Nivel k: {k}')
    opcion = input('Desea graficar las combinaciones? (s/n): ')
    if opcion == 's':
      grul.show()
  elif opcion == '2':
    matrix, string = at.start(random=mode_random)
    print(matrix)
    print('Cadena generada',string)
    opcion = input('Desea graficar el automata? (s/n): ')
    if opcion == 's':
      grat.show_register(matrix)
  elif opcion == '3':
    automata = ap.ParityDetector()
    automata.start_random(random = mode_random)
  elif opcion == '4':
    chees.start(random = mode_random)
  elif opcion == '5':
    bp.start(random = mode_random)
  elif opcion == 'r':
    mode_random = not mode_random
  elif opcion == '0':
    break