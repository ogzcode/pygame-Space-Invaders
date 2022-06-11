import pygame

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
    
    def draws(self,screen):
        for bullet in self.bullet_rect_list:
            pygame.draw.rect(screen, (255,255,0), bullet)

    def get_list(self):
        return self.bullet_rect_list
    
    def remove_bullet(self, bullet):
        self.bullet_rect_list.remove(bullet)