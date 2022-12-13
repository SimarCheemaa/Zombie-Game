# Import library
import pygame
from pygame.locals import *
import random
import sys
import time
# Pygame module imports
from Bullet import *
from Zombie import *
from Rocket import *
from Gun import *
from Player import Player
from Bird import Bird

# Initialize the game
pygame.init()
CLOCK = pygame.time.Clock()
width, height = 800, 550
display = pygame.display
display.set_caption('Zombie Game')
clock = pygame.time.Clock()
screen = display.set_mode((width, height))
background = pygame.image.load("images/background.png").convert()
backgroundBlur = pygame.image.load("images/backgroundBlur.png").convert()
explosion = pygame.image.load("images/explosion.png").convert_alpha()
explosion = pygame.transform.scale(explosion, (80, 80))

# Initialize player object
player = Player()

# Helper Functions


def start_game(screen, player, backgroundBlur):
    font = pygame.font.SysFont(pygame.font.get_fonts()[-1], 50)
    while True:
        screen.fill(0)
        screen.blit(backgroundBlur, (0, 0))
        pygame.draw.rect(screen, (100, 100, 100), (0, 400, 800, 150))
        startText = font.render("Tap anywhere to Start", True, (0, 0, 0))
        startText2 = font.render("Press Q to quit", True, (0, 0, 0))
        screen.blit(startText, (400 - startText.get_width()/2, 50))
        screen.blit(startText2, (400 - startText2.get_width()/2, 120))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONUP:
                run(player)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()


def game_over(screen, POINTS, zombie_count):
    font = pygame.font.SysFont(pygame.font.get_fonts()[-1], 50)
    game_over_text = font.render("Game Over", True, (240, 248, 255))
    score_text = font.render(f"Points: {POINTS}", True, (240, 248, 255))
    zombie_text = font.render(
        f"Zombies Killed: {zombie_count}", True, (240, 248, 255))
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, (400 - game_over_text.get_width()/2, 50))
    screen.blit(score_text, (400 - score_text.get_width()/2, 100))
    screen.blit(zombie_text, (400 - zombie_text.get_width()/2, 150))
    pygame.display.update()
    time.sleep(4)
    player = Player()
    while True:
        screen.fill(0)
        screen.blit(backgroundBlur, (0, 0))
        pygame.draw.rect(screen, (100, 100, 100), (0, 400, 800, 150))
        startText = font.render("Tap anywhere to Restart", True, (0, 0, 0))
        startText2 = font.render("Press Q to Quit", True, (0, 0, 0))
        screen.blit(startText, (400 - startText.get_width()/2, 50))
        screen.blit(startText2, (400 - startText2.get_width()/2, 120))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONUP:
                run(player)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()


