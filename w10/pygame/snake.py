from pygame.display import update


SIZE = 10


class Cell:

    def __init__(self, x, y, head=False):
        self.x = int(x)
        self.y = int(y)
        self.head = head
        self.next = None

    def move(self, x, y):
        old_x = self.x
        old_y = self.y
        self.x = x
        self.y = y
        if self.next != None:
            self.next.move(old_x, old_y)


class Snake:

    def __init__(self, width, height):
        self.field_width = width
        self.field_height = height
        self.head = Cell((width//(2*SIZE))*SIZE, (height//(2*SIZE))*SIZE, True)
        self.collide = False
        self.size = SIZE
        self.direction = "NONE"

    def add_cell(self):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Cell(current.x, current.y)

    def move(self):
        if self.direction=="UP":
            self.move_up()
        elif self.direction=="DOWN":
            self.move_down()
        elif self.direction=="LEFT":
            self.move_left()
        elif self.direction=="RIGHT":
            self.move_right()

    def move_up(self):
        old_y = self.head.y
        self.head.y -= SIZE//2
        self.check_and_move(self.head.x, old_y)

    def move_down(self):
        old_y = self.head.y
        self.head.y += SIZE//2
        self.check_and_move(self.head.x, old_y)

    def move_left(self):
        old_x = self.head.x
        self.head.x -= SIZE//2
        self.check_and_move(old_x, self.head.y)

    def move_right(self):
        old_x = self.head.x
        self.head.x += SIZE//2
        self.check_and_move(old_x, self.head.y)

    def check_and_move(self, x, y):
        self.check_out_of_bounds()
        self.check_collision()
        if self.collide:
            return
        if self.head.next != None:
            self.head.next.move(x, y)

    def check_out_of_bounds(self):
        if self.head.x < 0:
            self.head.x = self.field_width - SIZE
        if self.head.y < 0:
            self.head.y = self.field_height - SIZE
        if self.head.x > (self.field_width - SIZE):
            self.head.x = 0
        if self.head.y > (self.field_height - SIZE):
            self.head.y = 0

    def check_collision(self):
        current = self.head.next
        while current != None:
            if current.x == self.head.x and current.y == self.head.y:
                self.collide = True
                break
            else:
                current = current.next
