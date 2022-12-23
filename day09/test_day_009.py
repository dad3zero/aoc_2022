from collections import defaultdict

import pytest
import day09.day_09 as d9

basic_move_values = [("U", 0, 1),
                     ("D", 0, -1),
                     ("L", -1, 0),
                     ("R", 1, 0)]

def test_basic_move_up():
    r = d9.Rope()
    r.move("U")
    assert r.head_x == 0
    assert r.tail_x == 0
    assert r.head_y == 1
    assert r.tail_y == 0

def test_multiple_move_up():
    r = d9.Rope()
    r.move("U")
    r.move("U")
    r.move("U")
    assert r.head_x == 0
    assert r.tail_x == 0
    assert r.head_y == 3
    assert r.tail_y == 2


@pytest.mark.parametrize("direction, expected_x, expected_y", basic_move_values)
def test_basic_movement(direction, expected_x, expected_y):
    r = d9.Rope()
    r.move(direction)
    assert r.head_x == expected_x
    assert r.head_y == expected_y

multiple_move_values = [("U", 4, 0, 4, 0, 3),
                        ("D", 4, 0, -4, 0, -3),
                        ("L", 4, -4, 0, -3, 0),
                        ("R", 4, 4, 0, 3, 0)]

@pytest.mark.parametrize("direction, steps, expected_head_x, expected_head_y, expected_tail_x, expected_tail_y", multiple_move_values)
def test_repeat_move_up(direction, steps, expected_head_x, expected_head_y, expected_tail_x, expected_tail_y):
    r = d9.Rope()
    for _ in range(steps):
        r.move(direction)

    assert r.head_x == expected_head_x
    assert r.head_y == expected_head_y
    assert r.tail_x == expected_tail_x
    assert r.tail_y == expected_tail_y

def test_repeat_different_moves_one_step():
    r = d9.Rope()
    r.move("U")
    r.move("R")
    assert r.head_x == 1
    assert r.head_y == 1
    assert r.tail_x == 0
    assert r.tail_y == 0

def test_repeat_different_moves_more_steps():
    r = d9.Rope()
    r.move("U")
    r.move("R")
    r.move("R")
    r.move("R")
    r.move("L")
    r.move("U")
    assert r.head_x == 2
    assert r.head_y == 2
    assert r.tail_x == 2
    assert r.tail_y == 1

def test_repeat_single_move_4_knots():
    r = d9.Rope(knots=4)
    r.move("R")
    r.move("R")
    assert r.tail_x == 0
    assert r.tail_y == 0

def test_long_larger_values():
    r = d9.Rope(knots=9)

    visited = defaultdict(int)

    for instructions in input_larger_values:
        direction, how_many = instructions.split()
        for repeat in range(int(how_many)):
            r.move(direction)
            visited[(r.tail_x, r.tail_y)] += 1

    assert r.tail_x == -11
    assert r.tail_y == 6
    assert len(visited) == 36


input_test_values = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"
]

input_larger_values = [
"R 5",
"U 8",
"L 8",
"D 3",
"R 17",
"D 10",
"L 25",
"U 20",
]
