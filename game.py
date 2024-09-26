import pygame
from classes import *
from constants import *

def game(screen, clock):

    running = True

    all_sprites = pygame.sprite.Group()
    Player(all_sprites, SCREEN_W//10, SCREEN_H//2, 20, 80, 3, 1)
    Player(all_sprites, SCREEN_W*9//10, SCREEN_H//2, 20, 80, 3, 2)
    Block(all_sprites, SCREEN_W//2, 0, 1, SCREEN_H, 1)
    Ball(all_sprites, SCREEN_W//2, SCREEN_H//2, 20, 20, 3)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()