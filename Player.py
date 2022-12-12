import pygame


class Player:

    def __init__(self) -> None:
        self.playerRightGun = pygame.image.load(
            "images/playerRight.png").convert_alpha()
        self.playerRightGun = pygame.transform.scale(
            self.playerRightGun, (150, 150))

        self.playerRightRocket = pygame.image.load(
            "images/playerRightRocket.png").convert_alpha()
        self.playerRightRocket = pygame.transform.scale(
            self.playerRightRocket, (150, 150))

        self.playerRightKnife = pygame.image.load(
            "images/playerRightKnife.png").convert_alpha()
        self.playerRightKnife = pygame.transform.scale(
            self.playerRightKnife, (150, 150))

        self.playerLeftGun = pygame.image.load(
            "images/playerLeft.png").convert_alpha()
        self.playerLeftGun = pygame.transform.scale(
            self.playerLeftGun, (150, 150))

        self.playerLeftRocket = pygame.image.load(
            "images/playerLeftRocket.png").convert_alpha()
        self.playerLeftRocket = pygame.transform.scale(
            self.playerLeftRocket, (150, 150))

        self.playerLeftKnife = pygame.image.load(
            "images/playerLeftKnife.png").convert_alpha()
        self.playerLeftKnife = pygame.transform.scale(
            self.playerLeftKnife, (150, 150))

        self.DISPLAY = self.playerRightKnife
        self.RIGHT = True
        self.JUMPING = False
        self.KEYS = [False, False]
        self.playerPos = [50, 200]
        self.x = self.playerPos[0]
        self.y = self.playerPos[1]
        self.HEALTH = 210
        self.hitbox = (self.x + 40, self.y, 70, 150)
        self.KNIFE = True
        self.ROCKET = False
        self.GUN = False
        self.DAMAGE = 25
        self.LOCKED = ['gun', 'rocket']

    def __getitem__(self, index):
        return self.playerPos[index]

    def left(self) -> None:
        self.RIGHT = False
        if self.KNIFE:
            self.DISPLAY = self.playerLeftKnife
        elif self.GUN:
            self.DISPLAY = self.playerLeftGun
        else:
            self.DISPLAY = self.playerLeftRocket

    def right(self) -> None:
        self.RIGHT = True
        if self.KNIFE:
            self.DISPLAY = self.playerRightKnife
        elif self.GUN:
            self.DISPLAY = self.playerRightGun
        else:
            self.DISPLAY = self.playerRightRocket

    def knife(self) -> None:
        self.ROCKET = False
        self.GUN = False
        self.KNIFE = True
        if self.RIGHT:
            self.DISPLAY = self.playerRightKnife
        else:
            self.DISPLAY = self.playerLeftKnife

    def rocket(self) -> None:
        self.ROCKET = True
        self.GUN = False
        self.KNIFE = False
        if self.RIGHT:
            self.DISPLAY = self.playerRightRocket
        else:
            self.DISPLAY = self.playerLeftRocket

    def gun(self) -> None:
        self.ROCKET = False
        self.GUN = True
        self.KNIFE = False
        if self.RIGHT:
            self.DISPLAY = self.playerRightGun
        else:
            self.DISPLAY = self.playerLeftGun

    def cordinates(self) -> list:
        return self.playerPos

    def display(self):
        return self.DISPLAY

    def jumping(self) -> bool:
        return self.JUMPING

    def keys(self) -> list:
        return self.KEYS

    def setKey(self, index, val) -> None:
        self.KEYS[index] = val

    def direction(self) -> bool:
        return self.RIGHT

    def moveX(self, val) -> None:
        self.playerPos[0] += val
        self.x = self.playerPos[0]

    def moveY(self, val) -> None:
        self.playerPos[1] += val
        self.y = self.playerPos[1]

    def draw(self, screen):
        screen.blit(self.display(), self.cordinates())
        self.hitbox = (self.x + 40, self.y, 70, 150)

        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x + 40, self.y + 170, 70, 10))
        if self.HEALTH >= 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.x + 40,
                             self.y + 170, self.HEALTH / 3, 10))
