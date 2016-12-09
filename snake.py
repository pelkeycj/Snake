class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


class Snake:
    def __init__(self, x, y):
        '''Initialize a one segment snake at position (x,y)'''
        '''initial direction is 'up'''
        self.segments = [Segment(x, y, "up"), Segment(x + 10, y + 10, "up")]
        self.radius = 6
        self.length = 1


    def changeDirection(self, key):
        '''Change direction of snake head'''
        # cannot move in opposite of current direction
        current_direction = self.segments[0].direction
        if key is "left" and current_direction is "right":
            return
        elif key is "right" and current_direction is "left":
            return
        elif key is "up" and current_direction is "down":
            return
        elif key is "down" and current_direction is "up":
            return

        s = self.segments[0]
        s = Segment(s.x, s.y, key)
        self.segments[0] = s


    def move(self):
        '''Moves snake. Pops tail off and adds to head'''
        head = self.segments[0]
        delta = 2

        #make new head Segment
        if head.direction == "left":
            new_head = Segment(head.x - delta, head.y, head.direction)
        elif head.direction == "right":
            new_head = Segment(head.x + delta, head.y, head.direction)
        elif head.direction == "up":
            new_head = Segment(head.x, head.y - delta, head.direction)
        elif head.direction == "down":
            new_head = Segment(head.x, head.y + delta, head.direction)

        if self.length == 1:
            self.segments = [new_head]
        else:
            # append new segment to head of snake, pop tail
            self.segments = [new_head].extend(self.segments.pop())
