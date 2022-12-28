from utils import io

def noop_parse(current_cycle, current_value):
    return current_cycle + 1, current_value

def addx_parse(current_cycle, current_value, cycle_value):
    return current_cycle + 2, current_value + cycle_value

def first_question():
    register_X_value = 1
    cycle = 0

    FIRST_INTEREST_CYCLE = 20
    CYCLE_STEP = 40

    current_interest_cycle = FIRST_INTEREST_CYCLE
    interest_values = []

    for input in io.load_game_input():
        match input.split():
            case['noop']:
                next_cycle, next_value = noop_parse(cycle, register_X_value)
            case['addx', value]:
                next_cycle, next_value = addx_parse(cycle, register_X_value, int(value))

        if next_cycle >= current_interest_cycle:
            print(current_interest_cycle, register_X_value)
            interest_values.append(current_interest_cycle * register_X_value)
            current_interest_cycle += CYCLE_STEP

        register_X_value = next_value
        cycle = next_cycle

    print(interest_values)
    print(sum(interest_values))
    print(sum(interest_values[:6]))

def second_question():
    cycle = 0
    sprite_position = 1
    display = []

    for input in io.load_game_input():
        match input.split():
            case['noop']:
                next_cycle, next_value = noop_parse(cycle, sprite_position)
            case['addx', value]:
                next_cycle, next_value = addx_parse(cycle, sprite_position, int(value))

        append_pixel(display, cycle, sprite_position, next_cycle)
        cycle = next_cycle
        sprite_position = next_value

    draw_screen(display)

def append_pixel(display: list, cycle: int, position: int, next_position: int, max_line: int = 40):
    while cycle < next_position:
        line_position = cycle % max_line

        pixel = "#" if position - 1 <= line_position <= position + 1 else "."
        display.append(pixel)

        cycle += 1


def draw_screen(flow, max_line=40):
    start = 0
    step = max_line
    while display_line := flow[start:start + step]:
        print("".join(display_line))
        start += step


if __name__ == '__main__':
    first_question()
    second_question()
