import pygame
import random


class Bird:
    HEALTH = 50
    SPEED = 3

    def __init__(self) -> None:
        self.left = pygame.image.load("images/birdLeft.png").convert_alpha()
        self.left = pygame.transform.scale(self.left, (100, 100))
        self.right = pygame.image.load("images/birdRight.png").convert_alpha()
        self.right = pygame.transform.scale(self.right, (100, 100))
        self.choice = random.choice([0, 1])
        self.DISPLAY = (self.right, self.left)[self.choice]

        if not self.choice:
            self.x = -100
            self.direction = True
        else:
            self.x = 800
            self.direction = False
        self.y = 50
        self.hitbox = (self.x, self.y, 100, 100)

    def draw(self, screen):
        screen.blit(self.DISPLAY, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)

    def update(self):
        if self.direction:
            self.x += self.SPEED
        else:
            self.x -= self.SPEED

    def __bool__(self):
        return self.HEALTH > 0
