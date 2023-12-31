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
# fewest number of cubes of each colour that could be in the bag


# Call function to see if we add the id
def main(input_games):
    powers = 0
    for input_game in input_games:
        powers += find_game_power(input_game)
    return powers


def find_game_power(input_game):
    max_colours = get_max_colours(input_game)
    power = 1
    for value in max_colours.values():
        power *= value
    return power


# Still need this!
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
    print("Doing test example")
    print(main(test_input))

    input_df = read_input_to_list("./input_data/day2-1.csv")

    print("Main Problem")
    print(main(input_df))
