"""
This is the code for the first challenge in 2022 advent of code.

This code was updated after the first question to answer both of them.
"""


from utils import io
src_file = "input.txt"


def update_top_packs(top_packs: list, new_value: int):
    if new_value > top_packs[0]:
        top_packs[0] = new_value
        top_packs.sort()


if __name__ == "__main__":
    current_pack = []
    top_carry = [0, 0, 0]

    for line in io.load_game_input(src_file):
        if line:
            current_pack.append(int(line))
        else:
            carry = sum(current_pack)
            current_pack = []
            update_top_packs(top_carry, carry)

    print("Max value:", top_carry[-1])
    print("Top 3:", top_carry, sum(top_carry))
