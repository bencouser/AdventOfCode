# Combining the first digit and the last digit
# Forming a single two digit number
import pandas as pd


def main(inputs):
    sum = 0
    for input in inputs:
        sum += int(find_calibration_values(input))
    return sum


def find_calibration_values(input):
    left_pointer = 0
    first_not_digit = True
    right_pointer = len(input) - 1
    second_not_digit = True

    while first_not_digit:
        if input[left_pointer].isdigit():
            first_digit = input[left_pointer]
            first_not_digit = False
        else:
            left_pointer += 1

    while second_not_digit:
        if input[right_pointer].isdigit():
            last_digit = input[right_pointer]
            second_not_digit = False
        else:
            right_pointer -= 1

    first_digit = input[left_pointer]
    last_digit = input[right_pointer]
    return first_digit + last_digit


def read_input_to_list(file):
    input = pd.read_csv(file)
    list_input = input.stack().astype(str).tolist()
    return list_input


if __name__ == "__main__":
    print("Doing test example")
    print(main(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]))
    print("Main Problem")
    input = read_input_to_list("./trebuchet_input.csv")
    print(input[0], input[-1])
    print(main(input))
