import random

class Food:
    def __init__(self):
        self.x = None
        self.y = None
        self.radius = 8


    def setPosition(self, snake):
        x = random.randrange(self.radius, 632, self.radius)
        y = random.randrange(self.radius, 472, self.radius)

        s = snake.head
        while s is not None:
            if s.x is x or s.y is y:
                self.setPosition(snake)
            s = s.next

        self.x = x
        self.y = y
