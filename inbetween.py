import os
import pygame
import sys
from time import *
from pygame import mixer
import pygame.mixer
#import winsound
from MAIN1 import create_button
from level2 import create_level_2
# Initialize Pygame
pygame.init()
mixer.init()
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Safe Encounters - Level 1")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
music_paused = False
# Fonts
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 75)
bold_font = pygame.font.Font("BOLDFONT.ttf", 80)

# Load background image or assets
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
level2_rect = pygame.Rect(SCREEN_WIDTH // 2 -160, SCREEN_HEIGHT // 2 + 10  , 300, 75)
#video_rect = pygame.Rect(SCREEN_WIDTH // 2 +50, SCREEN_HEIGHT // 2 + 10  , 300, 75,)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def inbetween_slide():
    global current_screen
    global music_paused
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the user clicked on the "Next" button
                x,y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 95)
                    # Transition to the new screen
                if button_rect.collidepoint(x, y):
                    pass
                    #pygame.mixer.Sound('click.wav').play()
        # Draw the background image
        screen.blit(background_image, (0, 0))
    
        # Draw title and other elements
        draw_text("LEVEL 2: THE SOCIAL MEDIA POST", bold_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
        
        music_width = 90  # Replace with your desired width
        music_height = 90  # Replace with your desired height
        x = 20  # Replace with your desired x-coordinate
        y = 12  # Replace with your desired y-coordinate

        # Create the button_rect with the specified dimensions and position
        music_rect = pygame.Rect(x, y, music_width, music_height)

        # Load and scale the image to match the button's dimensions
        music_image = pygame.image.load("speaker.png")  # Replace with the actual image file name
        music_image = pygame.transform.scale(music_image, (music_width, music_height))
        screen.blit(music_image, music_rect)  
        # Add more elements and interactivity as needed
        create_button("LEVEL 2",  SCREEN_WIDTH // 2 -160, SCREEN_HEIGHT // 2 + 10  , 300, 75, bold_font, (0,43,128), (25,217,255))
        #create_button("VIDEO",  SCREEN_WIDTH // 2 +50, SCREEN_HEIGHT // 2 + 10  , 300, 75, bold_font, (0,43,128), (25,217,255))
        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)  # 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 + 220, 300, 75)
                
                if level2_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    create_level_2()
                #elif video_rect.collidepoint(x,y):
                    #mixer.music.set_volume(0.3)
                    #mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    #create_level_2()
                if music_rect.collidepoint(x, y):
                            if music_paused:
                                mixer.Channel(3).unpause()
                                music_paused = False
                            else:
                                mixer.Channel(3).pause()
                                music_paused = True