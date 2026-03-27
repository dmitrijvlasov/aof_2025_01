from pathlib import Path

def parse_input_file(input_file: Path):
    file_exists = input_file.is_file()
    if not file_exists:
        raise Exception(f"File does not exist {input_file=}")
    input_text = input_file.read_text()
    input_ranges = [input.split("-") for input in input_text.split(",")]
    return input_ranges

def main(input_file: Path) -> None:
    input_lines = parse_input_file(input_file)
    print(input_lines)

if __name__ == "__main__":
    main(Path("C:/Users/dmitrij.vlasov/Desktop/python_trainings/aof_2025_01/Day_2_input.txt"))