import pygame
import sys
import assets  # Import the asset loading functions from assets.py
from button_screen import create_button_screen


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Safe Encounters - Fourth Screen")

# Load background image and character image using the asset loading functions
room_image = assets.load_background_image("Room.jpg", SCREEN_WIDTH, SCREEN_HEIGHT)
character_image = assets.load_character_image("character.png", 500, 700)
character_width = 500  # Width of the character image
character_height = 700

# Define arrow image and position
arrow_width, arrow_height = 120, 120
arrow_image = pygame.image.load("arrow.png")
arrow_image = pygame.transform.scale(arrow_image, (arrow_width, arrow_height))
arrow_x = 1100
arrow_y = 650
arrow_position = (arrow_x, arrow_y)
arrow_rect = pygame.Rect(arrow_position[0], arrow_position[1], arrow_width, arrow_height)

# Define the text box parameters
text_box = pygame.Rect(120, 475, 1200, 300)
text_color = (255, 255, 255)
text_font = pygame.font.SysFont("LEMONMILK-Medium", 40)

# Define arrow visibility
arrow_visible = True

def create_fourth_slide():
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos

                    # Check if the user clicked on the arrow
                    if arrow_rect.collidepoint(x, y):
                        create_button_screen()
                        pass

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the background image and character
        screen.blit(room_image, (0, 0))
        screen.blit(character_image, (SCREEN_WIDTH // 5 - character_width // 2, SCREEN_HEIGHT - character_height - 20))

        # Draw the arrow image
        screen.blit(arrow_image, arrow_position)

        # Draw the text box
        pygame.draw.rect(screen, (0, 0, 0), text_box)
        # Add text content to the text box
        text = [
            "Imagine you're at a friend's house, and both of",
            "your parents aren't there. You notice a gun in ",
            "your friend's drawer. What do you think is the ",
            "best thing to do in this situation?",
        ]
        y_offset = 0
        for line in text:
            text_surface = text_font.render(line, True, text_color)
            screen.blit(text_surface, (text_box.x + 10, text_box.y + 10 + y_offset))
            y_offset += text_surface.get_height()

        if arrow_visible:  # Ensure arrow is only visible when needed
            screen.blit(arrow_image, arrow_position)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)  # 30 FPS

if __name__ == "__main__":
    create_fourth_slide()
