import os
import pygame
import sys
from pygame import mixer
#path = r"C:\Users\ishaa\OneDrive\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
#os.chdir(path)
# Initialize Pygame
pygame.init()
#mixer.init()
#mixer.music.load("click.wav")
#mixer.music.set_volume(0.4)
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Safe Encounters - Main App")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sound_effect = pygame.mixer.Sound('click.wav')
# Load the background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
button_clicked = False
def create_fonts():
    title_font = pygame.font.Font(None, 80)  # Increase title font size
    button_font = pygame.font.Font(None, 75)  # Increase button font size
    bold_font = pygame.font.Font("BOLDFONT.ttf", 80)  # Replace with the actual path to a bold font file
    return title_font, button_font, bold_font

def draw_revealed_text(text, x, y, font, color):
    revealed_text = ""
    for i in range(len(text)):
        revealed_text += text[i]
        text_surface = font.render(revealed_text, True, color)
        screen.blit(text_surface, (x, y))
        pygame.display.update()
        pygame.time.wait(50)  # Adjust the reveal speed here
# Create functions for common code like button creation
def create_button(text, x, y, width, height, font, hover_color, normal_color):
    button_text = font.render(text, True, WHITE)
    text_width, text_height = button_text.get_size()
    button_text = font.render(text, True, WHITE)
    text_width, text_height = button_text.get_size()
    
    button_rect = pygame.Rect(x, y, width, height)
    is_hovering = button_rect.collidepoint(pygame.mouse.get_pos())
    
    if is_hovering:
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=10)
        is_hovering=True
    else:
        pygame.draw.rect(screen, normal_color, button_rect,border_radius=10)
        is_hovering=False
    button_text = font.render(text, True, WHITE if is_hovering else BLACK)
    #text_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 95))
    text_rect = button_text.get_rect(center=(button_rect.centerx, button_rect.centery + 5))
    screen.blit(button_text, text_rect)
    
# Uncomment the create_button function definition
def create_button1(text, x, y, width, height, font, hover_color, normal_color):
    button_text = font.render(text, True, WHITE)
    text_width, text_height = button_text.get_size()
    button_text = font.render(text, True, WHITE)
    text_width, text_height = button_text.get_size()
    
    button_rect = pygame.Rect(x, y, width, height)
    is_hovering = button_rect.collidepoint(pygame.mouse.get_pos())
    
    if is_hovering:
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=10)
        is_hovering=True
    else:
        pygame.draw.rect(screen, normal_color, button_rect,border_radius=10)
        is_hovering=False
    button_text = font.render(text, True, WHITE if is_hovering else BLACK)
    #text_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 95))
    text_rect = button_text.get_rect(center=(button_rect.centerx, button_rect.centery + 5))
    screen.blit(button_text, text_rect)


def create_multiline_button(lines, x, y, width, height, font, hover_color, normal_color):
    is_hovering = False  # Initialize is_hovering to False
    button_text = []
    text_height = 0
    
    for line in lines:
        line_text = font.render(line, True, WHITE if is_hovering else BLACK)
        button_text.append(line_text)
        text_height += line_text.get_height()

    width = max(text.get_width() for text in button_text) + 30  # Add some padding
    height = text_height + 10
    
    button_rect = pygame.Rect(x, y, width, height)
    is_hovering = button_rect.collidepoint(pygame.mouse.get_pos())  # Update is_hovering here
    
    if is_hovering:
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, normal_color, button_rect, border_radius=10)

    text_y = button_rect.centery - text_height // 2
    for text_surface in button_text:
        text_rect = text_surface.get_rect(center=(button_rect.centerx, text_y + text_surface.get_height() // 2))
        screen.blit(text_surface, text_rect)
        text_y += text_surface.get_height()

    return button_rect



def handle_button_click(event, button_rect, action=None):
    original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    button_rect = original_button_rect.copy()
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x, y = event.pos

        # Check if the mouse click occurred within the button's bounds
        if button_rect.collidepoint(x, y):
            #mixer.music.load("click.wav")
            mixer.music.set_volume(1)
            mixer.Channel(0).play(pygame.mixer.Sound('whoosh_V1.mp3')) 
            # Handle the button click action
            if action:
                action()
              # Call the provided function for the button acti

def create_start_screen():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Call the create_button function
        create_button("Start", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 95, bold_font, (0, 43, 128), (25, 217, 255))

        # Check if the button was clicked
        if button_clicked:
            #sound_effect.play()  # Play the click sound when the button is clicked
            button_clicked = False  # Reset the button_clicked flag

        # Update the display
        pygame.display.flip()

