import pygame
import math


class Tower(object):
    def __init__(self, x, y, d, img, dis):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.damage = d
        self.tower_images = img
        self.dis = dis
        self.radius = 250

    def draw(self, win):
        img = self.tower_images
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))


    def attack(self, enemies):
        for enemy in enemies:
            if (enemy.x - self.x - self.tower_images.get_width() // 2) ** 2 + \
                    (enemy.y - self.y - self.tower_images.get_height() // 2) ** 2 <= self.radius ** 2:
                enemy.hp -= self.damage
                return True
        return False
