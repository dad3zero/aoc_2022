"""
This is the code for the first challenge in 2022 advent of code.

This code was updated after the first question to answer both of them.
"""

src_file = "input.txt"


def update_top_packs(top_packs: list, new_value: int):
    if new_value > top_packs[0]:
        top_packs[0] = new_value
        top_packs.sort()


current_pack = []
top_carry = [0, 0, 0]

with open(src_file) as elves_input:
    for line in elves_input:
        if line.strip():
            current_pack.append(int(line))
        else:
            carry = sum(current_pack)
            current_pack = []
            update_top_packs(top_carry, carry)

print("Max value:", top_carry[-1])
print("Top 3:", top_carry, sum(top_carry))
