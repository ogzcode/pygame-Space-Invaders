import pygame
from src.Ship import Ship
from src.Bullets import Bullets
from src.EnemyList import EnemyList
from src.Stars import Stars

class Game:
    def __init__(self, screen_width, screen_height, screen):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

        self.background = Stars(self.screen_width, self.screen_height)
        self.ship = Ship(self.screen_width, self.screen_height)
        self.enemys = EnemyList(self.screen_width, self.screen_height)
        self.bullet_list = Bullets()

        self.score = 0

    def draw_text(self):
        font = pygame.font.Font("freesansbold.ttf", 16)
        surface = font.render(f"Score: {self.score}", True, (255,255,255))
        rect = pygame.Rect((10,10), (surface.get_size()))
        self.screen.blit(surface, rect)

    def bullet_enemy_collision(self):
        for bullet in self.bullet_list.get_list():
            for enemy in self.enemys.get_list():
                if bullet.colliderect(enemy["rect"]):
                    self.enemys.remove_enemy(enemy)
                    self.bullet_list.remove_bullet(bullet)
                    self.score += 1
                    print(self.score)

    def event_control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.ship.set_direction("left")
            elif event.key == pygame.K_RIGHT:
                self.ship.set_direction("right")
        elif event.type == pygame.KEYUP:
            self.ship.set_direction("")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.bullet_list.create(self.ship.x + 10, self.ship.y)

    def on_draw(self):
        self.background.draw_star(self.screen)
        self.ship.draw(self.screen)
        self.enemys.draws(self.screen)
        self.bullet_list.draws(self.screen)
        self.draw_text()

    def on_update(self):
        self.ship.update_pos()

        self.enemys.create_enemy()
        self.score -= self.enemys.update()

        self.bullet_list.update()
        self.bullet_enemy_collision()