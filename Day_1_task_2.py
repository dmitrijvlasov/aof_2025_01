from pathlib import Path
from Day_1_task_1 import parse_input_file, parse_line


# 1. kiek kartu kirto 0 (div)
# 2. kokia nauja pozicija (mod)
# 3. itraukti logika neigiamoms vertems
# 4. jei ja buvo paskaiciaves 0, tai kad judedamas nuo to pacio nulio nepriskaiciuotu ji

def move(current_position: int, direction: str, step: int) -> tuple[int, int]:
    #zero_count = 0
    old_position = current_position

    if direction == "R":
        current_position += step
    else:
        current_position -= step

    q1, _ = divmod(old_position + 100, 100)
    q2, current_position = divmod(current_position + 100, 100)
    #zero_count, current_position = divmod(current_position, 100)
    zero_count = abs(q2 - q1)

    if old_position == 0:
        zero_count -= 0

    current_position = current_position % 100
    # if current_position < 0:
    #     current_position += 100
    return current_position, zero_count


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
    main(Path("C:/Users/dmitrij.vlasov/Desktop/python_trainings/aof_2025_01/Day_1_input.txt"))
