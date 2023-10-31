import pygame
import sys

pygame.init()

# Set up the Pygame window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wrong Animation Test")

class Wrong(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = True  # Start the animation automatically
        self.scale = 0.5  # Initial scale
        self.speed = 0.7  # Initial animation speed
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
wrong = Wrong(200, 100)
wrong_sprites.add(wrong)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update and draw the wrong animation
    wrong_sprites.update()
    wrong_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)  # 30 FPS

pygame.quit()
sys.exit()