def run(player):
    Zombie.SPEED = 0.8
    Zombie.DAMAGE = 0.65
    bulletList = []
    zombieList = [ZombieLeft(), ZombieRight()]
    zombie_count = 0
    OVER = False
    LEVEL = 1
    Y_GRAVITY = 1
    JUMP_HEIGHT = 20
    Y_VELOCITY = JUMP_HEIGHT
    POINTS = 1000
    t = 0
    start_ticks = pygame.time.get_ticks()
    birdList = [Bird()]
    zExplosion = []
    r = Rocket()
    g = Gun()

    def knife(zombieList):
        nonlocal POINTS
        for z in zombieList:
            if type(z) == Bird:
                if player.hitbox[0] - 100 < z.hitbox[0] < player.hitbox[0] + player.hitbox[2] + 50 and player.hitbox[1] - 40 < z.hitbox[1] < player.hitbox[1] + player.hitbox[3]:
                    z.HEALTH -= 100
                    POINTS += 75
            else:
                if player.hitbox[0] - 90 < z.hitbox[0] < player.hitbox[0] + player.hitbox[2] + 40 and player.hitbox[1] - 40 < z.hitbox[1] < player.hitbox[1] + player.hitbox[3]:
                    z.HEALTH -= player.DAMAGE
                    POINTS += 15

    def explode(screen, z):
        screen.blit(explosion, (z.x + 15, z.y + 40))

    while True:
        seconds = int((pygame.time.get_ticks()-start_ticks)/1000)
        if seconds > random.randint(6, 12):  # RANDOM NUMBER BETWEEN 6-12
            birdList.append(Bird())
            seconds = 0
            start_ticks = pygame.time.get_ticks()
            LEVEL += 2
            Zombie.SPEED += 0.5
            Zombie.DAMAGE += 0.05

        if OVER:
            game_over(screen, POINTS, zombie_count)

        # Clear the screen before drawing it again
        screen.fill(0)
        # Draw the screen elements
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (128, 128, 128), (0, 400, 800, 550))
        player.draw(screen)
        r.draw(screen)
        g.draw(screen)
        font = pygame.font.SysFont(pygame.font.get_fonts()[-1], 30)
        font2 = pygame.font.SysFont(pygame.font.get_fonts()[-1], 15)
        scoreText = font.render(f'Points: {POINTS}', True, (0, 0, 0))
        screen.blit(scoreText, (550, 420))
        instructions = font2.render(
            '1: Knife    2: Gun    3: Rocket    R: Fire', True, (0, 0, 0))

        screen.blit(instructions, (500, 470))
        ammoGun = font2.render(f'Bullets: {g.BULLETS}', True, (0, 0, 0))
        ammoRocket = font2.render(f'Rockets: {r.BULLETS}', True, (0, 0, 0))

        buyAmmo1 = font2.render("B: 8 Bullets / 200 Points", True, (0, 0, 0))
        buyAmmo2 = font2.render("B: 6 Rockets / 300 Points", True, (0, 0, 0))

        screen.blit(buyAmmo1, (150, 490))
        screen.blit(buyAmmo2, (150, 510))

        screen.blit(ammoGun, (30, 490))
        screen.blit(ammoRocket, (30, 510))

        t += 1
        if t > 200/LEVEL + 20:
            t = 0
            if random.choice([True, False]):
                zombieList.append((ZombieLeft(), ZombieRight())[
                    random.choice([True, False])])

        for bullet in bulletList[:]:
            bullet.draw(screen)
            bullet.update()
            if not bullet:
                bulletList.remove(bullet)

        for z in zombieList[:]:
            for b in bulletList[:]:
                if z.hitbox[0] < b.hitbox[0] < z.hitbox[0] + z.hitbox[2] and z.hitbox[1] < b.hitbox[1] < z.hitbox[1] + z.hitbox[3]:
                    z.HEALTH -= b.DAMAGE
                    POINTS += 15
                    bulletList.remove(b)
            if not z:
                if player.ROCKET:
                    zExplosion.append((z, pygame.time.get_ticks()))
                zombieList.remove(z)
                zombie_count += 1

            # If zombie is close enough to the player it would deal damage until it passes through or kills the player
            if player.hitbox[0] - 5 < z.hitbox[0] + z.hitbox[2] < player.hitbox[0] + player.hitbox[2] + 75 and player.hitbox[1] < z.hitbox[1] + 32 < player.hitbox[1] + player.hitbox[3]:
                player.HEALTH -= z.DAMAGE
                # If player health goes below 0 then display game over text and end game
                if player.HEALTH < 0:
                    zombieList = []
                    OVER = True
            z.draw(screen)
            z.update()

        for z in zExplosion[:]:
            explode(screen, z[0])
            if int((pygame.time.get_ticks() - z[1])/1000) == 1:
                zExplosion.remove(z)

        for bird in birdList:
            for b in bulletList[:]:
                if bird.hitbox[0] < b.hitbox[0] < bird.hitbox[0] + bird.hitbox[2] and bird.hitbox[1] < b.hitbox[1] < bird.hitbox[1] + bird.hitbox[3]:
                    bulletList.remove(b)
                    if player.ROCKET:
                        zExplosion.append((bird, pygame.time.get_ticks()))
                    bird.HEALTH = 0
                    POINTS += 75
            bird.draw(screen)
            bird.update()
            if not bird or bird.x > 810:
                birdList.remove(bird)

        # Update the screen
        display.update()
        CLOCK.tick(60)
        # loop through the events
        for event in pygame.event.get():
            # Check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if player.KNIFE:
                    knife(zombieList)
                    knife(birdList)
                else:
                    if player.ROCKET:
                        if r.BULLETS > 0:
                            r.BULLETS -= 1
                            if player.direction():
                                bulletList.append(RocketRight(player))
                            else:
                                bulletList.append(RocketLeft(player))
                    elif player.GUN:
                        if g.BULLETS > 0:
                            g.BULLETS -= 1
                            if player.direction():
                                bulletList.append(BulletRight(player))
                            else:
                                bulletList.append(BulletLeft(player))
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    player.setKey(0, True)
                    player.left()
                elif event.key == K_d:
                    player.setKey(1, True)
                    player.right()
                if event.key == K_SPACE:
                    player.JUMPING = True
                if event.key == K_r:
                    if player.KNIFE:
                        knife(zombieList)
                        knife(birdList)
                    else:
                        if player.ROCKET:
                            if r.BULLETS > 0:
                                r.BULLETS -= 1
                                if player.direction():
                                    bulletList.append(RocketRight(player))
                                else:
                                    bulletList.append(RocketLeft(player))
                        elif player.GUN:
                            if g.BULLETS > 0:
                                g.BULLETS -= 1
                                if player.direction():
                                    bulletList.append(
                                        BulletRight(player))
                                else:
                                    bulletList.append(
                                        BulletLeft(player))
                if event.key == K_b:
                    if player.GUN:
                        if POINTS >= 200:
                            POINTS -= 200
                            g.BULLETS += 8
                    elif player.ROCKET:
                        if POINTS >= 300:
                            POINTS -= 300
                            r.BULLETS += 6
                if event.key == K_1:
                    player.knife()

                elif event.key == K_2:
                    if 'gun' not in player.LOCKED:
                        player.gun()
                    elif POINTS >= 250:
                        POINTS -= 250
                        player.LOCKED.remove('gun')
                        g.LOCKED = False
                        g.BULLETS = 100
                        player.gun()
                    else:
                        print('Not enough Points')

                elif event.key == K_3:
                    if 'rocket' not in player.LOCKED:
                        player.rocket()
                    elif POINTS >= 500:
                        POINTS -= 500
                        player.LOCKED.remove('rocket')
                        r.LOCKED = False
                        r.BULLETS = 100
                        player.rocket()
                    else:
                        print('Not enought Points')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.setKey(0, False)

                elif event.key == pygame.K_d:
                    player.setKey(1, False)

        # Move player
        if player.KEYS[0]:
            player.moveX(-3)
        elif player.keys()[1]:
            player.moveX(3)
        if player.jumping():
            player.moveY(-Y_VELOCITY)
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                player.JUMPING = False
                Y_VELOCITY = JUMP_HEIGHT


if __name__ == "__main__":
    start_game(screen, player, backgroundBlur)
