""" 
  Author: Kevin Jafet Moran Orozco
  Start date: 09/03/2024
  Description: Pinta el arbol de soluciones por cada uno de lo jugadores
"""

import tkinter as tk

coordinate_board = [
   [(1,75,74), (2,214,74), (3,353,74), (4,492,74)],
   [(5,75,197), (6,214,197), (7,353,197), (8,492,197)],
   [(9,75,320), (10,214,320), (11,353,320), (12,492,320)],
   [(13,75,443), (14,214,443), (15,353,443), (16,492,443)]
]

def dibujar_linea(canvas, x1, y1, x2, y2, color="red"):
    # Dibujar un cuadrado en el canvas
    canvas.create_line(x1, y1, x2, y2, fill=color)

def get_coordinate(node):
  for row in coordinate_board:
    for col in row:
      if col[0] == node:
        return col[1], col[2]
      
def draw_board(canvas, array_solutions, player):
  x, y = [75, 74] if player == 0 else [492, 74]
  for solution in array_solutions:
    data = solution.data
    # Si el primer caracter es igual al jugador
    if data[0] == str(player):
      # si el primer caracter es 1 el color es rojo, si es 2 el color es verde
      color = "red" if data[0] == "1" else "green"
      # Obtenemos el nodo del tablero
      node = int(data.split("-")[1])
      # Obtenemos las coordenadas del nodo
      x_next, y_next = get_coordinate(node)
      # Dibujamos una linea
      dibujar_linea(canvas, x, y, x_next, y_next, color)
      # Actualizamos las coordenadas
      x, y = x_next, y_next


def show_board(solutions_tree):
  # Crear una ventana
  ventana = tk.Tk()
  ventana.title("Tablero de ajedrez")

  # Cargar la imagen
  imagen_fondo = tk.PhotoImage(file="./img/board.png")

  # Crear un canvas en la ventana con la imagen de fondo
  canvas = tk.Canvas(ventana, width=imagen_fondo.width(), height=imagen_fondo.height())
  canvas.pack()

  # Mostrar la imagen de fondo en el canvas
  canvas.create_image(0, 0, anchor=tk.NW, image=imagen_fondo)

  array_solutions = solutions_tree.children

  draw_board(canvas, array_solutions, 0)
  draw_board(canvas, array_solutions, 1)

  # Iniciar el bucle principal de la aplicación
  ventana.mainloop()
