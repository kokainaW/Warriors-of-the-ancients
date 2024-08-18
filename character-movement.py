def game_loop():
    global character1_x, character1_y, character2_x, character2_y
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        
        # Move character 1
        if keys[pygame.K_a]:
            character1_x -= 5
        if keys[pygame.K_d]:
            character1_x += 5
        if keys[pygame.K_w]:
            character1_y -= 5
        if keys[pygame.K_s]:
            character1_y += 5
        
        # Move character 2
        if keys[pygame.K_LEFT]:
            character2_x -= 5
        if keys[pygame.K_RIGHT]:
            character2_x += 5
        if keys[pygame.K_UP]:
            character2_y -= 5
        if keys[pygame.K_DOWN]:
            character2_y += 5
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw characters
        screen.blit(character1_img, (character1_x, character1_y))
        screen.blit(character2_img, (character2_x, character2_y))
        
        # Update display
        pygame.display.flip()
        
        # Frame rate
        clock.tick(30)

