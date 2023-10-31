# wrong_choice_2.py
import pygame
import sys
from video import create_video_slide
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def show_wrong_choice_2_content(screen):
    # Define the content for the second wrong answer here
    
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Define the text and font
    text_lines = [
        "Talking to your friend about the gun might not be a good idea.",
        "Guns are very serious and can be dangerous. Instead, always",
        "remember that if you see a gun, you should never touch it", 
        "and tell a grown-up you trust, like a parent, teacher, or ",
        "another adult in charge. It's all about making sure everyone",
        "stays safe."
    ]
    
    text_box = pygame.Rect(120, 475, 1200, 300)
    text_color = (255, 255, 255)  # White
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 30)
    
    # Create the arrow image
    arrow_width = 120
    arrow_height = 55
    arrow_image = pygame.image.load("arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (arrow_width, arrow_height))
    arrow_position = (1100, 710)
    arrow_rect = pygame.Rect(arrow_position[0], arrow_position[1], arrow_width, arrow_height)
    
    # Event loop for this screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        # Check if the user clicked on the arrow
                        if arrow_rect.collidepoint(x, y):
                            create_video_slide(screen)
                            pass
        
        # Clear the screen
        screen.fill(BLACK)
        
        # Draw the text box
        pygame.draw.rect(screen, BLACK, text_box)
        pygame.draw.rect(screen, WHITE, text_box, 3)
        screen.blit(arrow_image, arrow_position)
        
        # Display the text lines
        y_position = 480
        for line in text_lines:
            text_surface = text_font.render(line, True, text_color)
            text_rect = text_surface.get_rect(topleft=(150, y_position))
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10
        
        # Update the display
        pygame.display.flip()
    
    # You can add logic here to allow the player to try again
    
    # Return control to the main game loop
    return
