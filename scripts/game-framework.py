import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Warriors of the Ancients")

# Load images
try:
    character1_img = pygame.image.load('images/character1.png')
    character2_img = pygame.image.load('images/character2.png')
    print("Images loaded successfully!")
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill((0, 0, 0))
    # Draw images
    screen.blit(character1_img, (50, 50))  # Example coordinates
    screen.blit(character2_img, (200, 50)) # Example coordinates
    pygame.display.flip()

pygame.quit()

