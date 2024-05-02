import pygame
import sys

pygame.init()

# Configuración de la ventana
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animación en pygame")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Posición inicial del objeto
x, y = 50, 50
vel = 5

clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # Dibuja la pantalla
    screen.fill(white)
    pygame.draw.rect(screen, black, (x, y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
