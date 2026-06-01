import pygame
from pygame.sprite import Sprite
import os


class Enemy(Sprite):
    def __init__(self, type, x, y, lives, speed):
        super().__init__()
        self.type = type
        self.animation_types = ("Attack", "Dead", "Idle", "Walk")
        self.all_images = {}
        for anim in self.animation_types:
            imgs = []
            n = len(os.listdir(f"enemy_images/{type}/{anim}"))
            for i in range(1, n + 1):
                img = pygame.image.load(f"enemy_images/{type}/{anim}/{anim} ({i}).png")
                img = pygame.transform.scale_by(img, 0.3)
                imgs.append(img)

            self.all_images[anim] = imgs

        self.current_index = 0
        self.current_animation = "Walk"
        self.image = self.all_images[self.current_animation][self.current_index]
        self.last_animation_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.lives = lives
        self.speed = speed
        self.direction = 1
        self.turn_time = pygame.time.get_ticks()
        self.flip = False

    def animation(self):
        if pygame.time.get_ticks() - self.last_animation_time >= 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.current_index += 1
            if self.current_index >= len(self.all_images[self.current_animation]):
                self.current_index = 0
        img = self.all_images[self.current_animation][self.current_index]
        self.image = pygame.transform.flip(img, self.flip, False)

    def update(self, dt):
        
        self.rect.x += self.speed * self.direction * dt
        if pygame.time.get_ticks() - self.turn_time >= 2000:
            self.direction *= -1
            self.turn_time = pygame.time.get_ticks()
            self.flip = not self.flip

    def draw(self, screen, scroll_x):
        screen.blit(self.image, (self.rect.x - scroll_x, self.rect.y))
        self.animation()
