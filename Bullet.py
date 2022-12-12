import pygame


class Bullet:
    DAMAGE = 40


class BulletRight(Bullet):
    BULLET_VELOCITY = 5.5

    def __init__(self, player) -> None:
        self.bullet = pygame.image.load(
            "images/bulletRight.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.bullet, (20, 10))
        self.bulletPos = [player.cordinates()[0] + 140,
                          player.cordinates()[1] + 65]  # 40
        self.x = self.bulletPos[0]
        self.y = self.bulletPos[1]
        self.hitbox = (self.x, self.y, 20, 10)

    def update(self) -> None:
        self.bulletPos[0] += self.BULLET_VELOCITY
        self.x = self.bulletPos[0]

    def __bool__(self):
        if self.bulletPos[0] > 800:
            return False
        return True

    def __getitem__(self, index):
        return self.bulletPos[index]

    def draw(self, screen):
        screen.blit(self.DISPLAY, self.bulletPos)
        self.hitbox = (self.x, self.y, 20, 10)


class BulletLeft(Bullet):
    BULLET_VELOCITY = - 5.5

    def __init__(self, player) -> None:
        self.bullet = pygame.image.load(
            "images/bulletLEFT.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.bullet, (20, 10))
        self.bulletPos = [player.cordinates()[0], player.cordinates()[1] + 65]
        self.x = self.bulletPos[0]
        self.y = self.bulletPos[1]
        self.hitbox = (self.x, self.y, 20, 10)

    def update(self) -> None:
        self.bulletPos[0] += self.BULLET_VELOCITY
        self.x = self.bulletPos[0]

    def __bool__(self):
        if self.bulletPos[0] < 0:
            return False
        return True

    def __getitem__(self, index):
        return self.bulletPos[index]

    def draw(self, screen):
        screen.blit(self.DISPLAY, self.bulletPos)
        self.hitbox = (self.x, self.y, 20, 10)
