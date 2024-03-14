import tkinter as tk
from PIL import Image, ImageTk

class AnimatedApp:
    def __init__(self, ventana, canvas, image, coordinates):
        # Agregamos el canvas
        self.canvas = canvas
        self.ventana = ventana

        # Agregamos las coordenadas
        self.coordinates = coordinates

        # Carga de imagen
        self.image = Image.open(image)
        self.image = self.image.resize((50, 50), Image.ANTIALIAS)
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

def main():
    root = tk.Tk()
    # Crear un canvas en la ventana con la imagen de fondo
    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()
    coordinates = [(50,50), (300, 50), (300, 300), (50, 300)]
    image = ".\img\player2.png"
    app1 = AnimatedApp(root, canvas, image, coordinates)  # Coordenadas iniciales: (50, 50), Coordenadas finales: (300, 300)
    root.mainloop()

if __name__ == "__main__":
    main()
