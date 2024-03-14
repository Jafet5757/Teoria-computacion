import sys
sys.path.append('/automataNoDeterministico/')
sys.path.append('/lenguajeUniverso/')
sys.path.append('/protocolo/')

import automataNoDeterministico.automata as at
import automataNoDeterministico.grafica as grat
import lenguajeUniverso.universoLenguaje as ul
import lenguajeUniverso.graficador as grul
import protocolo.automata_paridad as ap

# Limpia la consola
def clear():
  print('\n'*100)
clear()

# Pintamos las opciones
while(True):
  print('\n\n1. Universo de lenguaje')
  print('2. Autómata no determinístico')
  print('3. Autómata de paridad')
  print('0. Salir')
  opcion = input('Ingrese la opción: ')
  print('\n')

  if opcion == '1':
    k = ul.start()
    print(f'Nivel k: {k}')
    opcion = input('Desea graficar las combinaciones? (s/n): ')
    if opcion == 's':
      grul.show()
  elif opcion == '2':
    matrix, string = at.start()
    print(matrix)
    print('Cadena generada',string)
    opcion = input('Desea graficar el automata? (s/n): ')
    if opcion == 's':
      grat.show()
  elif opcion == '3':
    automata = ap.ParityDetector()
    automata.start_random()
  elif opcion == '0':
    break