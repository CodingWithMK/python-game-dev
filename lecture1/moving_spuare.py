import pygame

# Initialize main event
pygame.init()

# Square features
square_x = 400
square_y = 300
square_size = 50
square_color = (200, 30, 30)

# Set window size
screen = pygame.display.set_mode((800, 600))

running = True

clock = pygame.time.Clock() # <-- Event handler for FPS

# Main game loop
while running:
    # 1) EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2) UPDATE (empty for now)

    # 3) RENDER
    screen.fill((30, 30, 30)) # <-- Fills the entire window with dark greyish color

    # Draw square on window
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()