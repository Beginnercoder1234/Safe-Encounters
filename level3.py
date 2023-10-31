import pygame
import sys
import assets  # Import the asset loading functions from assets.py
from text_animation import *
#from button_screen import create_button_screen
from MAIN1 import create_button
from MAIN1 import create_multiline_button
from pygame import mixer
from final import create_second_slide

#from video2 import create_video_slide

pygame.init()
mixer.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Safe Encounters - Fourth Screen")

# Load background image and character image using the asset loading functions
room_image = assets.load_background_image("fakkk copy.jpg", SCREEN_WIDTH, SCREEN_HEIGHT)
background_image = pygame.image.load("fakkk copy.jpg")
#character_image = assets.load_character_image("character.png", 500, 700)
#character_width = 500  # Width of the character image
#character_height = 700
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = True  # Start the animation automatically
        self.scale = 12  # Initial scale
        self.speed = 0.2  # Initial animation speed
        self.sprites = [pygame.image.load('tile000.png'),
                       pygame.image.load('tile001.png'),
                       pygame.image.load('tile002.png'),
                       pygame.image.load('tile003.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
            self.current_sprite += self.speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
            self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)], (int(self.rect.width * self.scale), int(self.rect.height * self.scale)))

moving_sprites = pygame.sprite.Group()
player = Player(40, -50)
moving_sprites.add(player)
class Wrong(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = True  # Start the animation automatically
        self.scale = 0.9  # Initial scale
        self.speed = 0.33  # Initial animation speed
        self.sprites = [pygame.image.load('frame0.png'),
                       pygame.image.load('frame1.png'),
                       pygame.image.load('frame2.png'),
                       pygame.image.load('frame3.png'),
                       pygame.image.load('frame4.png'),
                       pygame.image.load('frame5.png'),
                       pygame.image.load('frame6.png'),
                       pygame.image.load('frame7.png'),
                       pygame.image.load('frame8.png'),
                       pygame.image.load('frame9.png'),
                       pygame.image.load('frame10.png'),
                       pygame.image.load('frame11.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
            self.current_sprite += self.speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
            self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)], (int(self.rect.width * self.scale), int(self.rect.height * self.scale)))

wrong_sprites = pygame.sprite.Group()
wrong = Wrong(555,0)
wrong_sprites.add(wrong)
class Right(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = True  # Start the animation automatically
        self.scale = 3  # Initial scale
        self.speed = 0.5  # Initial animation speed
        self.sprites = [pygame.image.load('check_00.png'),
                       pygame.image.load('check_01.png'),
                       pygame.image.load('check_02.png'),
                       pygame.image.load('check_03.png'),
                       pygame.image.load('check_04.png'),
                       pygame.image.load('check_05.png'),
                       pygame.image.load('check_06.png'),
                       pygame.image.load('check_07.png'),
                       pygame.image.load('check_08.png'),
                       pygame.image.load('check_09.png'),
                       pygame.image.load('check_10.png'),
                       pygame.image.load('check_12.png'),
                       pygame.image.load('check_13.png'),
                       pygame.image.load('check_14.png'),
                       pygame.image.load('check_15.png'),
                       pygame.image.load('check_16.png'),
                       pygame.image.load('check_17.png'),
                       pygame.image.load('check_18.png'),
                       pygame.image.load('check_19.png'),
                       pygame.image.load('check_20.png'),
                       pygame.image.load('check_21.png'),
                       pygame.image.load('check_22.png'),
                       pygame.image.load('check_23.png'),
                       pygame.image.load('check_24.png'),
                       pygame.image.load('check_25.png'),
                       pygame.image.load('check_26.png'),
                       pygame.image.load('check_27.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
            self.current_sprite += self.speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
            self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)], (int(self.rect.width * self.scale), int(self.rect.height * self.scale)))

right_sprites = pygame.sprite.Group()
right = Right(520,70)
right_sprites.add(right)
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

