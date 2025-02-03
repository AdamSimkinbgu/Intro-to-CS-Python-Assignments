import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (1280, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("get rekt kid")

# Set the background color
bg_color = (180, 200, 120)

# Load the chicken image
image = pygame.image.load("get rekt.png")

# Get the rect for the chicken image
object_rect = image.get_rect()

# Set the initial position of the chicken
object_rect.x = 320
object_rect.y = 40

# Set the movement speed of the chicken
object_speed = 1

# Set the chicken to be facing right
object_direction = "right"

# Run the game loop
running = True
while running:
    # Fill the screen with the background color
    screen.fill(bg_color)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the chicken position
    if object_direction == "right":
        object_rect.x += object_speed
    elif object_direction == "left":
        object_rect.x -= object_speed

    # Change the direction of the chicken if it hits the edge of the screen
    if object_rect.right > window_size[0]:
        object_direction = "left"
    elif object_rect.left < 0:
        object_direction = "right"

    # Draw the chicken
    screen.blit(image, object_rect)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()