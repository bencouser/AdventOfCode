# NOTE: This is a very slow solution
# There has to be a faster algorithm to not have to keep adding to list
# my guess is that we need to store data in a dictionary for how many
# Children each card gets and then multiply down the line


# Elf has scratch cards Each card has two lists of numbers
# One list of winning numbers
# One list of numbers on the card

# We have to figure our which numbers you have
# That are on the winning numbers

# Scratch cards cause you to win more scratch cards
# Equal to the number of matching numbers

# You win copies of the cards below the winning card
# equal to the number of matches

# Example:

test_input = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
              "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
              "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
              "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
              "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
              "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

# I need something like
# cards = [{id: 1,
#           copy_cards: [2, 3, 4, 5, 6]}
#          {id: 2,
#           ....

# if len(copycards) = 0
# then we add 1

# each len = 0 card can be combined to make the others


def main(input):
    total_count = len(input)
    # cards = [{'id': 1, 'copy_cards': []}, ...]
    cards = []
    for card in input:
        # Get Card Name
        card_name, card_winning_numbers, card_numbers = split_numbers_tolist(
            card)
        # print(card_name)
        # Get number of winning number
        number_of_copies = count_matching_numbers(
            card_winning_numbers, card_numbers)
        # print(number_of_copies)
        # Get copy cards
        copy_cards = get_copy_cards(card_name, number_of_copies, input)
        cards.append({'id': card_name, 'copy_cards': copy_cards})

    total_count = count_total_cards(cards)
    print(cards)

    return total_count


def count_total_cards(card_list):
    card_dict = {card['id']: card['copy_cards'] for card in card_list}
    total_count = 0
    already_counted = set()

    for card_id in card_dict:
        total_count += count_copies(card_id, card_dict, already_counted)

    return total_count


def count_copies(card_id, card_dict, already_counted):
    if card_id not in already_counted:
        already_counted.add(card_id)
        count = 1
    else:
        count = 0

    for copy_id in card_dict[card_id]:
        count += count_copies(copy_id, card_dict, already_counted)

    return count


# create function get copy cards
# return list of card_names that are copies
def get_copy_cards(card_name, number_of_copies,  input):
    copy_cards = []
    for copy in range(number_of_copies):
        copy_card = input[card_name + copy]
        copy_index = get_card_name(copy_card)
        copy_cards.append(copy_index)
    return copy_cards


def get_card_name(card):
    card = card.split(":")
    card_name = card[0].split(" ")
    card_name = card_name[-1]
    card_name = int(card_name)
    return card_name


def split_numbers_tolist(card):
    card = card.split(":")
    card_name = card[0].split(" ")
    card_name = card_name[-1]
    card_name = int(card_name)
    card_numbers = card[1].split("|")
    card_winning_numbers = card_numbers[0].split()
    card_numbers = card_numbers[1].split()
    # print(card_name)
    # print(card_winning_numbers)
    # print(card_numbers)
    # print()
    return card_name, card_winning_numbers, card_numbers


def count_matching_numbers(winning_numbers, card_numbers):
    matching_numbers = 0
    for number in card_numbers:
        if number in winning_numbers:
            matching_numbers += 1
    return matching_numbers


def read_input(file_name):
    with open(file_name) as file:
        input = file.read().splitlines()
    return input


if __name__ == "__main__":
    test_result = main(test_input)
    print("Test result:", test_result)

    # input = read_input("./input_data/4.txt")
    #
    # main_result = main(input)
    # print("Main result:", main_result)
