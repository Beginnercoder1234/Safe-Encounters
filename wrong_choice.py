# wrong_choice.py
import pygame
import sys
import screen_management

#from fourth_slide2 import create_fourth_slide
#from fourth_slide import create_fourth_slide
from video import create_video_slide
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def show_wrong_choice_content(screen):
    # Define the content for the wrong answer here
    
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Define the text and font
    text_lines = [
        "Ignoring a gun in a situation like this can be very dangerous. ",
        "Guns should never be taken lightly or ignored. It's essential ",
        "to remember that if you ever come across a firearm, you should", 
        "never touch it and immediately find an adult or a trusted ",
        "authority figure to inform them about it. Your safety is the ",
        "top priority."
        
        
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
                        create_fourth_slide()
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
