import pygame
import math


class Tower(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

        self.selected = False
        self.range = 0
        self.tower_images = None
        self.price = 0
        self.radius = 200
        
        self.place_color = (255, 0, 0)

    def draw(self, win):
        img = self.tower_images
        win.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))

    def clicked(self, x_pos, y_pos):
        img = self.tower_images
        if self.x - img.get_width()//2 + self.width >= x_pos >= self.x - img.get_width()//2:
            if self.y + self.height - img.get_height()//2 >= y_pos >= self.y - img.get_height()//2:
                return True
        return False

    def attack(self, enemies):
        for enemy in enemies:
            if (enemy.x - self.x) **2 + (enemy.y - self.y)**2 <= self.radius**2:
                enemy.hp -= 2
                return True
        return False

    def draw_placement_range(self, win):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def buy_and_pay(self):
        return self.price

    def move_tower(self, x, y):
        self.x = x
        self.y = y

    def collide_other_tower(self, other_tower):
        x2 = other_tower.x
        y2 = other_tower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True
