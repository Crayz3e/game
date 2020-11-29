import pygame
import os
import spells.spell as spell
from tower.tower import Tower

import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("images/td-gui/PNG.menu", "bg.png")).convert_alpha(), (120, 70))
archer_imgs1 = []

for i in range(64, 77):
    tower_imgs1 = pygame.transform.scale(pygame.image.load(os.path.join("images/game/archers", str(i) + ".png")).convert_alpha(), (64, 64))

for i in range(2, 14):
    archer_imgs1.append(pygame.image.load(os.path.join("images/game/mage_towers", str(i) + ".png")).convert_aplha(), (90, 90))

class MageTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 100
        self.original_range = self.range
        self.in_range = False
        self.left = True
        self.damage = 30
        self.width = self.height = 90
        self.original_damage = self.damage
        self.moving = False
        self.name = "mage"

    def get_cost(self):
        return self.get_item_cost()

    def draw(self, win):
        super().draw(win)

        if self.in_range and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 10]
        if self.left is True:
            add = -25
        else:
            add = -archer.get_width() + 10

        win.blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))

    def change_attack_range(self, rng):
        self.range = rng