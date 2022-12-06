import pytest

import day_06 as d6

packet_test_data = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
                    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
                    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
                    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
                    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)]

message_test_data = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
                     ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
                     ("nppdvjthqldpwncqszvftbrmjlhg", 23),
                     ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
                     ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)]

@pytest.mark.parametrize("input_signal, mark_position", packet_test_data)
def test_find_mark(input_signal, mark_position):
    assert d6.find_start_index(input_signal) == mark_position

@pytest.mark.parametrize("input_signal, mark_position", message_test_data)
def test_find_message(input_signal, mark_position):
    assert d6.find_start_message(input_signal) == mark_position
