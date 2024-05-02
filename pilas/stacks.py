import pygame
import sys

# Implementación de una pila en Python
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    

def detect_simetric_string_zeros_ones(input_string):
    """
    Detecta si una cadena de ceros y unos es simetrica, tiene el mismo numero de ceros y unos
    empezando por ceros (apila) y terminando por unos (desapila)
    """
    s = Stack()
    for i in input_string:
        if i == '0':
            s.push(i)
        else:
            if s.isEmpty():
                return False
            s.pop()
    return s.isEmpty()

# Usamos pygame para animar el proceso

# Define los colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tamaño de la pantalla
WIDTH, HEIGHT = 800, 600

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación de Apilación y Desapilación")

# Fuente para texto
font = pygame.font.Font(None, 36)

def start(input_string):
    """ Inicia la simulación """
    result = detect_simetric_string_zeros_ones(input_string)
    oneTimeRender = False

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not oneTimeRender:
          screen.fill(WHITE)

        text = font.render(f"La cadena {input_string} es simétrica: {result}", True, BLACK)
        screen.blit(text, (50, 100))

        # agregamos un cuadrado rojo cada que detectemos un 0 y lo quitamos cada que detectemos un 1
        x, y = 50, 500
        if not oneTimeRender:
          for i in input_string:
              if i == '0':
                  pygame.draw.rect(screen, RED, (x, y, 50, 50))
                  x += 60
              else:
                  x -= 60
                  pygame.draw.rect(screen, WHITE, (x, y, 50, 50))
              # Esperamos un poco
              pygame.display.flip()
              pygame.time.wait(500)
              oneTimeRender = True

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()


# Probamos
if __name__ == "__main__":
    """ print(detect_simetric_string_zeros_ones('000111')) # True
    print(detect_simetric_string_zeros_ones('0000111')) # False
    print(detect_simetric_string_zeros_ones('0001111')) # False
    print(detect_simetric_string_zeros_ones('0001110')) # False """
    start('00001111') # True
    #start('0000111') # False
    #start('0001111') # False
    #start('0001110') # False