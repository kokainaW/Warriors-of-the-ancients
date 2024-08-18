# Game variables
character1_health = 100
character2_health = 100

def check_collision(x1, y1, x2, y2):
    return (x1 < x2 + 50 and x1 + 50 > x2 and
            y1 < y2 + 50 and y1 + 50 > y2)

def game_loop():
    global character1_x, character1_y, character2_x, character2_y
    global character1_health, character2_health
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        
        # Move characters
        if keys[pygame.K_a]:
            character1_x -= 5
        if keys[pygame.K_d]:
            character1_x += 5
        if keys[pygame.K_w]:
            character1_y -= 5
        if keys[pygame.K_s]:
            character1_y += 5
        
        if keys[pygame.K_LEFT]:
            character2_x -= 5
        if keys[pygame.K_RIGHT]:
            character2_x += 5
        if keys[pygame.K_UP]:
            character2_y -= 5
        if keys[pygame.K_DOWN]:
            character2_y += 5
        
        # Check for collision
        if check_collision(character1_x, character1_y, character2_x, character2_y):
            character1_health -= 1
            character2_health -= 1
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw characters
        screen.blit(character1_img, (character1_x, character1_y))
        screen.blit(character2_img, (character2_x, character2_y))
        
        # Draw health bars
        pygame.draw.rect(screen, BLACK, (20, 20, character1_health, 10))
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 120, 20, character2_health, 10))
        
        # Update display
        pygame.display.flip()
        
        # Frame rate
        clock.tick(30)

