import pygame
import math

# Initialize main event
pygame.init()

# Square features
square_x = 400
square_y = 300
square_size = 50
square_color = (200, 30, 30)

# Speed features
MAX_SPEED = 300
ACCELERATION = 800
FRICTION = 1000

velocity_x = 0
velocity_y = 0

square_speed = 300

WIDTH = 800
HEIGHT = 600

# Set window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

clock = pygame.time.Clock() # <-- Event handler for FPS

# Main game loop
while running:
    # Get Delta Time for movement smoothness
    delta_time = clock.tick(120) / 1000

    # 1) EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2) UPDATE
    keys = pygame.key.get_pressed()

    dx, dy = 0, 0

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
        vel_x = dx / length
        vel_y = dy / length

        # 3) Update speed
        velocity_x += dx * ACCELERATION * delta_time
        velocity_y += dy * ACCELERATION * delta_time

    else:
        # ----- Apply friction if no input -----
        if velocity_x != 0:
            velocity_x -= (1 if velocity_x > 0 else -1) * FRICTION * delta_time
            # threshold to prevent small oscillations
            if abs(velocity_x) < 1e-2:
                velocity_x = 0
        
        if velocity_y != 0:
            velocity_y -= (1 if velocity_y > 0 else -1) * FRICTION * delta_time
            if abs(velocity_y) < 1e-2:
                velocity_y = 0

    # ----- Setup velocity limit (MAX_SPEED) -----
    # Find speed vector
    speed = (velocity_x * velocity_x + velocity_y * velocity_y) ** 0.5
    # Handle max_speed exceeding
    if speed > MAX_SPEED:
        velocity_x = (velocity_x / speed) * MAX_SPEED
        velocity_y = (velocity_y / speed) * MAX_SPEED

    square_x += velocity_x * delta_time
    square_y += velocity_y * delta_time

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

pygame.quit()