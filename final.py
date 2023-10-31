# second_slide.py
import winsound
import os
import pygame
import sys
from time import *
import pygame.mixer
from MAIN1 import create_button, handle_button_click
from text_animation import display_text_animation

from pygame import mixer
#from playsound import playsound



path = r"C:\Users\ishaa\OneDrive\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
os.chdir(path)
#click = pygame.mixer.Sound(os.path.join('click.wav'))
#click.set_volume(10000)  # Adjust the volume level if needed
# frequency is set to 500Hz
#freq = 500
 
# duration is set to 100 milliseconds             
#dur = 100

pygame.init()
#pygame.mixer.init()
mixer.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
#information font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)
# second_slide.py
bold_font = pygame.font.Font("BOLDFONT.ttf", 80)
bold_font2 = pygame.font.Font("BOLDFONT.ttf", 40)
WHITE = (255, 255, 255)
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.center = (x, y)
#     screen.blit(text_surface, text_rect)
text_font = pygame.font.SysFont("LEMONMILK-Medium", 40)
pygame.display.set_caption("Safe Encounters - Final Screen")


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
lines = [
    "Thank you for playing our exciting learning",
    "game! It's been a fantastic adventure where",
    "you've learned to make safe choices in    ",
    "different situations. Your commitment to",
    "making the right choices made you have a ",
    "fantastic time while learning. We truly ",
    "appreciate your participation in our game!",
    
]
def create_second_slide(screen, background_image):
    
    clock = pygame.time.Clock()

    # Load the image for the second slide
    second_slide_image = pygame.image.load("background.jpg")  # Replace with the actual image file name
    second_slide_image = pygame.transform.scale(second_slide_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    #next_button_rect = original_button_rect.copy()
    text_animation_complete = False
    
    # Define the semi-transparent white color with reduced alpha value
    white_semi_transparent = (255,255,255, 128)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 95)
                #winsound.PlaySound('click.wav', winsound.SND_FILENAME)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    pygame.quit()
                    sys.exit()
                      # Replace with your function to create the next screen
        # Draw the background image
        screen.blit(background_image, (0, 0))  # Use the passed background_image
        #draw the button
        
        

        # Draw the image for the second slide
        screen.blit(second_slide_image, (0, 0))
        # Draw the semi-transparent white rectangle at a specific position
        rect_x = 120  # Adjust this value for the x-coordinate
        rect_y = 55  # Adjust this value for the y-coordinate
        rect_width = 1200  # Adjust this value for the width of the rectangle
        rect_height = 700  # Adjust this value for the height of the rectangle
        border_radius = 20  # Adjust this value for the rounded corners
        
        transparent_rect = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        pygame.draw.rect(transparent_rect, white_semi_transparent, (0, 0, rect_width, rect_height), border_radius=border_radius)
        screen.blit(transparent_rect, (rect_x, rect_y))
        # Draw any other content you want for the second slide
        #text
        y_position = 100
        x_position = 150
        # Inside your while loop where you draw the second slide
    
        # Inside your while loop where you draw the second slide
        # Inside your while loop where you draw the second slide
        if not text_animation_complete:
            display_text_animation(lines, screen, text_font, x_position, y_position,)
            text_animation_complete = True  # Mark the text animation as complete

        # Check if the text animation is complete before drawing the button
        if text_animation_complete:
            for line in lines:
                text_surface = text_font.render(line, True, BLACK)
                text_rect = text_surface.get_rect(topleft=(x_position, y_position))
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10
            create_button("LEAVE", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75, bold_font, (0, 43, 128), (25, 217, 255))
        
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)  # 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    pygame.quit()
                    sys.exit()
# Define a function to display the text animation



