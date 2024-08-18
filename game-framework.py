import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Warriors of the Ancients")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load character images
# Replace 'path_to_image' with the actual paths to your images
character1_img = pygame.image.load('path_to_character1_image.png')
character2_img = pygame.image.load('path_to_character2_image.png')

# Game variables
character1_x, character1_y = 100, 300
character2_x, character2_y = 600, 300

# Main game loop
def game_loop():
    global character1_x, character1_y, character2_x, character2_y
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw characters
        screen.blit(character1_img, (character1_x, character1_y))
        screen.blit(character2_img, (character2_x, character2_y))
        
        # Update display
        pygame.display.flip()
        
        # Frame rate
        clock.tick(30)

if __name__ == "__main__":
    game_loop()

