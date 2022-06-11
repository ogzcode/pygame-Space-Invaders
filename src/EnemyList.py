from turtle import width
import pygame
import random
import os

class EnemyList:
    path = "sprite/enemy"
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.enemy_list = []
        self.creation_time = 0

    def update(self):
        score = 0
        for enemy in self.enemy_list:
            enemy["rect"].y += 1

            if enemy["rect"].y + 20 > self.screen_height:
                score += 1
                self.enemy_list.remove(enemy)

        return score

    def create_enemy(self):
        self.creation_time += 1
        if self.creation_time % 60 == 0:
            image = random.choice(os.listdir(self.path))
            surface = pygame.transform.scale(pygame.image.load(f"{self.path}/{image}"), (20,20))
            rect = surface.get_rect(center=(random.randint(0,self.screen_width - 20), 10))

            if not self.control_pos(rect):
                self.enemy_list.append({"surface": surface, "rect": rect})

            self.creation_time = 0

    def draws(self, screen):
        for enemy in self.enemy_list:
            screen.blit(enemy["surface"], enemy["rect"])

    def control_pos(self, other_rect):
        for enemy in self.enemy_list:
            if enemy["rect"].colliderect(other_rect):
                return True
        return False

    def get_list(self):
        return self.enemy_list

    def remove_enemy(self, enemy):
        self.enemy_list.remove(enemy)