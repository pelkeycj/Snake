class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.next = None
        self.prev = None


class Snake:
    def __init__(self, x, y):
        '''Initialize a one segment snake at position (x,y)'''
        '''initial direction is 'up'''
        s = Segment(x, y, "up")
        self.head = s
        self.tail = s
        self.radius = 6
        self.length = 1

    def changeDirection(self, key):
        '''Change direction of snake head'''
        # cannot move in opposite of current direction
        current_direction = self.head.direction
        if key is "left" and current_direction is "right":
            return
        elif key is "right" and current_direction is "left":
            return
        elif key is "up" and current_direction is "down":
            return
        elif key is "down" and current_direction is "up":
            return

        self.head.direction = key


    def popTail(self):
        '''removes tail from snake'''
        if self.head is self.tail:
            return
        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
        self.length -= 1


    def insert(self, segment):
        if self.head is None:
            self.head = segment
            self.tail = segment
        else:
            segment.next = self.head
            self.head.prev = segment
            self.head = segment

        self.length += 1

    def addSegment(self):
        head = self.head
        delta = self.radius * 2

        #make new head Segment
        if head.direction == "left":
            new_head = Segment(head.x - delta, head.y, head.direction)
        elif head.direction == "right":
            new_head = Segment(head.x + delta, head.y, head.direction)
        elif head.direction == "up":
            new_head = Segment(head.x, head.y - delta, head.direction)
        elif head.direction == "down":
            new_head = Segment(head.x, head.y + delta, head.direction)

        self.insert(new_head)


    def move(self):
        '''Moves snake. Pops tail off and adds to head'''
        self.addSegment()
        self.popTail()


    def getSegments(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print(count)
