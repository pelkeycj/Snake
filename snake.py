class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
class Snake:
    def __init__(self):
        self.segments = [Segment(400, 300, "up")]
