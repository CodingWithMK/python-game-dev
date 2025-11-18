import pygame
import math

# Initialize main event
pygame.init()

# Square features
square_x = 400
square_y = 300
square_size = 50
square_color = (200, 30, 30)

square_speed = 5

WIDTH = 800
HEIGHT = 600

# Set window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

clock = pygame.time.Clock() # <-- Event handler for FPS

# Main game loop
while running:
    # 1) EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2) UPDATE
    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    # 1) Set dx, dy for pressed button
    if keys[pygame.K_RIGHT]:
        dx += 1
    if keys[pygame.K_LEFT]:
        dx -= 1
    if keys[pygame.K_UP]:
        dy -= 1
    if keys[pygame.K_DOWN]:
        dy += 1
    if (dx, dy) == (0, 0):
        dx = 0
        dy = 0

    # 2) Normalize (dx, dy) if needed
    if (dx, dy) != (0, 0):
        length = math.sqrt(dx * dx + dy * dy)
        dx = dx / length * square_speed
        dy = dy / length * square_speed

    # 3) Finally update square_x and square_y
    square_x += dx
    square_y += dy

    # 4) Boundary Clamp
    if square_x < 0:
        square_x = 0
    if square_x + square_size > WIDTH:
        square_x = WIDTH - square_size
    
    if square_y < 0:
        square_y = 0
    if square_y + square_size > HEIGHT:
        square_y = HEIGHT - square_size

    # 3) RENDER
    screen.fill((30, 30, 30)) # <-- Fills the entire window with dark greyish color

    # Draw square on window
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()