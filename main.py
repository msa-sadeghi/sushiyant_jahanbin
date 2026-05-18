import pygame
from player import Player
from enemy import Enemy

pygame.init()

WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_player = Player("dog", 100, 200, 3, 4)

enemy_group = pygame.sprite.Group()
enemy1 = Enemy("female_zombie", WIDTH - 400, 460, 5, 2)
enemy2 = Enemy("male_zombie", WIDTH - 100, 460, 5, 2)
enemy_group.add(enemy1)
enemy_group.add(enemy2)
FPS = 60
clock = pygame.time.Clock()
scroll_x = 0
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((255, 255, 255))
    scroll_x = my_player.rect.centerx - WIDTH // 2
    screen.fill("lightblue")
    my_player.draw(screen, scroll_x)
    my_player.move()
    my_player.move_y()
    my_player.slide()
    my_player.animation()
    for enemy in enemy_group:
        enemy.draw(screen, scroll_x)
    enemy_group.update()
    pygame.display.update()

    clock.tick(FPS)
