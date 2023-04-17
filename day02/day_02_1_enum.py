"""
This version of the first question uses Python's enums.
"""

from enum import Enum

src_file = "input.txt"


class ShapeScore(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.value == other.value
        else:
            return False

    def __gt__(self, other):
        if self.__class__ == other.__class__:
            if self.value == 1 and other.value == 3:
                return True
            elif self.value == 3 and other.value == 1:
                return False
            else:
                return self.value > other.value

class ResultScore(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0

def get_round_result(mine, opponent):
    if mine > opponent:
        result = ResultScore.WIN
    elif mine == opponent:
        result = ResultScore.DRAW
    else:
        result = ResultScore.LOOSE

    return result


opponent_values = {"A": ShapeScore.ROCK, "B": ShapeScore.PAPER, "C": ShapeScore.SCISSOR}
my_values = {"Y": ShapeScore.PAPER, "X": ShapeScore.ROCK, "Z": ShapeScore.SCISSOR}


if __name__ == "__main__":
    total_score = 0

    with open(src_file) as game_input:
        for line in game_input:
            opponent_shape, my_shape = line.strip().split()

            my_shape = my_values[my_shape]
            opponent_shape = opponent_values[opponent_shape]

            total_score += (my_shape.value + get_round_result(my_shape, opponent_shape).value)

    print(total_score)


