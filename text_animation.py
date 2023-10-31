import pygame, sys
import pygame.mixer

from pygame.locals import *

pygame.init()
pygame.mixer.init()
text_writing_sound = pygame.mixer.Sound('click.wav')

BLACK = (0,0,0)
def display_text_animation(lines, screen, font, x_position, y_position):
    #y_position = 100
    #x_position = 150
    for line in lines:
        text = ""
        for char in line:
            text += char
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(topleft=(x_position, y_position))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.wait(4) 
            pygame.mixer.Sound('click.wav').play() # Adjust the delay as needed
        y_position += text_rect.height + 10
        pygame.time.wait(0)

def display_text_animation_with_color(lines, screen, font, x_position, y_position, color):
    #y_position = 100
    #x_position = 150
    for line in lines:
        text = ""
        for char in line:
            text += char
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(topleft=(x_position, y_position))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.wait(4) 
            pygame.mixer.Sound('click.wav').play()# Adjust the delay as needed
        y_position += text_rect.height + 10
        pygame.time.wait(0)
def display_text_animation_with_right(lines, screen, font, x_position, y_position, color):
    #y_position = 100
    #x_position = 150
    for line in lines:
        text = ""
        for char in line:
            text += char
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(topleft=(x_position, y_position))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.wait(4) 
            #pygame.mixer.Sound('click.wav').play()# Adjust the delay as needed
        y_position += text_rect.height + 10
        pygame.time.wait(0)
