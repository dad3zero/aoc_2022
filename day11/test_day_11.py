import pytest

import day_11 as d11

@pytest.fixture
def monkeys():
    return d11.file_parser("test_input.txt")

def test_use_case_round1(monkeys):
    for monkey in monkeys:
        monkey.inspect_items()

    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert len(monkeys[2].items) == 0
    assert len(monkeys[3].items) == 0

def test_use_case_round2(monkeys):
    for _ in range(2):
        for monkey in monkeys:
            monkey.inspect_items()

    assert monkeys[0].items == [695, 10, 71, 135, 350]
    assert monkeys[1].items == [43, 49, 58, 55, 362]
    assert len(monkeys[2].items) == 0
    assert len(monkeys[3].items) == 0

def test_use_case_round20(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_items()

    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert len(monkeys[2].items) == 0
    assert len(monkeys[3].items) == 0

def test_counting_round20_inspection(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_items()

    assert monkeys[0].inspected_item_count == 101
    assert monkeys[1].inspected_item_count == 95
    assert monkeys[2].inspected_item_count == 7
    assert monkeys[3].inspected_item_count == 105

def test_most_active_rount20(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_items()

    most_actives = d11.get_most_actives(monkeys)
    assert most_actives[0].inspected_item_count == 101
    assert most_actives[1].inspected_item_count == 105

    assert most_actives[0].inspected_item_count * most_actives[1].inspected_item_count == 10605

def test_use_case_not_managed_round1(monkeys):
    for monkey in monkeys:
        monkey.is_worry_managed = False

    for monkey in monkeys:
        monkey.inspect_items()

    assert monkeys[0].inspected_item_count == 2
    assert monkeys[1].inspected_item_count == 4
    assert monkeys[2].inspected_item_count == 3
    assert monkeys[3].inspected_item_count == 6
