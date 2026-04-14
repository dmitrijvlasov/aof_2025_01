from pathlib import Path
from Day_2_task_1 import parse_input_file

def main(input_file: Path) -> None:
    all_ranges = parse_input_file(Path)
    invalid_ranges_counter = 0
    for (
        start,
        end,
    ) in all_ranges:
        for number in range(start, end + 1):
            number_is_string = str(number)
            string_length = len(number_is_string)
            if string_length % 2 == 0:
                mid = string_length // 2
                if number_is_string[:mid] == number_is_string[mid:]:
                    invalid_ranges_counter += number
    print(invalid_ranges_counter)

if __name__ == "__main__":
    main(
        Path(
            "C:/Users/dmitrij.vlasov/Desktop/python_trainings/aof_2025_01/Day_2_input.txt"
        )
    )