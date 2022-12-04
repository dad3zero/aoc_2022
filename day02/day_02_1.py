
src_file = "input.txt"

result_scores = {  # The key is my shape and the returned dictionary returns the score for the opponent shape.
    "R": {"R": 3, "P": 0, "S": 6},
    "P": {"R": 6, "P": 3, "S": 0},
    "S": {"R": 0, "P": 6, "S": 3}
}

shape_scores = {"R": 1,  # This is the scores for playing a shape
                "P": 2,
                "S": 3}

values = {"A":"R", "B":"P", "C":"S",  # Those are the corresponding shapes for each character on the sheet.
          "Y":"P", "X":"R", "Z":"S"}


if __name__ == "__main__":
    total_score = 0

    with open(src_file) as game_input:
        for line in game_input:
            opponent_shape, my_shape = line.strip().split()

            my_shape = values[my_shape]
            opponent_shape = values[opponent_shape]


            shape_score = shape_scores[my_shape]
            round_result = result_scores[my_shape][opponent_shape]

            total_score += shape_score + round_result

    print(total_score)

