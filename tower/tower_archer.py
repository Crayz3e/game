import pygame
import os
from tower.tower import Tower

current_path = os.path.dirname(__file__)

ind = current_path.find("tower/")

current_path = current_path[:ind - len("tower/") + 1:]

tower_imgs1 = [pygame.transform.scale(pygame.image.load(current_path + "/images/archers/" + str(i) + ".png"), (64, 64))
               for i in range(37, 44)]


archer_imgs1 = [pygame.transform.scale(pygame.image.load(current_path + "/images/arch_towers/" + str(i) + ".png"),
                                       (90, 90))
                for i in [2, 4, 6, 7, 8, 9, 10, 11]]


class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        # я взяла с того туториала на ютубе эту идею хд
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.in_range = False
        self.left = True
        self.damage = 30
        self.width = self.height = 90
        self.original_damage = self.damage
        self.moving = False
        self.name = "archer"
        self.cost = 50

    def get_cost(self):
        return self.cost

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
