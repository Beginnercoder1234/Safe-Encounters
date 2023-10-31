import pygame
import sys
from MAIN1 import create_button
from MAIN1 import create_multiline_button
from right_choice import show_right_choice_content
from wrong_choice import show_wrong_choice_content
from wrong_choice_2 import show_wrong_choice_2_content
from video import create_video_slide
#from screen_management import switch_to_right_choice_content
#from screen_management import switch_to_wrong_choice_content
#from screen_management import switch_to_wrong_choice_2_content
import assets

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Safe Encounters - Button Screen")
size1x=600
size1y=300
size2x=200
size2y=200
size3x=200
size3y=200

current_screen = "button_screen"
# Define button positions and sizes
button1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 640, SCREEN_HEIGHT // 2 + 100, size1x, size1y)
button2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 290, size2x, size2y)
button3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 120, SCREEN_HEIGHT // 2 + 100, size3x, size3y)

# Initialize room and character positions
room_positions = [(0, 0), (100, 100)]  # Example room positions
current_room_index = 0  # Initialize with the first room
current_character_position = room_positions[current_room_index]

# Load background room image and character image
room_image = assets.load_background_image("Room.jpg", SCREEN_WIDTH, SCREEN_HEIGHT)
character_image = assets.load_character_image("character.png", 500, 700)
character_width = 500  # Width of the character image
character_height = 700
bold_font = pygame.font.Font("BOLDFONT.ttf", 80)
def create_button_screen():
    global current_screen
    clock = pygame.time.Clock()
    global current_character_position
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    mouse_position = pygame.mouse.get_pos()  
                    print (mouse_position)
                    print(x)
                    print(y)
                    # Check if the user clicked on the buttons
                    #button3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 120, SCREEN_HEIGHT // 2 + 100, size3x, size3y)
                if button3_rect.collidepoint(x,y): #SCREEN_WIDTH // 2 - - 120, SCREEN_HEIGHT // 2 + 100):
                        current_screen = show_right_choice_content(screen)  # Transition to the right choice screen
                        print(SCREEN_WIDTH)
                        print(SCREEN_WIDTH // 2 - - 120)
                        print(SCREEN_HEIGHT)
                        print(SCREEN_HEIGHT // 2 + 100)
                        print("button is being pressed")
                elif button2_rect.collidepoint(mouse_position):  #SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 290):
                        current_screen = show_wrong_choice_content(screen)  # Transition to the wrong choice content screen
                        print("button is being pressed2")
                elif button1_rect.collidepoint(mouse_position):#SCREEN_WIDTH // 2 - 640, SCREEN_HEIGHT // 2 + 100):
                        current_screen = show_wrong_choice_2_content(screen)
                        print("button is being pressed3")  # Transition to the wrong choice 2 content screen

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the background room image and character
        screen.blit(room_image, (0, 0))
        screen.blit(character_image, (SCREEN_WIDTH // 5 - character_width // 2, SCREEN_HEIGHT - character_height - 20))

        multiline_button_lines1 = ["Inform your", "parents"]
        create_multiline_button(multiline_button_lines1, SCREEN_WIDTH // 2 + 120, SCREEN_HEIGHT // 2 + 100, size1x, size1y, bold_font, (0, 43, 128), (25, 217, 255))


        # Use create_multiline_button to create a multiline button
        multiline_button_lines = ["Confront your", "friend"]  # Define the lines of text for the multiline button
        create_multiline_button(multiline_button_lines, SCREEN_WIDTH // 2 - 640, SCREEN_HEIGHT // 2 + 100, size2x, size2y, bold_font, (0, 43, 128), (25, 217, 255))


        # Draw the third button (you can use create_button for this)
        multine_button_lines2 =["Ignore it"]
        create_multiline_button(multine_button_lines2, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 290, size3x, size3y, bold_font, (0, 43, 128), (25, 217, 255))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)  # 30 FPS

if __name__ == "__main__":
    # Initialize Pygame and set up the game window
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Safe Encounters - Button Screen")

    # Add any other initialization code here

    # Call the function that sets up and runs your button screen
    create_button_screen(current_character_position)  # You can pass any necessary parameters if needed

    # Quit Pygame when the screen is closed
    pygame.quit()
    sys.exit()
