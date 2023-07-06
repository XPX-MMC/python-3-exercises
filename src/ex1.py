from ValidationException import ValidationException


def validate_file(file_name):
    lines = []

    with open(file_name, "r") as file1:
        while True:
            line = file1.readline().split()

            if not line:
                break
            lines.append(line)

    for i in range(len(lines)):
        if "." in lines[i][1]:
            raise ValidationException(f"Invalid Milage: {lines[i][1]}")


def ex1():
    try:
        validate_file("../files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()