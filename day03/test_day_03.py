import pytest

import day_03 as d3


test_data = [("vJrwpWtwJgWr", "hcsFMMfFFhFp", "p"),
             ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL", "L"),
             ("PmmdzqPrV", "vPwwTWBwg", "P")]


@pytest.mark.parametrize("right, left, result", test_data)
def test_common_item(right, left, result):
    assert d3.common_item(right, left) == result

