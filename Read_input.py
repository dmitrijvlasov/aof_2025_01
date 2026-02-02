from pathlib import Path

input_file = Path(
    "C:/Users/dmitrij.vlasov/Desktop/python_trainings/aof_2025_01/input.txt"
)
file_exists = input_file.is_file()
if not file_exists:
    raise Exception(f"File does not exist {input_file=}")

input_text = input_file.read_text()
input_lines = input_text.splitlines()
current_position = 50
counter = 0

for line in input_lines:
    direction = line[0]  # direction from the input
    if (
        not isinstance(direction, str)
        or not direction.strip()
        or direction not in {"R", "L"}
    ):
        raise Exception(f"Direction is wrong {direction=}")
    # patikrink ar gera kryptis ar tai L ar R o ne kas kitas
    step = line[1:]  # steps from the input
    step_is_int = step.isdigit()  # check if integer
    if not step_is_int:  # if not raise exception
        raise Exception(f"Step is not as integer")  # exception
    step = int(step)  # string to integer
    # patikrink ar tai yra skaicius is paversk i skaiciu.
    # for move in range(0, 99):
    #     if direction == "L":  # check position left
    #         current_position = current_position - step  # go left
    #     elif direction == "R":  # check position right
    #         current_position = current_position + step  # go right
    #     # pakeisk current position
    #     if current_position == 0:  # check if current position is 0
    #         counter += 1  # counter increase when current position is 0
    #     # ir pasitikrink ar current possition ==0

    if direction == "R":
        current_position += step
    else:
        current_position -= step

    current_position = current_position % 100
    if current_position < 0:
        current_position += 100
    elif current_position > 99:
        current_position -= 100

    counter += current_position == 0
print(counter)
# jei taip prisidek counteri +=1


# fruit = "apple"
# count = 1
# msg = f"I have {count} {fruit}"

# text = "Labas vakaras Dima!"
# words = text.split(sep=" ")
