import pygame
from classes import *
from constants import *
from game import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
Text(all_sprites, "Pong", 100, "white", SCREEN_W//2, SCREEN_H//4, 3)

buttons = pygame.sprite.Group()
start = Button(all_sprites, "Play", 60, "white", SCREEN_W//2, SCREEN_H*3//4, 3)
buttons.add(start)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        buttons.update(event)

    screen.fill("black")

    all_sprites.draw(screen)

    if start.clicked:
        game(screen, clock)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()