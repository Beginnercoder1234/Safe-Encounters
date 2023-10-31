# screen_manager.py
import pygame
import sys

#from button_screen import create_button_screen
#from wrong_choice import show_wrong_choice_content
# Define a variable to keep track of the current screen
current_screen = "button_screen"  # Initialize with the button screen

def switch_to_button_screen():
    global current_screen
    SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    current_screen = "create_button_screen"

def switch_to_wrong_choice_content():
    global current_screen
    SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    create_fourth_slide()
def switch_to_right_choice_content():
    global current_screen
    SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Add logic to switch to the right choice content
    current_screen = show_right_choice_content(screen)
    print("I am inside1")

def switch_to_wrong_choice_2_content():
    global current_screen
    # Add logic to switch to the wrong choice 2 content
    current_screen = "wrong_choice_2_content"