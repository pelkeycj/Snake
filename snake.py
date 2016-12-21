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
        self.radius = 8
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


    def addHead(self):
        '''Add segment to head of snake'''
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

        #add new head
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

        self.length += 1


    def addTail(self):
        '''Add segment to tail of snake'''
        tail = self.tail
        delta = self.radius * 2

        #make new tail Segment
        if tail.direction == "left":
            new_tail = Segment(tail.x + delta, tail.y, tail.direction)
        elif tail.direction == "right":
            new_tail = Segment(tail.x - delta, tail.y, tail.direction)
        elif tail.direction == "up":
            new_tail = Segment(tail.x, tail.y + delta, tail.direction)
        elif tail.direction == "down":
            new_tail = Segment(tail.x, tail.y - delta, tail.direction)

        #insert new tail
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

        self.length += 1


    def move(self):
        '''Moves snake. Pops tail off and adds to head'''
        self.addHead()
        self.popTail()


    def eat(self, food):
        s = self.head
        if (s.x - 5) <= food.x <= (s.x + 5) and (s.y - 5) <= food.y <= (s.y + 5):
            print("eat")
            food.setPosition(self)
            self.addTail()
