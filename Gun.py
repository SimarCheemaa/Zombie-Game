import pygame


class Gun:
    BULLETS = 0
    LOCKED = True

    def __init__(self) -> None:
        self.gunImage = pygame.image.load("images/gun.png").convert_alpha()
        self.DISPLAY = pygame.transform.scale(self.gunImage, (100, 40))

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 235, 255), (30, 420, 60, 50))

        screen.blit(self.DISPLAY, (30, 420))
        if self.LOCKED:
            pygame.draw.rect(screen, (255, 0, 0), (30, 420, 60, 50), 2)
        else:
            pygame.draw.rect(screen, (0, 255, 0), (30, 420, 60, 50), 2)
