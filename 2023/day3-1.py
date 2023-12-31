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


# Example usage
file_path = './input_data/3.txt'
schematic_input = read_schematic_file(file_path)


def main(input):
    sum = 0
    number = ""
    for j, line in enumerate(input):
        for i, character in enumerate(line):
            if character.isdigit():
                number = number + character
            else:
                if number != "":
                    multi_factor = check_symbols(input,
                                                 j,
                                                 i,
                                                 len(number))
                    sum += int(number) * multi_factor
                    number = ""
    return sum


# I believe once I solve what ranges to search through everything should work
def check_symbols(input, line, character, number_length):
    for offset in range(number_length):
        current_char_col = character - number_length + offset
        for direction_row, direction_col in directions:
            row, col = line + direction_row, current_char_col + direction_col
            if 0 <= row < len(input) and 0 <= col < len(input[row]):
                potential_symbol = input[row][col]
                if potential_symbol.isprintable() and not potential_symbol.isalnum() and potential_symbol != '.':
                    return 1
    return 0


if __name__ == "__main__":
    print("Test Results:")
    print(main(test_input))

    print("Main Results:")
    result = main(schematic_input)
    print("Sum of part numbers:", result)
