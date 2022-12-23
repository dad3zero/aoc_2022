
from collections import defaultdict

import numpy as np

from utils import io


class Knot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.next_knot: Knot = None

    def add_next_knot(self, x: int = 0, y: int = 0):
        if self.next_knot is not None:
            new_knot = self.next_knot.add_next_knot(x, y)
        else:
            self.next_knot = Knot(x, y)
            new_knot = self.next_knot

        return new_knot

    def move_up(self):
        self.y += 1
        if self.next_knot:
            self.next_knot.follow(self)


    def move_down(self):
        self.y -= 1
        if self.next_knot:
            self.next_knot.follow(self)

    def move_left(self):
        self.x -= 1
        if self.next_knot:
            self.next_knot.follow(self)

    def move_right(self):
        self.x += 1
        if self.next_knot:
            self.next_knot.follow(self)

    def follow(self, head):
        diff_x = head.x - self.x
        diff_y = head.y - self.y

        if abs(diff_x) > 1 or abs(diff_y) > 1:
            self.x = self.x + np.sign(diff_x)
            self.y = self.y + np.sign(diff_y)

        if self.next_knot:
            self.next_knot.follow(self)

class Rope:
    def __init__(self, x=0, y=0, knots=1):
        self.head_knot = Knot()
        self.tail_knot = None

        for _ in range(knots):
            new_knot = self.head_knot.add_next_knot()

        self.tail_knot = new_knot

    @property
    def head_x(self):
        return self.head_knot.x

    @property
    def head_y(self):
        return self.head_knot.y

    @property
    def tail_x(self):
        return self.tail_knot.x

    @property
    def tail_y(self):
        return self.tail_knot.y

    def move(self, direction):
        match direction:
            case 'U':
                self.head_knot.move_up()
            case 'D':
                self.head_knot.move_down()
            case 'L':
                self.head_knot.move_left()
            case 'R':
                self.head_knot.move_right()


def update_visited_spot(position, visited_spots):
    visited_spots[position] += 1

def input_parser(input_str: str):
    direction, steps = input_str.split()
    return direction, int(steps)

if __name__ == "__main__":
    visited = defaultdict(int)
    r = Rope(knots=9)
    for input in io.load_game_input():
        direction, steps = input_parser(input)
        for _ in range(steps):
            r.move(direction)
            update_visited_spot((r.tail_x, r.tail_y), visited)

    from pprint import pprint
    pprint(visited)
    print(len(visited))

