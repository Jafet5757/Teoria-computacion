from manim import *

class ChangeGraphLayout(Scene):
    def construct(self):
        vertices = ['q0', 'q1', 'q2']
        edges = [('q0', 'q1'), ('q1', 'q2')]
        G = Graph(vertices, edges,
                  layout={'q0': [-2, 0, 0], 'q1': [-1, 0, 0], 'q2': [0, 0, 0]},
                  edge_config={'color': BLUE, 'stroke_width': 2},
                  labels=True
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))

        # Esperar un momento antes de cambiar el color de un nodo
        self.wait(1)

        # Cambiar el color del nodo 'q1' a rojo
        self.play(G.vertices['q1'].animate.set_color(RED))

        # Esperar un momento antes de finalizar la animación
        self.wait(1)
