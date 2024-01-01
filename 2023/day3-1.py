# Add up all the part numbers in the schematic
# Any number adjacent to a symbol (and diagonal) is a part number
# "." is not a symbol

# What is the sum of all the part numbers in the engine schemtic

# Loop through each line
# Find size of number
# Check area around number to see if it should be added


test_input = ["467..114..",
              "...*......",
              "..35..633.",
              "......#...",
              "617*......",
              ".....+.58.",
              "..592.....",
              "......755.",
              "...$.*....",
              ".664.598.."]


# Each direction to look around a cell
# Could optimse by specifying search directions for specific positions
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1), (1, -1),
              (1, 0), (1, 1)]


def read_schematic_file(file_path):
    with open(file_path, 'r') as file:
        schematic = file.readlines()
        # Remove newline characters at the end of each line
        schematic = [line.strip() for line in schematic]
    return schematic


def main(input):
    sum = 0
    j = 0
    line = input[0]
    number = ""
    for j, line in enumerate(input):
        for i, character in enumerate(line):
            if character.isdigit():
                number = number + character
            else:
                if number != "":
                    multi_factor = check_symbols(input, j, i, len(number))
                    sum += int(number) * multi_factor
                    print(number, multi_factor)
                    number = ""
    if number:
        multi_factor = check_symbols(input, j, len(line), len(number))
        sum += int(number) * multi_factor
    return sum


def check_symbols(input, line, character, number_length):
    for offset in range(number_length):
        print(offset)
        current_char_col = character - number_length + offset
        for direction_row, direction_col in directions:
            row, col = line + direction_row, current_char_col + direction_col
            if 0 <= row < len(input) and 0 <= col < len(input[row]):
                print(row, col)
                potential_symbol = input[row][col]
                if potential_symbol != '.' and not potential_symbol.isalnum():
                    allsymbols.append(potential_symbol)
                    return 1
    return 0


allsymbols = []


if __name__ == "__main__":
    # print("Test Results:")
    # print(main(test_input))

    # file_path = './input_data/3.txt'
    # input = read_schematic_file(file_path)
    # print("Main Results:")
    # result = main(input[13])
    # print(input[13])
    # print("Sum of part numbers:", result)
    test = check_symbols("852*68...", 0, 4, 2)
    print(test)


# print(set(allsymbols))
# print(len(allsymbols))
# {'*', '$', '%', '&', '=', '@', '/', '+', '-', '#'}

# Current answer 1180324
