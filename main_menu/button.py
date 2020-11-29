import pygame


class Button:
    def __init__(self, position: tuple, width: int, height: int, image):
        self.position = position
        self.width = width
        self.height = height
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def pressed(self, mouse: tuple):
        if self.position[0] <= mouse[0] <= (self.position[0] + self.width):
            if self.position[1] <= mouse[1] <= (self.position[1] + self.height):
                return True

        return False

    def get_pos(self):
        return self.position

    def direct(self):
        if self.position[0] <= pygame.mouse.get_pos()[0] <= (self.position[0] + self.width):
            if self.position[1] <= pygame.mouse.get_pos()[1] <= (self.position[1] + self.height):
                return True

        return False

    def __del__(self):
        self.position = (0, 0)
        self.width = 0
        self.height = 0
        self.image = None
        self.action = None
