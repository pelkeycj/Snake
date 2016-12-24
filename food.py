import random

class Food:
    def __init__(self):
        self.x = None
        self.y = None
        self.radius = 8


    def setPosition(self, snake):
        x = random.randrange(7, 826, 7)
        y = random.randrange(7, 686, 7)

        s = snake.head
        while s is not None:
            if s.x is x or s.y is y:
                self.setPosition(snake)
            s = s.next

        self.x = x
        self.y = y
