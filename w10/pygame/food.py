from random import randint
from time import sleep

class Food:

    def __init__(self, width, height, size, type, head):
        x, y = self.get_xy(width, height, size, head)
        self.x = x
        self.y = y
        self.size = size
        self.type = type

    def check_hit(self, head):
        if not self.check_valid_x(self.x, head.x, self.size) and not self.check_valid_y(self.y, head.y, self.size):
            return 1
        return 0

    def get_xy(self, width, height, size, head):
        x = 0
        y = 0
        ok = False
        while not ok:
            ok = True
            x = randint(0, width)
            y = randint(0, height)
            current = head
            while current != None:
                if not self.check_valid_x(x, current.x, size) and not self.check_valid_y(y, current.y, size):
                    ok = False
                    break
                current = current.next
        return x, y

    def check_valid_x(self, x, cell_x, size):
        valid = True
        if x>=(cell_x-size) and x<=(cell_x+size):
            valid = False
        return valid

    def check_valid_y(self, y, cell_y, size):
        valid = True
        if y>=(cell_y-size) and y<=(cell_y+size):
            valid = False
        return valid
