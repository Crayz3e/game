class Enemy():
    def __init__(self, x, y, end_x, end_y, hp, speed, pos, path):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = end_y
        self.hp = hp
        self.speed = speed
        self.pos = pos
        self.enemy_path = enemy_path

    def move(self, trace, speed):
        if self.x <= trace[pos][0] and self.y <= trace[pos][1]:
            if self.x + speed > trace[pos][0]:
                self.x = trace[pos][0]
            else:
                self.x += speed

            if self.y + speed > trace[pos][1]:
                self.y = trace[pos][1]
            else:
                self.y += speed
        elif self.x <= trace[pos][0] and self.y >= trace[pos][1]:
            if self.x + speed > trace[pos][0]:
                self.x = trace[pos][0]
            else:
                self.x += speed

            if self.y - speed < trace[pos][1]:
                self.y = trace[pos][1]
            else:
                self.y -= speed
        elif self.x >= trace[pos][0] and self.y >= trace[pos][1]:
            if self.x - speed < trace[pos][0]):
                self.x = trace[pos][0]
            else:
                self.x -= speed

            if self.y - speed < trace[pos][1]:
                self.y = trace[pos][1]
            else:
                self.y -= speed
        elif self.x >= trace[pos][0] and self.y <= trace[pos][1]:
            if self.x - speed < trace[pos][0]:
                self.x = trace[pos][0]
            else:
                self.x -= speed

            if self.y + speed > trace[pos][1]:
                self.y = trace[pos][1]
            else:
                self.y += speed

        self.pos += 1