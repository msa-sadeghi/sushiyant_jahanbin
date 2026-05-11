import pygame
import os
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, type, x, y, health, speed):
        super().__init__()
        self.type = type
        self.health = health
        self.speed = speed
        self.animation_types = os.listdir(f"{self.type}")
        self.all_images = {}
        for anim in self.animation_types:
            images = []
            n = len(os.listdir(f"{self.type}/{anim}"))
            for i in range(1, n + 1):
                img = pygame.image.load(f"{self.type}/{anim}/{anim} ({i}).png")
                img = pygame.transform.scale_by(img, 0.5)
                images.append(img)
            self.all_images[anim] = images

        self.frame_image = 0
        self.current_animation = "Idle"
        self.animation_time = 0
        self.image = self.all_images[self.current_animation][self.frame_image]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1
        self.yspeed = 0
        self.is_grounded = False

    def animation(self):
        if pygame.time.get_ticks() - self.animation_time > 100:
            self.animation_time = pygame.time.get_ticks()
            self.frame_image += 1
        if self.frame_image >= len(self.all_images[self.current_animation]):
            self.frame_image = 0
        self.image = self.all_images[self.current_animation][self.frame_image]

        if self.yspeed < 0:
            self.switch_animation("Jump")
        elif self.yspeed > 0 and not self.is_grounded:
            self.switch_animation("Fall")

    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.direction == -1, False)
        screen.blit(img, self.rect)

    def switch_animation(self, new_animation_name):
        if self.current_animation != new_animation_name:
            self.current_animation = new_animation_name
            self.frame_image = 0
            self.animation_time = 0
        self.image = self.all_images[self.current_animation][self.frame_image]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            self.direction = -1
            self.rect.x -= 7
            self.switch_animation("Walk")
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.rect.x += 7
            self.switch_animation("Walk")
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.switch_animation("Idle")
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.switch_animation("Idle")

    def move_y(self):
        dy = 0
        dy += self.yspeed
        self.yspeed += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.is_grounded:
            self.yspeed = -20
            self.is_grounded = False
        if self.rect.bottom + dy >= 640:
            self.yspeed = 0
            dy = 0
            self.is_grounded = True

        self.rect.y += dy
