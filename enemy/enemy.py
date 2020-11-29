class Enemy:
    def __init__(self, x, y, end_x, end_y, hp, speed, pos, path):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = end_y
        self.hp = hp
        self.speed = speed
        self.pos = pos
        self.path = path

    def move(self, trace, speed):
        if self.x <= trace[self.pos][0] and self.y <= trace[self.pos][1]:
            if self.x + speed > trace[self.pos][0]:
                self.x = trace[self.pos][0]
            else:
                self.x += speed

            if self.y + speed > trace[self.pos][1]:
                self.y = trace[self.pos][1]
            else:
                self.y += speed
        elif self.x <= trace[self.pos][0] and self.y >= trace[self.pos][1]:
            if self.x + speed > trace[self.pos][0]:
                self.x = trace[self.pos][0]
            else:
                self.x += speed

            if self.y - speed < trace[self.pos][1]:
                self.y = trace[self.pos][1]
            else:
                self.y -= speed
        elif self.x >= trace[self.pos][0] and self.y >= trace[self.pos][1]:
            if self.x - speed < trace[self.pos][0]:
                self.x = trace[self.pos][0]
            else:
                self.x -= speed

            if self.y - speed < trace[self.pos][1]:
                self.y = trace[self.pos][1]
            else:
                self.y -= speed
        elif self.x >= trace[self.pos][0] and self.y <= trace[self.pos][1]:
            if self.x - speed < trace[self.pos][0]:
                self.x = trace[self.pos][0]
            else:
                self.x -= speed

            if self.y + speed > trace[self.pos][1]:
                self.y = trace[self.pos][1]
            else:
                self.y += speed

        if self.x == trace[self.pos][0] and self.y == trace[self.pos][1]:
            self.pos += 1