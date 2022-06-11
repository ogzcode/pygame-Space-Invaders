#Background
import pygame
import random

class Stars:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.star_list = []
        self.random_star()

    def random_star(self):
        for i in range(100):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            self.star_list.append({"pos_x": x, "pos_y": y})

    def draw_star(self, screen):
        for star in self.star_list:
            pygame.draw.rect(screen, (255,255,255), (star["pos_x"], star["pos_y"], 2, 2))
