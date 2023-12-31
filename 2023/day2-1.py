import pandas as pd


def read_input_to_list(file):
    input = pd.read_csv(file)
    list_input = input.stack().astype(str).tolist()
    return list_input


test_input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
              "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
              "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
              "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
              "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]


# What to do
# read game and split into sets
# Count maximum number of each colour per set
# If max is less than elf condition we can add id to sum


# Call function to see if we add the id
def main(input_games):
    sum = 0
    for id, game in enumerate(input_games):
        if check_valid_game(game, 12, 13, 14):
            sum += id + 1
            print(id + 1)
    return sum


# Need to check each against condition, work out how to use dictionaries ffs
def check_valid_game(input_game,
                     red_condition,
                     green_condition,
                     blue_condition):
    max_colours = get_max_colours(input_game)
    if red_condition >= max_colours.get('red') and green_condition >= max_colours.get('green') and blue_condition > max_colours.get('blue'):
        return True
    else:
        return False


def get_max_colours(input_string):
    max_colours = {'red': 0, 'green': 0, 'blue': 0}
    game = input_string[8:]
    sets = game.split(";")
    for set in sets:
        pairs = set.split(',')
        for pair in pairs:
            parts = pair.strip().split(' ')
            if len(parts) == 2:
                count, colour = int(parts[0]), parts[1]
                max_colours[colour] = max(max_colours[colour], count)
    return max_colours


if __name__ == "__main__":
    # print("Doing test example")
    # print(main(test_input))

    input_df = read_input_to_list("./input_data/day2-1.csv")
    print("RED = 12, GREEN = 13, BLUE = 14")
    for i in range(10):
        print(input_df[i])
        print(check_valid_game(input_df[i], 12, 13, 14))

    print("Main Problem")
    print(main(input_df))
