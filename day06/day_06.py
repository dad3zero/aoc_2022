from utils import io

def _find_start_marker(seq:str, window_size: int):
    window_size_index = window_size - 1
    for index, char in enumerate(seq[window_size_index:], start=window_size_index):
        if len(set(seq[index-window_size_index:index+1])) == window_size:
            return index +1


def find_start_index(seq):
    return _find_start_marker(seq, 4)

def find_start_message(seq):
    return _find_start_marker(seq, 14)

stream = next(io.load_game_input())
print(find_start_index(stream))
stream = next(io.load_game_input())
print(find_start_message(stream))