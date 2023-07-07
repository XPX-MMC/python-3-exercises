from ValidationException import ValidationException

def validate_file(file_name):
    file1 = open(file_name)

    for count, line in enumerate(file1):
        # print(count, line, end="\n")
        if count != 0:
            line_values = line.split(',')
            try:
                int(line_values[1])
            except:
                file1.close()
                raise ValidationException(f"INVALID MILEAGE: ${line_values[1]}")

    file1.close()
    return True


def ex1():
    try:
        validate_file("./files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()