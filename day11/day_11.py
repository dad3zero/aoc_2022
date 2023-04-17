from utils import io

class Monkey:
    def __init__(self, name: str, items: list, action: str, divisible_value: int, target_true=None, target_false=None):
        self.name = name.lower()
        self.items = items
        self._action = action
        self._divisible_value = divisible_value
        self.target_true = target_true
        self.target_false = target_false
        self.inspected_item_count = 0
        self._is_worry_managed = True

    def __str__(self):
        return f"{self.name}"

    def inspect_items(self):
        while self.items:
            self.eval_item(self.items.pop(0))
            self.inspected_item_count += 1

    def eval_item(self, worry_level):
        old = worry_level
        bored =  eval(self._action)
        bored = bored // 3
        if bored % self._divisible_value:
            self.target_false.get_item(bored)
        else:
            self.target_true.get_item(bored)

    def get_item(self, item):
        self.items.append(item)

    def add_targets(self, monkey_true, monkey_false):
        self.target_true = monkey_true
        self.target_false = monkey_false

    def set_as_is_worry_managed(self):
        self._is_worry_managed = True
        self._divisible_value *= 3


def create_monkey(monkey_input):
    name = monkey_input[0][:-1]

    items = [int(item)
             for item in monkey_input[1].split(":")[1].split(',')]

    action = monkey_input[2].split(": new = ")[1]

    test_value = int(monkey_input[3].split('divisible by')[1])

    target_true = monkey_input[4].split("throw to ")[1]
    target_false = monkey_input[5].split("throw to ")[1]

    monkey = Monkey(name, items, action, test_value)

    return monkey, target_true.lower(), target_false.lower()


def file_parser(input_file="input.txt"):
    monkeys = []
    monkey_info = []
    for input in io.load_game_input(input_file):
        if input.strip():
            monkey_info.append(input)
        else:
            monkeys.append(create_monkey(monkey_info))
            monkey_info.clear()

    if monkey_info:
        monkeys.append(create_monkey(monkey_info))

    monkeys_dict = {monkey.name: monkey for monkey, _, _ in monkeys}

    if len(monkeys_dict) != len(monkeys):
        raise ValueError(f'Duplicate monkey')

    for monkey, target_true, target_false in monkeys:
        monkey.add_targets(monkeys_dict[target_true], monkeys_dict[target_false])

    return [monkey for monkey, _, _ in monkeys]

def display_monkeys(monkeys: list):
    for monkey in monkeys:
        print(monkey.name)
        print(monkey.items)

def get_most_actives(monkeys: list):
    return sorted(monkeys, key=lambda m: m.inspected_item_count)[-2:]

if __name__ == "__main__":
    monkeys = file_parser("input.txt")

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_items()

    most_actives = get_most_actives(monkeys)
    print(most_actives[0].inspected_item_count * most_actives[1].inspected_item_count)

    monkeys = file_parser("input.txt")
    for monkey in monkeys:
        monkey.set_as_is_worry_managed()

    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect_items()
            #print(f"Completed round {i}")

    most_actives = get_most_actives(monkeys)
    print(most_actives[0].inspected_item_count * most_actives[1].inspected_item_count)