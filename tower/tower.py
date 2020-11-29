import pygame
import math
import os

#from ??? import menu ???
#у нас ведь будет меню для магазина, чтобы покупать башни?

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("images/td-gui/PNG", "bg.png")).convert_alpha(), (120, 70))

class Tower(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

        self.selected = False
        self.range = 0
        self.tower_imgs = None
        self.damage = 1
        self.price = 0

        self.menu = Menu(self.x, self.y, menu_bg)
        
        self.place_color = (255, 0, 0)

    def draw(self, win):
        img = self.tower_imgs
        win.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))
        if self.selected:
            self.menu.draw(win)

    def clicked(self, x_pos, y_pos):
        img = self.tower_imgs
        if self.x - img.get_width()//2 + self.width >= x_pos and x_pos >= self.x - img.get_width()//2:
            if self.y + self.height - img.get_height()//2 >= y_pos and y_pos >= self.y - img.get_height()//2:
                return True
        return False

    #def attack_radius(self, win):
    #нужно ли, чтобы область атаки подсвечивалась?

    def draw_placement_range(self, win):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def buy_and_pay(self):
        return self.price

    def move_tower(self, x, y):
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide_other_tower(self, other_tower):
        x2 = other_tower.x
        y2 = other_tower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True
