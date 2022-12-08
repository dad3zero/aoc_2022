import pytest
import day08.day_08 as d8

values_test_on_row = [
    ("30373", [True, False, False, True, True]),
    ("25512", [True, True, True, False, True]),
    ("65332", [True, True, False, True, True]),
    ("33549", [True, False, True, False, True]),
    ("35390", [True, True, False, True, True]),
]
def test_left_to_right():
    values = d8.get_viewable_left_2_right("30373")
    assert values == [True, False, False, True, False]

def test_right_to_left():
    values = d8.get_viewable_right_2_left("30373")
    assert values == [False, False, False, True, True]

@pytest.mark.parametrize("in_value, expected", values_test_on_row)
def test_viewable_row(in_value, expected):
    values = d8.get_viewable_on_row(in_value)
    assert values == expected

def test_view_score():
    values = input_test_value
    print(values)
    assert d8.get_view_score(3, 2, values) == 8


input_test_value = [
"30373",
"25512",
"65332",
"33549",
"35390",
]