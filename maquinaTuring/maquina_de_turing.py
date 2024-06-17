import pandas as pd
import pygame

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

    def run(self, string):
      """ Por cada caracter leido de la cadena, se realiza una transición en la máquina de Turing """
      self.tape = Tape(string+'B')
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
          print(f'{self.state} {symbol} -> ({next_state} {write} {direction})')
          self.register += f'{self.state} {symbol} -> ({next_state} {write} {direction})\n'
          self.register += f'tape: {self.tape}\n'
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
      pygame.init()
      pygame.display.set_caption('Máquina de Turing')
      screen = pygame.display.set_mode((800, 600))
      screen.fill((255, 255, 255))
      pygame.display.flip()
      running = True
      while running:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  running = False
      pygame.quit()

if __name__ == '__main__':
  mt = MaquinaTuring()
  mt.run('000111')
  mt.save_register()
  mt.start_animation()