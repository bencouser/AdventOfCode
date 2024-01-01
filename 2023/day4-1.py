# Elf has scratch cards
# Each card has two lists of numbers
# One list of winning numbers
# One list of numbers on the card

# We have to figure our which numbers you have
# That are on the winning numbers

# One match is worth 1 point
# Each match after the first doubles in point value.

# Example:


test_input = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
              "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
              "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
              "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
              "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
              "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]


def main(input):
    total_points = 0
    for card in input:
        card_winning_numbers, card_numbers = split_numbers_tolist(card)
        matching_numbers_count = count_matching_numbers(
            card_winning_numbers, card_numbers)
        points = calculate_points(matching_numbers_count)
        total_points += points
    return total_points


def split_numbers_tolist(card):
    card = card.split(":")
    # card_name = card[0]
    card_numbers = card[1].split("|")
    card_winning_numbers = card_numbers[0].split()
    card_numbers = card_numbers[1].split()
    # print(card_name)
    # print(card_winning_numbers)
    # print(card_numbers)
    # print()
    return card_winning_numbers, card_numbers


def count_matching_numbers(winning_numbers, card_numbers):
    matching_numbers = 0
    for number in card_numbers:
        if number in winning_numbers:
            matching_numbers += 1
    return matching_numbers


def calculate_points(matching_numbers):
    points = 0
    if matching_numbers == 0:
        return points
    else:
        points += 1
        for i in range(1, matching_numbers):
            points *= 2
        return points


def read_input(file_name):
    with open(file_name) as file:
        input = file.read().splitlines()
    return input


if __name__ == "__main__":
    test_result = main(test_input)
    print("Test result:", test_result)

    input = read_input("./input_data/4.txt")

    main_result = main(input)
    print("Main result:", main_result)
