# Combining the first digit and the last digit
# Forming a single two digit number
import pandas as pd

numbers = ["one",
           "two",
           "three",
           "four",
           "five",
           "six",
           "seven",
           "eight",
           "nine"]


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
        if check_all_number_substrings(input,
                                       numbers,
                                       left_pointer) is not None:
            first_digit = check_all_number_substrings(input,
                                                      numbers,
                                                      left_pointer) + 1
            first_not_digit = False
        else:
            left_pointer += 1

    while second_not_digit:
        if input[right_pointer].isdigit():
            last_digit = input[right_pointer]
            second_not_digit = False
        if check_all_number_substrings(input,
                                       numbers,
                                       right_pointer) is not None:
            last_digit = check_all_number_substrings(input,
                                                     numbers,
                                                     right_pointer) + 1
            second_not_digit = False
        else:
            right_pointer -= 1

    return str(first_digit) + str(last_digit)


# Should I return the index or just true?
def check_all_number_substrings(input, substrings, index):
    for i, substring in enumerate(substrings):
        if input[index:index+len(substring)] == substring:
            return i
    return None


def read_input_to_list(file):
    input = pd.read_csv(file)
    list_input = input.stack().astype(str).tolist()
    return list_input


if __name__ == "__main__":
    print("Doing test example")
    print(main(["two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen"]))

    print("Main Problem")
    input = read_input_to_list("./trebuchet_input.csv")
    print(main(input))
