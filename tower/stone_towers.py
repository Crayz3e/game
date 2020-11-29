import pygame
import os
import spells.spell as spell

from Towers.tower import Tower

import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("images/td-gui/PNG.menu", "bg.png")).convert_alpha(), (120, 70))

for i in range(3, 15):
    archer_imgs1.append(pygame.image.load(os.path.join("images/game/stone_towers", str(x) + ".png")), convert_aplha(), (90, 90))

class StoneTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1
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

    def change_attack_range(self, rng):
        self.range = rng