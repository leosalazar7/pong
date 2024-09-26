import pygame
from constants import *

class Block(pygame.sprite.Sprite):

    def __init__(self, group, x, y, width, height, ruling):
        super().__init__(group)
        self.image = pygame.Surface((width, height))
        self.image.fill("white")
        if ruling == 1:
            self.rect = self.image.get_rect(topleft=(x, y))
        elif ruling == 2:
            self.rect = self.image.get_rect(topright=(x, y))
        else:
            self.rect = self.image.get_rect(center=(x, y))

    # def draw(self, screen):
    #     if self.type == 1:
    #         screen.blit(self.image, self.rect)
    #     else:

class Text(pygame.sprite.Sprite):

    def __init__(self, group, text, size, color, x, y, ruling):
        super().__init__(group)
        self.font = pygame.font.Font(None, size)
        self.text = text
        self.color = color
        self.image = self.font.render(text, True, color)
        if ruling == 1:
            self.rect = self.image.get_rect(topleft=(x, y))
        elif ruling == 2:
            self.rect = self.image.get_rect(topright=(x, y))
        else:
            self.rect = self.image.get_rect(center=(x, y))

class Button(Text):

    def __init__(self, group, text, size, color, x, y, ruling):
        super().__init__(group, text, size, color, x, y, ruling)
        self.hovered = False
        self.clicked = False

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

        self.updateColor()
        self.updateButton()

    def updateColor(self):
        if self.hovered:
            self.color = "blue"
        else:
            self.color = "white"

        if self.clicked:
            self.color = "lightblue"

    def updateButton(self):
        self.image = self.font.render(self.text, True, self.color)

class Player(Block):

    def __init__(self, group, x, y, width, height, ruling, num):
        super().__init__(group, x, y, width, height, ruling)
        self.player = num

    def update(self):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            self.p1Move(keys)
        elif self.player == 2:
            self.p2Move(keys)

        self.checkBorders()

    def p1Move(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5

    def p2Move(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def checkBorders(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_H:
            self.rect.bottom = SCREEN_H

class Ball(Block):

    def __init__(self, group, x, y, width, height, ruling):
        super().__init__(group, x, y, width, height, ruling)
        self.image = pygame.Surface((width, width), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (width//2, height//2), width//2)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        self.bounce()
        self.point()

    def bounce(self):
        if self.rect.top < 0:
            self.rect.top = 0
            self.dy *= -1
        if self.rect.bottom > SCREEN_H:
            self.rect.bottom = SCREEN_H
            self.dy *= -1

    def point(self):
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > SCREEN_W:
            self.kill()