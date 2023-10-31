import os
import pygame
import sys
from time import *
from pygame import mixer
import winsound
from MAIN1 import create_button, handle_button_click
from MAIN1 import create_fonts
from second_slide2 import create_second_slide
#from tehird_slide import create_third_slide

path = r"C:\Users\ishaa\OneDrive\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
os.chdir(path)
sound_effect = pygame.mixer.Sound('click.wav')
# Initialize Pygame
pygame.init()
mixer.init()
  

mixer.music.set_volume(0.1)
mixer.Channel(1).play(pygame.mixer.Sound('home_background_music.mp3'))
#mixer.Channel(1).play(pygame.mixer.Sound('whoosh.mp3'))
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Safe Encounters - Start Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
title_font = pygame.font.Font(None, 80)  # Increase title font size
button_font = pygame.font.Font(None, 75)  # Increase button font size
bold_font = pygame.font.Font("BOLDFONT.ttf", 80)  # Replace "path_to_bold_font.ttf" with the actual path to a bold font file


# Load the background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)  

def your_button_action_function():
    # Replace this with the action you want to perform
    #mixer.music.load("click.wav")
    mixer.music.set_volume(0.3)
    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
    create_second_slide(screen, background_image)
    

def create_start_screen():
    clock = pygame.time.Clock()
    is_hovering = False
    original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    button_rect = original_button_rect.copy()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            handle_button_click(event, button_rect, action=your_button_action_function)
            
            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the user clicked on the "Start" button
                #x,y = event.pos
                #button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 95)
        # Load the second slide and pass the background_image
                #if button_rect.collidepoint(x,y):
                    #create_second_slide(screen, background_image)   

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the title
        
        draw_text("Safe Encounters", bold_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)



        # Draw the "Start" button
        if mixer.get_busy() == False:
            create_button("Start",  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50  , 300, 95, bold_font, (0,43,128), (25,217,255))
   

        



        # Draw other options like instructions, settings, etc., if needed
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)  # 30 FPS

def create_main_game_screen(): 
    clock = pygame.time.Clock()
    
    create_second_slide(screen)

        # Draw the background for the main game screen here
        

        # Draw content for the main game screen here

        # Update the display
    pygame.display.flip()
        
        # Control the frame rate
    clock.tick(30)  # 30 FPS
def draw_text(text, font, color, x, y, is_hovering=False, scale=1.0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)

    # Apply scaling if hovering
    if is_hovering:
        new_width = int(text_rect.width * scale)
        new_height = int(text_rect.height * scale)
        text_surface = pygame.transform.scale(text_surface, (new_width, new_height))
        text_rect = text_surface.get_rect(center=text_rect.center)

    screen.blit(text_surface, text_rect)


if __name__ == "__main__":
    create_start_screen()