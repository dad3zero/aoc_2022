
from utils import io

src_file = "input.txt"

def badge_name(stack1, stack2, stack3):
    for item in stack1:
        if item in stack2 and item in stack3:
            return item


def common_item(stack1, stack2):
    for item in stack1:
        if item in stack2:
            return item


def item_value(item):
    ascii_value = ord(item)
    if ascii_value < 97:
        value = ascii_value - 38
    else:
        value = ascii_value - 96

    return value


if __name__ == "__main__":
    total_value = 0
    for items in io.load_game_input(src_file):
        comp1, comp2 = items[:len(items)//2], items[len(items)//2:]

        item = common_item(comp1, comp2)
        value = item_value(item)

        total_value += value

    print(total_value)

    group = []
    total_value = 0
    for items in io.load_game_input(src_file):
        group.append(items)

        if len(group) == 3:
            item = badge_name(*group)
            value = item_value(item)
            group.clear()

            total_value += value
    print(total_value)


