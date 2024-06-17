import pandas as pd
import pygame
import sys

class Tape:
    def __init__(self, string):
        self.tape = list(string)
        self.head = 0

    def read(self):
        return self.tape[self.head]

    def write(self, symbol):
        self.tape[self.head] = symbol

    def move(self, direction):
        if direction == 'R':
            self.head += 1
        elif direction == 'L':
            self.head -= 1
        if self.head == len(self.tape):
            self.tape.append('_')
        elif self.head == -1:
            self.tape.insert(0, '_')
            self.head = 0

    def __str__(self):
        return ''.join(self.tape)

class MaquinaTuring:
    def __init__(self, file_transitions = 'reglas.csv'):
      self.transitions = pd.read_csv(file_transitions, sep=',', header=0, index_col=0, skipinitialspace=True, na_filter=False)
      self.state = 'q0'
      self.head = 0
      self.direction = 'R'
      self.tape = None
      self.register = ''
      self.string = ''
      self.movements_register = []

    def run(self, string):
      """ Por cada caracter leido de la cadena, se realiza una transición en la máquina de Turing """
      self.tape = Tape(string+'B')
      self.string = string+'B'
      while self.state != 'q4':
          symbol = self.tape.read()
          if self.state not in ('q0', 'q1', 'q2', 'q3', 'q4'):
              print(f'{self.state} {symbol}')
              break
          # Si ocurre un error aquí es porque llegó a un estado no definido
          try:
            next_state, write, direction = self.state_to_instructions(self.transitions.loc[(self.state, symbol)])
          except:
            print(f'Fin: Estado no definido {self.state} {symbol} -> - - -')
            self.register += f'Fin: Estado no definido {self.state} {symbol} -> - - -\n'
            self.register += f'tape: {self.tape}\n'
            break
          # Registramos y mostramos la transición
          print(f'{self.state} {symbol} -> ({next_state} {write} {direction})')
          self.register += f'{self.state} {symbol} -> ({next_state} {write} {direction})\n'
          self.register += f'tape: {self.tape}\n'
          self.movements_register.append(f'{write}{direction}')
          print('tape: ',self.tape)
          self.tape.write(write)
          self.tape.move(direction)
          self.state = next_state
      return self.state
          
    def state_to_instructions(self, state):
      """ Devuelve las instrucciones de la máquina de Turing para un estado dado """
      return state.replace(')', '').replace('(', '').replace(' ', '').split(';')
    
    def save_register(self, file_name = 'registro_maquina_turing.txt'):
      """ Guarda el registro de la máquina de Turing en un archivo """
      with open(file_name, 'w') as file:
        file.write(self.register)

    def start_animation(self):
      """ Inicia la animación de la máquina de Turing """    
      # Inicializar Pygame
      pygame.init()

      # Configuración de la ventana
      size = width, height = 1000, 200
      screen = pygame.display.set_mode(size)
      pygame.display.set_caption("Cinta de Máquina de Turing")

      # Colores
      BLACK = (0, 0, 0)
      WHITE = (255, 255, 255)
      RED = (255, 0, 0)

      # Fuente
      font = pygame.font.Font(None, 36)

      # Cinta de la Máquina de Turing
      tape = ['_'] * 16  # Inicialmente, 16 celdas vacías
      cell_width = 60
      cell_height = 60
      tape_start_x = (width - cell_width * len(tape)) // 2 # Centrar la cinta
      tape_start_y = (height - cell_height) // 2 # Centrar la cinta
      current_cell = 0

      # Colocamos la cadena self.string en la cinta
      for i, char in enumerate(self.string):
          tape[i] = char

      # Bucle principal del juego
      running = True
      movement = self.movements_register.pop(0)
      while running:
          #for event in pygame.event.get():
              #if event.type == pygame.QUIT:
                  #running = False # romper el bucle principal
          if len(self.movements_register) > 0:
              # Actualizar la cinta
              if movement[0] == 'X':
                  tape[current_cell] = 'X'
              elif movement[0] == 'Y':
                  tape[current_cell] = 'Y'
              elif movement[0] == 'B':
                  tape[current_cell] = 'B'
              elif movement[0] == '0':
                  tape[current_cell] = str(0)

              # Mover la cabeza de la cinta
              if movement[1] == 'L': # Movimiento a la izquierda
                  current_cell = (current_cell - 1) % len(tape)
              elif movement[1] == 'R': # Movimiento a la derecha
                  current_cell = (current_cell + 1) % len(tape)

          # Cambiamos el movimiento
          if len(self.movements_register) > 0:
            movement = self.movements_register.pop(0)
          else:
            running = False

          # Dibujar en la pantalla
          screen.fill(WHITE)

          # Dibujar las celdas de la cinta
          for i, char in enumerate(tape):
              x = tape_start_x + i * cell_width
              y = tape_start_y
              rect = pygame.Rect(x, y, cell_width, cell_height)
              pygame.draw.rect(screen, RED if i == current_cell else BLACK, rect, 2)
              
              # Dibujar el contenido de la celda
              text = font.render(char, True, BLACK)
              text_rect = text.get_rect(center=rect.center)
              screen.blit(text, text_rect)

          pygame.display.flip()

          # Esperar 0.5 segundos
          pygame.time.wait(500)

          # Salir de Pygame
          """ pygame.quit()
          sys.exit() """

if __name__ == '__main__':
  string = '000111'
  mt = MaquinaTuring()
  mt.run(string)
  mt.save_register()
  # si la cadena es menor a 16 se anima
  if len(string) <= 16:
    mt.start_animation()