
from utils import io

src_file = "input.txt"

target_values = {
    "R": {"W": ("P", 6), "D": ("R", 3), "L": ("S", 0)},
    "P": {"W": ("S", 6), "D": ("P", 3), "L": ("R", 0)},
    "S": {"W": ("R", 6), "D": ("S", 3), "L": ("P", 0)}
}

shape_scores = {"R": 1,
                "P": 2,
                "S": 3}

values = {"A":"R", "B":"P", "C":"S",
          "Y":"D", "X":"L", "Z":"W"}

if __name__ == "__main__":
    total_score = 0


    for line in io.load_game_input(src_file):
        other, target = line.split()

        other = values[other]
        target = values[target]

        shape_to_do, draw_score = target_values[other][target]

        shape_score = shape_scores[shape_to_do]

        round_score = shape_score + draw_score

        total_score += round_score

    print(total_score)
