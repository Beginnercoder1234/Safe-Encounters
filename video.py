import os
import pygame
import sys
from time import *
#from pyvidplayer2 import Video
import moviepy.editor
#import pygame.movie

#path = r"C:\Users\ishaa\OneDrive\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
#os.chdir(path)

pygame.init()
pygame.display.init()
#moviepy.Initialize()
SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 810
#information font
screen = pygame.display.set_mode((SCREEN_WIDTH // 2, SCREEN_HEIGHT //2))
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

#video_screen = pygame.Surface((video.get_size()))
#video.set_display(video_screen)
#video.play()
#vid = Video("actual_render1.mp4")

#win = pygame.display.set_mode(screen)
#pygame.display.set_caption(vid.name)


def create_video_slide(screen):
    pygame.init()
    pygame.display.init()
    clock = pygame.time.Clock()
    #vid = Video("actual_render.mp4")
    #vid.set_size((720, 405))
    # Load the image for the second slide
    second_slide_image = pygame.image.load("background.jpg")  # Replace with the actual image file name
    second_slide_image = pygame.transform.scale(second_slide_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #original_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 80)
    #next_button_rect = original_button_rect.copy()
    
    
    # Define the semi-transparent white color with reduced alpha value
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #vid.close()
                pygame.quit()
                sys.exit()
              # Replace with your function to create the next screen
        #screen.blit(video_screen, (0, 0))
        #vid.draw(screen, (0,0))
        pygame.display.update()
        #pygame.display.flip()
        #pygame.time.delay(30)
        #video_path = "actual_render.mp4"  # Replace with the path to your video file
        #video = moviepy.editor.VideoFileClip(video_path)
        #video.preview()
        
        # Draw the background image
        screen.blit(second_slide_image, (0, 0))  # Use the passed background_image
        #draw the button
        
        

        # Draw the image for the second slide
        screen.blit(second_slide_image, (0, 0))
        
        
        # Draw any other content you want for the second slide
        #text
        y_position = 100
        x_position = 150
        
        #Next Button
        
        
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)  # 30 FPS
        pygame.quit()