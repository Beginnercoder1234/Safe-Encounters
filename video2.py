import pygame
from pyvidplayer2 import Video
import os

path = r"C:\Users\ishaa\OneDrive\Videos\MInecraftclips\Python\SafeEncountrs\Media\backups"
os.chdir(path)

# Create video object
vid = Video("actual_render1.mp4")

# Set up the Pygame display to a 1440x2560 screen (9:16 aspect ratio)
screen = pygame.display.set_mode((1440, 840))
pygame.display.set_caption(vid.name)

# Calculate the dimensions for the smaller rectangle to maintain the 9:16 aspect ratio
video_width = 400  # Adjust this width as needed
video_height = 711 # Calculate height to maintain 9:16 aspect ratio

# Position the video rectangle in the center of the screen
video_x = (1440 - video_width) // 2  # Center the video horizontally
video_y = (840 - video_height) // 2  # Center the video vertically

# Position the video rectangle in the center of the screen
#ideo_x = 360  # Adjust the x-coordinate as needed
#video_y = 100  # Adjust the y-coordinate as needed
size = (video_width, video_height)  # Adjust the width as needed, and 0 for maintaining aspect ratio

# Resize the video

# Define the video rectangle with the new position
video_rect = pygame.Rect(video_x, video_y, video_width, video_height)
vid.resize(size)
while vid.active:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vid.stop()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)

    if key == "r":
        vid.restart()  # Rewind video to the beginning
    elif key == "p":
        vid.toggle_pause()  # Pause/plays video
    elif key == "m":
        vid.toggle_mute()  # Mutes/unmutes video
    elif key == "right":
        vid.seek(15)  # Skip 15 seconds in the video
    elif key == "left":
        vid.seek(-15)  # Rewind 15 seconds in the video
    elif key == "up":
        vid.set_volume(1.0)  # Max volume
    elif key == "down":
        vid.set_volume(0.0)  # Min volume
    elif key == "1":
        vid.set_speed(1.0)  # Regular playback speed
    elif key == "2":
        vid.set_speed(2.0)  # Doubles video speed

    # Draw the video within the smaller rectangle
    vid.draw(screen, video_rect.topleft, force_draw=False)

    pygame.display.update()

    pygame.time.wait(16)  # Around 60 fps

# Close the video when done
#vid.close()
pygame.quit()
