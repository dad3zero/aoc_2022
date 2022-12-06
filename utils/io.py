def load_game_input(src_path="input.txt"):
    with open(src_path) as data_input:
        for line in data_input:
            yield line.rstrip()