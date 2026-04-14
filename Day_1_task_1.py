from pathlib import Path



def parse_input_file(input_file: Path) -> list[str]:
    file_exists = input_file.is_file()
    if not file_exists:
        raise Exception(f"File does not exist {input_file=}")
    input_text = input_file.read_text()
    input_lines = input_text.splitlines()
    return input_lines


def parse_line(line: str) -> tuple[str, int]:
    direction = line[0]
    if (
        not isinstance(direction, str)
        or not direction.strip()
        or direction not in {"R", "L"}
    ):
        raise Exception(f"Direction is wrong {direction=}")

    step = line[1:]
    step_is_int = step.isdigit()
    if not step_is_int:
        raise Exception(f"Step is not integer {step=}")
    step = int(step)
    return direction, step


def move(current_position: int, direction: str, step: int) -> int:
    if direction == "R":
        current_position += step
    else:
        current_position -= step

    current_position = current_position % 100
    if current_position < 0:
        current_position += 100
    return current_position


def main(input_file: Path) -> None:
    input_lines = parse_input_file(input_file)
    current_position = 50
    counter = 0
    for line in input_lines:
        direction, step = parse_line(line)
        current_position = move(current_position, direction, step)
        if current_position == 0:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main(
        Path(
            "C:/Users/dmitrij.vlasov/Desktop/python_trainings/aof_2025_01/Day_1_input.txt"
        )
    )
