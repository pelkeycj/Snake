import pygame

class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

class Snake:
    def __init__(self, x, y):
        '''Initialize a one segment snake at position (x,y)'''
        '''initial direction is 'up'''
        self.segments = [Segment(x, y, "up")]
        self.radius = 3
        self.length = 1

    def changeDirection(self, key):
        '''Change direction of snake head'''
        s = self.segments[0]
        s = Segment(s.x, s.y, key)
        self.segments[0] = s

    def move(self):
        '''Moves snake. Pops tail off and adds to head'''
        head = self.segments[0]
        delta = self.radius * 2

        #make new head Segment
        if head.direction == pygame.K_LEFT:
            new_head = Segment(head.x - delta, head.y, head.direction)
        elif head.direction == pygame.K_RIGHT:
            new_head = Segment(head.x + delta, head.y, head.direction)
        elif head.direction == pygame.K_UP:
            new_head = Segment(head.x, head.y - delta, head.direction)
        elif head.direction == pygame.K_DOWN:
            new_head = Segment(head.x, head.y + delta, head.direction)

        # append new segment to head of snake, pop tail
        self.segments = [new_head] + self.segments.pop()
