import pygame

class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.radius = 3
        self.direction = direction

class Snake:
    def __init__(self, x, y):
        '''Initialize a one segment snake at position (x,y)'''
        '''initial direction is 'up''''
        self.segments = [Segment(x, y, "up")]
        self.length = 1

    def changeDirection(self, key):
        '''Change direction of snake head''''
        s = self.segments[0]
        s = Segment(s.x, s.y, key)
        self.segments[0] = s
