""" 
  Author: Kevin Jafet Moran Orozco
  Start date: 09/03/2024
  Description: Pinta el arbol de soluciones por cada uno de lo jugadores
"""

import tkinter as tk
from PIL import Image, ImageTk

# Coordenadas de las casillas del tablero junto con el nodo al que pertenecen
coordinate_board = [
   [(1,75,74), (2,214,74), (3,353,74), (4,492,74)],
   [(5,75,197), (6,214,197), (7,353,197), (8,492,197)],
   [(9,75,320), (10,214,320), (11,353,320), (12,492,320)],
   [(13,75,443), (14,214,443), (15,353,443), (16,492,443)]
]

class AnimatedApp:
    def __init__(self, ventana, canvas, image, coordinates):
        # Agregamos el canvas
        self.canvas = canvas
        self.ventana = ventana

        # Agregamos las coordenadas
        self.coordinates = coordinates

        # Carga de imagen
        self.image = Image.open(image)
        #self.image = self.image.resize((50, 50), Image.ANTIALIAS)
        self.ball_image = ImageTk.PhotoImage(self.image)

        # Posición inicial en la lista de coordenadas
        self.position = 0

        # Coordenadas iniciales y finales
        self.start_x = coordinates[self.position][0]
        self.start_y = coordinates[self.position][1]
        self.end_x = coordinates[self.position+1][0]
        self.end_y = coordinates[self.position+1][1]

        # Crear la imagen en el canvas
        self.ball = self.canvas.create_image(self.start_x, self.start_y, image=self.ball_image, anchor="nw")

        # Calcular el incremento para el movimiento
        self.delta_x = (self.end_x - self.start_x) / 100
        self.delta_y = (self.end_y - self.start_y) / 100

        # Iniciar la animación
        self.animate()

    def animate(self):
        # Mover la imagen
        self.start_x += self.delta_x
        self.start_y += self.delta_y
        self.canvas.coords(self.ball, self.start_x, self.start_y)
        
        # Si la bola llega a su destino, detener la animación
        if abs(self.start_x - self.end_x) < 1 and abs(self.start_y - self.end_y) < 1:
          # Pasar a la siguiente coordenada
          self.position += 1
          if self.position < len(self.coordinates) - 1:
            self.start_x = self.coordinates[self.position][0]
            self.start_y = self.coordinates[self.position][1]
            self.end_x = self.coordinates[self.position+1][0]
            self.end_y = self.coordinates[self.position+1][1]
            self.delta_x = (self.end_x - self.start_x) / 100
            self.delta_y = (self.end_y - self.start_y) / 100
          else:
            return


        # Llamar recursivamente a la función después de un breve tiempo para crear la animación
        self.ventana.after(10, self.animate)

def array_solutions_to_coordinates(array_solutions, player, add_start_node=True):
  """ 
    Convierte las soluciones (arbol) de un array a las coordenadas del tablero (tambien un array)
    Args:
      array_solutions (list): Lista de soluciones 
      player (int): Jugador (0, 1)
  """
  coordinates = []
  # Agregamos el nodo inicial
  if add_start_node:
    coordinates.append((75, 74) if player == 0 else (492, 74))
  for solution in array_solutions:
    data = solution.data
    if data[0] == str(player):
      coordinates.append(get_coordinate(int(data.split("-")[1])))
  return coordinates

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
      color = "red" if data[0] == "0" else "green"
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

  # Iniciar la animación
  array_solutions_player0 = array_solutions_to_coordinates(array_solutions, 0)
  array_solutions_player1 = array_solutions_to_coordinates(array_solutions, 1)

  AnimatedApp(ventana, canvas, "./img/player1.png", array_solutions_player0)
  AnimatedApp(ventana, canvas, "./img/player2.png", array_solutions_player1)

  # Iniciar el bucle principal de la aplicación
  ventana.mainloop()
