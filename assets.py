# assets.py

import pygame

def load_background_image(image_path, screen_width, screen_height):
    room_image = pygame.image.load("Room.jpg")
    return pygame.transform.scale(room_image, (screen_width, screen_height))

def load_character_image(image_path, character_width, character_height):
    character_image = pygame.image.load("character.png")
    return pygame.transform.scale(character_image, (character_width, character_height))
