import pygame

class Ship:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = pygame.transform.scale(pygame.image.load("sprite/ship.png"), (20,20))
        self.x = 0
        self.y = self.screen_height - 40
        self.direction = ""

    def update_pos(self):
        if self.direction == "left":
            if self.x > 0:
                self.x -= 2
        elif self.direction == "right":
            if self.x < self.screen_width - 20:
                self.x += 2

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def set_direction(self, direction):
        self.direction = direction