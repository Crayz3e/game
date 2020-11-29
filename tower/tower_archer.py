import pygame
import os

from Towers.tower import Tower

import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("images/td-gui/PNG", "bg.png")).convert_alpha(), (120, 70))
archer_imgs1 = []

for i in range(37, 44):
    tower_imgs1 = pygame.transform.scale(pygame.image.load(os.path.join("images/game/archers", str(x) + ".png")).convert_alpha(), (64, 64))

for i in range(2, 10):
    archer_imgs1.append(pygame.image.load(os.path.join("images/game/arch_towers", str(x) + ".png")), convert_aplha(), (90, 90))


class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        #я взяла с того туториала на ютубе эту идею хд
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 200
        self.range = 200
        self.original_range = self.range
        self.in_range = False
        self.left = True
        self.damage = 30
        self.width = self.height = 90
        self.original_damage = self.damage
        self.moving = False
        self.name = "archer"

        self.menu = Menu(self.x, self.y, menu_bg)

    def get_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win):
        super().draw_range(win)
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

    def attack(self, enemies):
        money = 0
        self.in_range = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - 100 / 2 - x) ** 2 + (self.y - 100 / 2 - y) ** 2)
            if dis < self.range:
                self.in_range = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda i: i.path_pos)
        enemy_closest = enemy_closest[::-1]

        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            #
            if self.atcher_count == :
                if first_enemy.health(self.damage) is True:
                    money = first_enemy.if_killed_money_earned * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return money
