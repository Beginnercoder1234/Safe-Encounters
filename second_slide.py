# second_slide.py
import os
import pygame
import sys
from time import *
import pygame.mixer
from MAIN import create_button, handle_button_click
from third_slide import create_third_slide

path = r"C:\Users\ishaa\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
os.chdir(path)

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
#information font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)
# second_slide.py
bold_font = pygame.font.Font("BOLDFONT.ttf", 80)
WHITE = (255, 255, 255)
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.center = (x, y)
#     screen.blit(text_surface, text_rect)
text_font = pygame.font.SysFont("LEMONMILK-Medium", 40)



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
lines = [
    "Hey there, welcome to our exciting learning ",
    "game! It's like a fun adventure where you'll ",
    "discover how to make safe choices in different  ",
    "situations. As you play, you'll come across  ",
    "challenges, and by making the right choices,",
    "you can keep moving forward and having a   ",
    "great time while learning!  ",
    
]
def create_second_slide(screen, background_image):
    
    clock = pygame.time.Clock()

    # Load the image for the second slide
    second_slide_image = pygame.image.load("background.jpg")  # Replace with the actual image file name
    second_slide_image = pygame.transform.scale(second_slide_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    #next_button_rect = original_button_rect.copy()
    
    
    # Define the semi-transparent white color with reduced alpha value
    white_semi_transparent = (255, 255, 255, 128)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 95)
                if button_rect.collidepoint(x, y):
                    create_third_slide()  # Replace with your function to create the next screen
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
        for line in lines:
            text_surface = text_font.render(line, True, BLACK)
            text_rect = text_surface.get_rect(topleft=(x_position, y_position))
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10
            
        #Next Button
        create_button("NEXT",  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220  , 300, 75, bold_font, (0,43,128), (25,217,255))
        
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)  # 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 220, 300, 75)
                if button_rect.collidepoint(x, y):
                    create_third_slide()