import pygame
from old.player import Player
from old.enemy import Enemy

pygame.init()

WIDTH = 1000
MAP_WIDTH = 3000
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
    dt = clock.tick(FPS) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((255, 255, 255))
    scroll_x = my_player.rect.centerx - WIDTH // 2
    scroll_x = max(0, scroll_x)
    scroll_x = min(MAP_WIDTH - WIDTH , scroll_x)
    screen.fill("lightblue")
    pygame.draw.rect(
        screen,
        (50, 180,50),
        (0, HEIGHT - 40, WIDTH, 40)
    )
    my_player.draw(screen, scroll_x)
    my_player.move()
    my_player.move_y()
    my_player.slide()
    my_player.animation()
    for enemy in enemy_group:
        enemy.draw(screen, scroll_x)
    enemy_group.update(dt)
    pygame.display.update()

