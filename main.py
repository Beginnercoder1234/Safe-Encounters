import os
import asyncio
import pygame
import sys
from time import *
from pygame import mixer

from MAIN1 import create_button, handle_button_click
from MAIN1 import create_fonts
from second_slide2 import create_second_slide
#from tehird_slide import create_third_slide

#path = r"C:\Users\ishaa\OneDrive\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
#os.chdir(path)
sound_effect = pygame.mixer.Sound('click.wav')
# Initialize Pygame
pygame.init()
mixer.init()
  

mixer.Channel(3).set_volume(0.15)
mixer.Channel(3).play(pygame.mixer.Sound('action.mp3'),-1)
#mixer.Channel(1).play(pygame.mixer.Sound('home_background_music.mp3'))
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
bold_font = pygame.font.Font("BOLDFONT.ttf", 80)
bold_font_credits = pygame.font.Font("BOLDFONT.ttf", 60)  # Replace "path_to_bold_font.ttf" with the actual path to a bold font file


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
music_paused = False

def main():
    clock = pygame.time.Clock()
    global music_paused
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                #winsound.PlaySound('click.wav', winsound.SND_FILENAME)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    create_credit_slide(screen, background_image)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                music_rect = pygame.Rect(20, 12, 90,90)
                #winsound.PlaySound('click.wav', winsound.SND_FILENAME)
                if music_rect.collidepoint(x, y):
                        if music_paused:
                            mixer.Channel(3).unpause()
                            music_paused = False
                        else:
                            mixer.Channel(3).pause()
                            music_paused = True
                    #create_credit_slide(screen, background_image)
    
    
        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the title
        #music_image = pygame.image.load("speaker.png")  # Replace with the actual image file name
        #music_rect = music_image.get_rect()
        #button_width = 20  # Replace with your desired width
        #button_height = 20  # Replace with your desired height

        #button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 40 // 2, SCREEN_HEIGHT // 2 - button_height // 2, 2, 2)
        #music_image = pygame.transform.scale(music_image, (150, 150))
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
        draw_text("Safe Encounters", bold_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        # Draw the "Start" button
        #if mixer.Channel(1).get_busy() == False:
        create_button("Start",  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50  , 300, 95, bold_font, (0,43,128), (25,217,255))
        create_button("CREDITS", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75, bold_font, (0, 43, 128), (25, 217, 255))
         

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
def create_credit_slide(screen, background_image):
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 25)
    clock = pygame.time.Clock()

    # Load the image for the second slide
    second_slide_image = pygame.image.load("background.jpg")  # Replace with the actual image file name
    second_slide_image = pygame.transform.scale(second_slide_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    #next_button_rect = original_button_rect.copy()
    text_animation_complete = False
    lines = [
    "Organizations:",
    "CAGV: CT Against Gun Violence",
    "Compassionate Atlanta  ",
    "Moms Demand Action For Gun Sense In America  ",
    "Everytown For Gun Safety Support Fund",
    "People:",
    "Professor David I. Schwartz Rochester Institue of Technology",
    "Professor David Simkins of IGM",
    "Lucy Mcbath's Office", 
    ]
    # Define the semi-transparent white color with reduced alpha value
    white_semi_transparent = (255,255,255, 128)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                #winsound.PlaySound('click.wav', winsound.SND_FILENAME)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    create_credit_slide2(screen, background_image)
                    pass
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
        create_button("NEXT",  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220  , 300, 75, bold_font, (0,43,128), (25,217,255))
        #text
        y_position = 100
        x_position = 150
        # Inside your while loop where you draw the second slide
        # Inside your while loop where you draw the second slide
        # Inside your while loop where you draw the second slide
        for line in lines:
                if "Organizations" in line or "People" in line:  # Bold these lines
                    text_surface = bold_font_credits.render(line, True, BLACK)
                else:
                    text_surface = text_font.render(line, True, BLACK)
                text_rect = text_surface.get_rect(topleft=(x_position, y_position))
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10
        
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)  # 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    create_credit_slide2(screen, background_image)

def create_credit_slide2(screen, background_image):
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 25)
    clock = pygame.time.Clock()

    # Load the image for the second slide
    second_slide_image = pygame.image.load("background.jpg")  # Replace with the actual image file name
    second_slide_image = pygame.transform.scale(second_slide_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    #next_button_rect = original_button_rect.copy()
    text_animation_complete = False
    lines = [
    "Softwares:",
    "Python",
    "Pygame  ",
    "Photoshop, Premiere Pro, After Effects  ",
    "Game Assets:",
    "Free Design File: Loutpany",
    "Pixabay: BabarAli",
    "Itch.io: Incursio", 
    "Itch.io: Sungrraphica",
    "Itch.io: PogoNr ",
    "Itch.io: Zeenaz",
    "Tenor: mojitok",
    "Pixabay: Blender Timer"
    ]
    # Define the semi-transparent white color with reduced alpha value
    white_semi_transparent = (255,255,255, 128)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                #winsound.PlaySound('click.wav', winsound.SND_FILENAME)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    main()
                    pass
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
        create_button("HOME",  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220  , 300, 75, bold_font, (0,43,128), (25,217,255))
        #text
        y_position = 75
        x_position = 150
        # Inside your while loop where you draw the second slide
        # Inside your while loop where you draw the second slide
        # Inside your while loop where you draw the second slide
        for line in lines:
                if "Softwares:" in line or "Game Assets:" in line:  # Bold these lines
                    text_surface = bold_font_credits.render(line, True, BLACK)
                else:
                    text_surface = text_font.render(line, True, BLACK)
                text_rect = text_surface.get_rect(topleft=(x_position, y_position))
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10
        
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)  # 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                if button_rect.collidepoint(x, y):
                    mixer.music.set_volume(0.3)
                    mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                    main()
                    pass

if __name__ == "__main__":
    main()