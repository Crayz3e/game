from abc import ABC

class Enemy(ABC):
    def __init__(self, x, y, end_x, end_y):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = end_y

    def move(self, trace, speed):
        pos = 0
        while (x < end_x && y < end_y):
            while (x < trace[pos][0] && y < trace[pos][1]):
                if (x + speed > trace[pos][0]):
                    x = trace[pos][0]
                else:
                    x += speed

                if (y + speed > trace[pos][1]):
                    y = trace[pos][1]
                else:
                    y += speed

            while (x < trace[pos]):
                if (x + speed > trace[pos][0]):
                    x = trace[pos][0]
                else:
                    x += speed
            
            while (y < trace[pos]):
                if (y + speed > trace[pos][1]):
                    y = trace[pos][1]
                else:
                    y += speed
            
            pos += 1