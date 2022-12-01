"""
This is the code for the first challenge in 2022 advent of code.

This code was updated after the first question to answer both of them.
"""

src_file = "input.txt"

elves_backpack = []
current_pack = []

with open(src_file) as elves_input:
    for line in elves_input:
        if line.strip():
            current_pack.append(int(line))
        else:
            elves_backpack.append(current_pack)
            current_pack = []

top = sorted([sum(element) for element in elves_backpack])[-3:]
print("Max value:", top[-1])
print("Top 3:", top, sum(top))
