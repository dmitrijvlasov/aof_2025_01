from pathlib import Path


def parse_input_file(input_file: Path) -> tuple[(int, int)]:
    file_exists = input_file.is_file()
    if not file_exists:
        raise Exception(f"File does not exist {input_file=}")
    raw_input = input_file.read_text()
    ranges = raw_input.split(",")
    all_list_of_ranges = []
    for each_range in ranges:
        start_range, end_range = each_range.split("-")
        start_range_is_int = start_range.isdigit
        if not start_range_is_int:
            raise Exception(f"start range is not integer {start_range=}")
        start_range = int(start_range)
        end_range_is_int = end_range.isdigit
        if not end_range_is_int:
            raise Exception(f"end range is not integer {end_range=}")
        end_range = int(end_range)
        all_list_of_ranges.append((start_range, end_range))
    return all_list_of_ranges


def main(input_file: Path) -> None:
    all_ranges = parse_input_file(input_file)
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
