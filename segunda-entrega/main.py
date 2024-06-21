import gramatica_no_ambigua as g
import if_generator as ifs
import stacks as s
import maquina_de_turing as mt
import random
import time

# Preguntamos si el programa se jecutar en modo automático o manual
modo = input("¿Desea ejecutar el programa en modo automático? (s/n): ")
random_mode = False if modo == "n" else True

while True:
  # Mostramos el menu de opciones
  print("Seleccione una opción:")
  print("1. Automata de pila")
  print("2. Backus-Naur condicional IF")
  print("3. Gramatica no ambigua")
  print("4. Máquina de Turing")
  print("5. Salir")

  # Leemos la opción seleccionada
  opcion = int(input("Opción: ")) if not random_mode else random.randint(1, 4)

  # Ejecutamos la opción seleccionada
  if opcion == 1:
      print('Ejecuntando automata de pila...')
      s.run(random_mode)
  elif opcion == 2:
      print('Ejecuntando Backus-Naur condicional IF...')
      ifs.run(random_mode)
  elif opcion == 3:
      print('Ejecuntando gramatica no ambigua...')
      g.run(random_mode)
  elif opcion == 4:
      print('Ejecuntando Máquina de Turing...')
      mt.run(random_mode)
  elif opcion == 5:
      break
  
  time.sleep(1)