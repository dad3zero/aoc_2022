import re

pattern = "move (?P<how_many>[0-9]+) from (?P<from>[0-9]) to (?P<to>[0-9])"

src_file = "input.txt"

def setup_stacks(input_file):
    docks = []
    for line in input_file:
        if not line.strip():
            break
        docks.append(line[1::4])

    stacks = [[] for _ in range(len(docks.pop()))]
    docks.reverse()

    for col in docks:
        for index, crate in enumerate(col):
            if not crate.isspace():
                stacks[index].append(crate)

    stacks.insert(0, None)  # a first "empty" value is inserted to have numbering matching the indexes
    return stacks

def move_crate_9000(docks: list, from_stack: int, to_stack: int, how_many: int = 1):
    from_stack = int(from_stack)
    to_stack = int(to_stack)
    how_many = int(how_many)

    for _ in range(how_many):
        docks[to_stack].append(docks[from_stack].pop())


def move_crate_9001(docks: list, from_stack: int, to_stack: int, how_many: int = 1):
    from_stack = int(from_stack)
    to_stack = int(to_stack)
    how_many = int(how_many)

    docks[to_stack].extend(docks[from_stack][-how_many:])
    docks[from_stack] = docks[from_stack][:-how_many]


stacks = []

if __name__ == "__main__":
    with open(src_file) as game_input:
        docks = setup_stacks(game_input)

        for line in game_input:
            if result := re.search(pattern, line):
                how_many, from_stack, to_stack = result.groups()
                move_crate_9001(docks, from_stack, to_stack, how_many)
            else:
                print(f"Line cannot be parsed : {line}")

    for stack in docks[1:]:
        print(stack[-1], end="")
