import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,type, x,y, lives, speed):
        super().__init__()
        self.type = type
        self.image = pygame.image.load(f"enemy_images/female_zombie/Idle/Idle (1).png")
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.lives = lives
        self.speed = speed
        self.direction = 1
        self.turn_time = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speed * self.direction
        if pygame.time.get_ticks() - self.turn_time >= 2000:
            self.direction *= -1
            self.turn_time = pygame.time.get_ticks()
            self.image = pygame.transform.flip(self.image, True, False)

