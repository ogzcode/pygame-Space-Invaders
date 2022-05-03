import pygame, sys
from pygame.locals import *
import os
import random

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 480

class Bullets:
    def __init__(self):
        self.bullet_rect_list = []

    def create(self, pos_x, pos_y):
        self.bullet_rect_list.append(pygame.Rect(pos_x, pos_y, 1, 4))

    def update(self):
        for bullet in self.bullet_rect_list:
            bullet.y -= 2
            
            if bullet.y < 0:
                self.bullet_rect_list.remove(bullet)
    
    def draws(self):
        for bullet in self.bullet_rect_list:
            pygame.draw.rect(SCREEN, (255,255,0), bullet)

class Ship:
    def __init__(self):
        self.surface = pygame.transform.scale(pygame.image.load("sprite/ship.png"), (20,20))
        self.x = 0
        self.y = SCREEN_HEIGHT - 40
        self.direction = ""

    def update_pos(self):
        if self.direction == "left":
            if self.x > 0:
                self.x -= 2
        elif self.direction == "right":
            if self.x < SCREEN_WIDTH - 20:
                self.x += 2

    def draw(self):
        SCREEN.blit(self.surface, (self.x, self.y))

    def set_direction(self, direction):
        self.direction = direction

class EnemyList:
    path = "sprite/enemy"
    def __init__(self):
        self.enemy_list = []
        self.creation_time = 0

    def update(self):
        global score
        for enemy in self.enemy_list:
            enemy["rect"].y += 1

            if enemy["rect"].y + 20 > SCREEN_HEIGHT:
                score -= 1
                self.enemy_list.remove(enemy)

    def create_enemy(self):
        self.creation_time += 1
        if self.creation_time % 60 == 0:
            image = random.choice(os.listdir(self.path))
            surface = pygame.transform.scale(pygame.image.load(f"{self.path}/{image}"), (20,20))
            rect = surface.get_rect(center=(random.randint(0,SCREEN_WIDTH - 20), 10))

            if not self.control_pos(rect):
                self.enemy_list.append({"surface": surface, "rect": rect})

            self.creation_time = 0

    def draws(self):
        for enemy in self.enemy_list:
            SCREEN.blit(enemy["surface"], enemy["rect"])

    def control_pos(self, other_rect):
        for enemy in self.enemy_list:
            if enemy["rect"].colliderect(other_rect):
                return True
        return False

def random_star():
    pos_list = []
    for i in range(100):
        x = random.randint(0,SCREEN_WIDTH)
        y = random.randint(0,SCREEN_HEIGHT)
        pos_list.append({"pos_x": x, "pos_y": y})

    return pos_list

def draw_star(star_list):
    for star in star_list:
        pygame.draw.rect(SCREEN, (255,255,255), (star["pos_x"], star["pos_y"], 2, 2))

def draw_text(scr):
    font = pygame.font.Font("freesansbold.ttf", 16)
    surface = font.render(f"Score: {scr}", True, (255,255,255))
    rect = pygame.Rect((10,10), (surface.get_size()))
    SCREEN.blit(surface, rect)

def bullet_enemy_collision(bullets, enemyies):
    global score
    for bullet in bullets:
        for enemy in enemyies:
            if bullet.colliderect(enemy["rect"]):
                enemyies.remove(enemy)
                bullets.remove(bullet)
                score += 1


pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
GAME_STATE = True

star_list = random_star()


ship = Ship()
direction = ""

enemys = EnemyList()
bullet_list = Bullets()

score = 0
while GAME_STATE:
    SCREEN.fill((0,0,50))

    draw_star(star_list)

    ship.draw()
    ship.update_pos()

    enemys.create_enemy()
    enemys.draws()
    enemys.update()

    bullet_list.draws()
    bullet_list.update()

    bullet_enemy_collision(bullet_list.bullet_rect_list, enemys.enemy_list)

    draw_text(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATE = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.set_direction("left")
            elif event.key == pygame.K_RIGHT:
                ship.set_direction("right")
        elif event.type == pygame.KEYUP:
            ship.set_direction("")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet_list.create(ship.x + 10, ship.y)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()

        