music_paused = False
#button_screen variables
size1x=452
size1y=160
size2x=536
size2y=160
size3x=499
size3y=160
bold_font = pygame.font.Font("BOLDFONT.ttf", 75)
button1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 570, SCREEN_HEIGHT // 2 + 30, size2x, size2y)
button2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 220, SCREEN_HEIGHT // 2 + 200, size3x, size3y)
button3_rect = pygame.Rect(SCREEN_WIDTH // 2 +100, SCREEN_HEIGHT // 2 + 30, size1x, size1y)
current_screen = "button_screen"


def create_level_3():
    clock = pygame.time.Clock()
    global music_paused
    text_animation_complete = False
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if music_rect.collidepoint(x, y):
                        if music_paused:
                            mixer.Channel(3).unpause()
                            music_paused = False
                        else:
                            mixer.Channel(3).pause()
                            music_paused = True

                    # Check if the user clicked on the arrow
                    if arrow_rect.collidepoint(x, y):
                        mixer.music.set_volume(0.3)
                        mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                        create_button_screen()
                        pass
        

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the background image and character
        screen.blit(background_image, (0, 0))
        #screen.blit(character_image, (SCREEN_WIDTH // 5 - character_width // 2, SCREEN_HEIGHT - character_height - 20))
        #moving_sprites.update()
        #moving_sprites.draw(screen)
        # Draw the arrow image
        screen.blit(arrow_image, arrow_position)
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
        # Draw the text box
        pygame.draw.rect(screen, (0, 0, 0), text_box)
        # Add text content to the text box
        text = [
            "In this level you stumble upon a surprising and",
            "potentially hazardous discovery while playing ",
            "outdoors. You find a firearm concealed by a pile",
            "of leaves. Now, you need to figure out what to do  ",
            "next to ensure your saftey"
        ]
        y_offset = 0
        x_position = text_box.x + 10
        y_position = text_box.y + 10
        if not text_animation_complete:
            display_text_animation_with_color(text, screen, text_font, x_position, y_position, text_color)
            text_animation_complete = True  # Mark the text animation as complete

        # Check if the text animation is complete before drawing the button
        if text_animation_complete:
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

#button screen code
def create_button_screen():
    global current_screen
    global music_paused
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
                    if music_rect.collidepoint(x, y):
                        if music_paused:
                            mixer.Channel(3).unpause()
                            music_paused = False
                        else:
                            mixer.Channel(3).pause()
                            music_paused = True
                    #print (mouse_position)
                    #print(x)
                    #print(y)
                    # Check if the user clicked on the buttons
                    #button3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 120, SCREEN_HEIGHT // 2 + 100, size3x, size3y)
                if button3_rect.collidepoint(x,y): #SCREEN_WIDTH // 2 - - 120, SCREEN_HEIGHT // 2 + 100):
                        mixer.music.set_volume(0.4)
                        mixer.Channel(1).play(pygame.mixer.Sound('right_choice.mp3'))
                        mixer.Channel(2).play(pygame.mixer.Sound('right.mp3'),-1)
                        current_screen = show_right_choice_content(screen)  # Transition to the right choice screen
                        #print(SCREEN_WIDTH)
                        #print(SCREEN_WIDTH // 2 - - 120)
                        #print(SCREEN_HEIGHT)
                        #print(SCREEN_HEIGHT // 2 + 100)
                        #print("button is being pressed")
                elif button2_rect.collidepoint(mouse_position):  #SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 290):
                        mixer.music.set_volume(0.5)
                        mixer.Channel(1).play(pygame.mixer.Sound('wrong.mp3'),-1)
                        current_screen = show_wrong_choice_content(screen)  # Transition to the wrong choice content screen
                        #print("button is being pressed2")
                elif button1_rect.collidepoint(mouse_position):#SCREEN_WIDTH // 2 - 640, SCREEN_HEIGHT // 2 + 100):
                        mixer.music.set_volume(0.5)
                        mixer.Channel(1).play(pygame.mixer.Sound('wrong.mp3'),-1)
                        current_screen = show_wrong_choice_2_content(screen)
                        #print("button is being pressed3")  # Transition to the wrong choice 2 content screen

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the background room image and character
        screen.blit(background_image, (0, 0))
        #moving_sprites.update()
        #moving_sprites.draw(screen)
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
        multiline_button_lines1 = ["Call the", "authorities"]
        button_1=create_multiline_button(multiline_button_lines1, SCREEN_WIDTH // 2 +100, SCREEN_HEIGHT // 2 + 30, size1x, size1y, bold_font, (45,232,86), (255,200,50))


        # Use create_multiline_button to create a multiline button
        multiline_button_lines = ["Gently cover", "it"]  # Define the lines of text for the multiline button
        button_2=create_multiline_button(multiline_button_lines, SCREEN_WIDTH // 2 - 570, SCREEN_HEIGHT // 2 + 30, size2x, size2y, bold_font, (45,232,86), (255,200,50))


        # Draw the third button (you can use create_button for this)
        multine_button_lines2 =["Post to", "social media"]
        button_3=create_multiline_button(multine_button_lines2, SCREEN_WIDTH // 2 - 220, SCREEN_HEIGHT // 2 + 200, size3x, size3y, bold_font, (45,232,86), (255,200,50))
        #print("3")
        #print(button_1.width, button_1.height)
        #print(button_2.width, button_2.height)
        #print(button_3.width, button_3.height)
        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)  # 30 FPS

def show_right_choice_content(screen):
    loop_counter=0
    global music_paused
    # Define the content for the right answer here
    text_animation_complete = False
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Define the text and font
    text_lines = [
        "You take quick and responsible action by dialing the local",
        "authorities. By taking this step, you're ensuring that",
        "professionals with the expertise to handle firearms safely",
        "and conduct a thorough investigation will promptly address",
        "the situation. ",
        
    ]   
    
    text_box = pygame.Rect(120, 475, 1200, 300)
    text_color = (255, 255, 255)  # White
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 25)
    
    # Create the arrow image
    arrow_width = 120
    arrow_height = 120
    arrow_image = pygame.image.load("arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (arrow_width, arrow_height))
    arrow_position = (1100, 650)
    arrow_rect = pygame.Rect(arrow_position[0], arrow_position[1], arrow_width, arrow_height)
    # Event loop for this screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        # Check if the user clicked on the arrow
                        if arrow_rect.collidepoint(x, y):
                            mixer.Channel(2).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                            create_second_slide(screen, background_image)
                            
                            pass
                        if music_rect.collidepoint(x, y):
                            if music_paused:
                                mixer.Channel(3).unpause()
                                music_paused = False
                            else:
                                mixer.Channel(3).pause()
                                music_paused = True
        # Clear the screen
        screen.blit(background_image, (0, 0))
        right.update()
        right_sprites.draw(screen)
        loop_counter=loop_counter + 1
        # Draw the text box
        pygame.draw.rect(screen, BLACK, text_box)
        pygame.draw.rect(screen, WHITE, text_box, 3)
        screen.blit(arrow_image, arrow_position)
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
        # Display the text lines
        if loop_counter > 35:
            y_offset = 0
            x_position = 150
            y_position = 480
            if not text_animation_complete:
                display_text_animation_with_right(text_lines, screen, text_font, x_position, y_position, text_color)
                text_animation_complete = True  # Mark the text animation as complete
             # Check if the text animation is complete before drawing the button
            if text_animation_complete:
                for line in text_lines:
                    text_surface = text_font.render(line, True, text_color)
                    screen.blit(text_surface, (x_position + 10, y_position + 10 + y_offset))
                    y_offset += text_surface.get_height()
        
        # Update the display
        pygame.display.flip()
    
    # You can add logic here to move on to the next screen or level
    
    # Return control to the main game loop
    return

def show_wrong_choice_content(screen):
    loop_counter=0
    global music_paused
    # Define the content for the wrong answer here
    text_animation_complete = False
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Define the text and font
    text_lines = [
        "Your decision is to share the discovery of the firearm on ",
        "your social media account. This choice is not the best one.",
        "Posting about the firearm on social media may not be ,", 
        "responsible as it could encourage unsafe actions or cause",
        "unnecessary fear among those who see the post. Safety is the",
        "top priority, and the best way to ensure it is by informing",
        "trusted adults or the authorities. ",
        
        
    ]
    
    text_box = pygame.Rect(120, 475, 1200, 300)
    text_color = (255, 255, 255)  # White
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 27)
    
    # Create the arrow image
    arrow_width = 120
    arrow_height = 55
    arrow_image = pygame.image.load("arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (arrow_width, arrow_height))
    arrow_position = (1100, 710)
    arrow_rect = pygame.Rect(arrow_position[0], arrow_position[1], arrow_width, arrow_height)
    # Event loop for this screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos

                    # Check if the user clicked on the arrow
                    if arrow_rect.collidepoint(x, y):
                        mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                        create_button_screen()
                        pass
                    if music_rect.collidepoint(x, y):
                        if music_paused:
                            mixer.Channel(3).unpause()
                            music_paused = False
                        else:
                            mixer.Channel(3).pause()
                            music_paused = True
        
        # Clear the screen
        screen.blit(background_image, (0, 0))
        wrong.update()
        wrong_sprites.draw(screen)
        loop_counter=loop_counter + 1
        # Draw the text box
        pygame.draw.rect(screen, BLACK, text_box)
        pygame.draw.rect(screen, WHITE, text_box, 3)
        screen.blit(arrow_image, arrow_position)
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
        # Display the text lines
        y_offset = 0
        x_position = 150
        y_position = 480
        if loop_counter > 53:
            y_offset = 0
            x_position = 150
            y_position = 480
            if not text_animation_complete:
                display_text_animation_with_color(text_lines, screen, text_font, x_position, y_position, text_color)
                text_animation_complete = True  # Mark the text animation as complete
             # Check if the text animation is complete before drawing the button
            if text_animation_complete:
                for line in text_lines:
                    text_surface = text_font.render(line, True, text_color)
                    screen.blit(text_surface, (x_position + 10, y_position + 10 + y_offset))
                    y_offset += text_surface.get_height()
            
            
        
        # Update the display
        pygame.display.flip()
    
    # You can add logic here to allow the player to try again
    
    # Return control to the main game loop
    return

def show_wrong_choice_2_content(screen):
    # Define the content for the second wrong answer here
    loop_counter=0
    global music_paused
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    text_animation_complete = False
    # Define the text and font
    text_lines = [
        "Hiding the firearm is a way to make it less visible and",
        "prevent accidents.However, in this case, it's not the best",
        "choice. Keeping the gun hidden without telling authorities", 
        "handle it safely. Safety comes first, so it's better to ",
        "involve experts who can deal with firearms properly.",
    ]
    
    text_box = pygame.Rect(120, 475, 1200, 300)
    text_color = (255, 255, 255)  # White
    text_font = pygame.font.SysFont("LEMONMILK-Medium", 25)
    
    # Create the arrow image
    arrow_width = 120
    arrow_height = 55
    arrow_image = pygame.image.load("arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (arrow_width, arrow_height))
    arrow_position = (1100, 710)
    arrow_rect = pygame.Rect(arrow_position[0], arrow_position[1], arrow_width, arrow_height)
    
    # Event loop for this screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        # Check if the user clicked on the arrow
                        if arrow_rect.collidepoint(x, y):
                            mixer.Channel(1).play(pygame.mixer.Sound('whoosh_V1.mp3'))
                            create_button_screen()
                            pass
                        if music_rect.collidepoint(x, y):
                            if music_paused:
                                mixer.Channel(3).unpause()
                                music_paused = False
                            else:
                                mixer.Channel(3).pause()
                                music_paused = True
        
        # Clear the screen
        screen.blit(background_image, (0, 0))
        wrong.update()
        wrong_sprites.draw(screen)
        loop_counter=loop_counter + 1
        # Draw the text box
        pygame.draw.rect(screen, BLACK, text_box)
        pygame.draw.rect(screen, WHITE, text_box, 3)
        screen.blit(arrow_image, arrow_position)
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
        # Display the text lines
        if loop_counter > 53:
            y_offset = 0
            x_position = 150
            y_position = 480
            if not text_animation_complete:
                display_text_animation_with_color(text_lines, screen, text_font, x_position, y_position, text_color)
                text_animation_complete = True  # Mark the text animation as complete
             # Check if the text animation is complete before drawing the button
            if text_animation_complete:
                for line in text_lines:
                    text_surface = text_font.render(line, True, text_color)
                    screen.blit(text_surface, (x_position + 10, y_position + 10 + y_offset))
                    y_offset += text_surface.get_height()
        
        # Update the display
        pygame.display.flip()
    
    # You can add logic here to allow the player to try again
    
    # Return control to the main game loop
    return



if __name__ == "__main__":
    create_level_3()
