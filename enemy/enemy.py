from abc import ABC

class Enemy(ABC):
    def __init__(self, x, y, end_x, end_y):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = end_y

    def move(self, trace, speed):
        pos = 0
        while self.x < self.end_x and self.y < self.end_y:
            while self.x <= trace[pos][0] and self.y <= trace[pos][1]:
                if self.x + speed > trace[pos][0]:
                    self.x = trace[pos][0]
                else:
                    self.x += speed

                if self.y + speed > trace[pos][1]:
                    self.y = trace[pos][1]
                else:
                    self.y += speed

            while self.x <= trace[pos][0] and self.y >= trace[pos][1]:
                if self.x + speed > trace[pos][0]:
                    self.x = trace[pos][0]
                else:
                    self.x += speed

                if self.y - speed < trace[pos][1]:
                    self.y = trace[pos][1]
                else:
                    self.y -= speed
                
            while self.x >= trace[pos][0] and self.y >= trace[pos][1]:
                if self.x - speed < trace[pos][0]):
                    self.x = trace[pos][0]
                else:
                    self.x -= speed

                if self.y - speed < trace[pos][1]:
                    self.y = trace[pos][1]
                else:
                    self.y -= speed

            while self.x >= trace[pos][0] and self.y <= trace[pos][1]:
                if self.x - speed < trace[pos][0]:
                    self.x = trace[pos][0]
                else:
                    self.x -= speed

                if self.y + speed > trace[pos][1]:
                    self.y = trace[pos][1]
                else:
                    self.y += speed

            pos += 1