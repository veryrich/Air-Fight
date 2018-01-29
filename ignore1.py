import pygame
from plane_sprite import GameSprite
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((480, 752), 0, 32)
pygame.display.set_caption("plane fight")

background = pygame.image.load('./image/background.png')
screen.blit(background, (0, 0))

hero = pygame.image.load("./image/hero1.png")
screen.blit(hero,(200, 600))

pygame.display.update()

clock = pygame.time.Clock()

hert_rect = pygame.Rect(200, 600, 100, 124)

enemy = GameSprite("./image/enemy0.png")
enemy1 = GameSprite("./image/enemy0.png", 2)

enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    #游戏主循环
    clock.tick(60)
    hert_rect.y -= 1

    if hert_rect.y <= -124:
        hert_rect.y = 752

    screen.blit(background, (0, 0))
    screen.blit(hero, hert_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
