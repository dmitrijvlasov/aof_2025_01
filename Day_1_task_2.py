from pathlib import Path
from day_1_task_1 import parse_input_file, parse_line

def move_right(current_position: int, step: int) -> tuple[int, int]:
    """Calculates new position and how many times zero was crossed.

    Returns:
        tuple with new position and zero count
    """
    if not isinstance(current_position, int) or not isinstance(step, int):
        raise ValueError(
            f"Incorrect input type given, exp: int, got {type(current_position)} and {type(step)}"
        )

    if current_position < 0:
        raise ValueError(f"Current position is negative {current_position}")

    if step < 0:
        raise ValueError(f"Step is negative {step}")

    old_position = current_position
    new_position = current_position + step
    temp_current_position = new_position

    zero_count = new_position // 100
    new_position = new_position % 100

    if new_position < 0:
        new_position += 100
    elif old_position == 0 and temp_current_position < 0:
        zero_count = 0
    elif old_position == 0 and temp_current_position > 0:
        zero_count = 0
    return new_position, zero_count


def move_left(current_position: int, step: int) -> tuple[int, int]:
    """Calculates new position and how many times zero was crossed.

    Returns:
        tuple with new position and zero count
    """
    if not isinstance(current_position, int) or not isinstance(step, int):
        raise ValueError(
            f"Incorrect input type given, exp: int, got {type(current_position)} and {type(step)}"
        )

    if current_position < 0:
        raise ValueError(f"Current position is negative {current_position}")

    if step < 0:
        raise ValueError(f"Step is negative {step}")

    old_position = current_position
    new_position = current_position - step

    if -100 <= new_position < 0:
        new_position += 100
    elif -1000 <= new_position < -100:
        zero_count, new_position = divmod(new_position, 100)
        zero_count = abs(zero_count)
    elif new_position < -1000:
        zero_count, new_position = divmod(new_position, 100)
        zero_count = abs(zero_count) - 1

    # zero_count = (abs(new_position) // 100) + 1
    # new_position = new_position % 100
    temp_current_position = new_position

    if old_position == 0 and temp_current_position < 0:
        zero_count = 0
    # elif old_position == 0 and temp_current_position > 0:
    #     zero_count = 0
    return new_position, zero_count


def move(current_position: int, direction: str, step: int) -> tuple[int, int]:
    """Checks to which direction move has to be done and folows to another function.

    Returns:
        tuple with new position and zero count
    """

    if direction != "R" and direction != "L":
        raise ValueError(f"The direction is not Right {direction}")
    
    if not isinstance(direction, str):
        raise ValueError(f"Incorrect input type, {direction}")

    zero_count = 0

    if direction == "R":
        new_position, zero_count = move_right(current_position, step)
    elif direction == "L":
        new_position, zero_count = move_left(current_position, step)

    return new_position, zero_count


def main(input_file: Path) -> None:
    input_lines = parse_input_file(input_file)
    current_position = 50
    counter = 0
    for line in input_lines:
        direction, step = parse_line(line)
        current_position, zero_count = move(current_position, direction, step)
        counter += zero_count

    print(counter)


if __name__ == "__main__":
    main(
        Path(
            "C:/Users/dmitrij.vlasov/Desktop/python_trainings/aof_2025_01/Day_1_input.txt"
        )
    )
