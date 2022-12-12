import pygame


class Zombie:
    HEALTH = 70
    zombiePos = []
    SPEED = 0.8
    DAMAGE = 0.65

    def __bool__(self):
        return self.HEALTH > 0


class ZombieLeft(Zombie):

    def __init__(self) -> None:
        self.zombieL = pygame.image.load(
            "images/zombieLeft.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.zombieL, (150, 150))
        self.zombiePos = [750, 200]
        self.x = self.zombiePos[0]
        self.y = self.zombiePos[1]
        self.hitbox = (self.x + 40, self.y, 65, 150)

    def update(self) -> None:
        self.zombiePos[0] -= self.SPEED
        self.x = self.zombiePos[0]

    def __getitem__(self, index):
        return self.zombiePos[index] + 15

    def draw(self, screen):
        screen.blit(self.DISPLAY, self.zombiePos)
        self.hitbox = (self.x + 40, self.y, 65, 150)
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x + 40, self.y - 20, 70, 10))
        if self.HEALTH >= 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.x +
                             40, self.y - 20, self.HEALTH, 10))


class ZombieRight(Zombie):

    def __init__(self) -> None:
        self.zombieR = pygame.image.load(
            "images/zombieRight.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.zombieR, (150, 150))
        self.zombiePos = [-100, 200]
        self.x = self.zombiePos[0]
        self.y = self.zombiePos[1]
        self.hitbox = (self.x + 45, self.y, 70, 150)

    def update(self) -> None:
        self.zombiePos[0] += self.SPEED
        self.x = self.zombiePos[0]

    def __getitem__(self, index):
        return self.zombiePos[index] + 100

    def draw(self, screen):
        screen.blit(self.DISPLAY, self.zombiePos)
        self.hitbox = (self.x + 45, self.y, 70, 150)
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x + 43, self.y - 20, 70, 10))
        if self.HEALTH >= 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.x +
                             43, self.y - 20, self.HEALTH, 10))
