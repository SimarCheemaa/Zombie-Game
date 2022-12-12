import pygame


class Rocket:
    BULLETS = 0
    LOCKED = True
    DAMAGE = 100

    def __init__(self) -> None:
        self.rocketImage = pygame.image.load(
            "images/rocket.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.rocketImage, (80, 40))

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 235, 255), (100, 420, 90, 50))

        screen.blit(self.DISPLAY, (105, 420))
        if self.LOCKED:
            pygame.draw.rect(screen, (255, 0, 0), (100, 420, 90, 50), 2)
        else:
            pygame.draw.rect(screen, (0, 255, 0), (100, 420, 90, 50), 2)


class RocketRight(Rocket):

    ROCKET_VELOCITY = 6.5

    def __init__(self, player) -> None:
        self.rocket = pygame.image.load(
            "images/rocketRight.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.rocket, (60, 30))
        self.rocketPos = [player.cordinates()[0] + 140,
                          player.cordinates()[1] + 74]
        self.x = self.rocketPos[0]
        self.y = self.rocketPos[1]
        self.hitbox = (self.x, self.y, 30, 15)

    def update(self) -> None:
        self.rocketPos[0] += self.ROCKET_VELOCITY
        self.x = self.rocketPos[0]

    def __bool__(self):
        if self.rocketPos[0] > 800:
            return False
        return True

    def __getitem__(self, index):
        return self.rocketPos[index]

    def draw(self, screen):
        screen.blit(self.DISPLAY, self.rocketPos)
        self.hitbox = (self.x, self.y, 30, 15)


class RocketLeft(Rocket):

    ROCKET_VELOCITY = -6.5

    def __init__(self, player) -> None:
        self.rocket = pygame.image.load(
            "images/rocketLeft.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.rocket, (60, 30))
        self.rocketPos = [player.cordinates()[0] - 40,
                          player.cordinates()[1] + 74]
        self.x = self.rocketPos[0]
        self.y = self.rocketPos[1]
        self.hitbox = (self.x, self.y, 30, 15)

    def update(self) -> None:
        self.rocketPos[0] += self.ROCKET_VELOCITY
        self.x = self.rocketPos[0]

    def __bool__(self):
        if self.rocketPos[0] > 800:
            return False
        return True

    def __getitem__(self, index):
        return self.rocketPos[index]

    def draw(self, screen):
        screen.blit(self.DISPLAY, self.rocketPos)
        self.hitbox = (self.x, self.y, 30, 15)
