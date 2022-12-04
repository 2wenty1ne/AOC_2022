# Enemy        Response   Points   Round 2  Points
# A Rock       X          1        Lose     0
# B Paper      Y          2        Draw     3
# C Scissors   Z          3        Win      6

points = {"X": 1, "Y": 2, "Z": 3}

def strategy(enemy_move, strategy_input):
    if enemy_move == "A": #Rock
        if strategy_input == "X": # Lose -> Scissors
            return determine_winner(enemy_move, "Z")
        elif strategy_input == "Y": # Draw -> Rock
            return determine_winner(enemy_move, "X")
        elif strategy_input == "Z": # Win -> Paper
            return determine_winner(enemy_move, "Y")

    elif enemy_move == "B": # Paper
        if strategy_input == "X": # Lose -> Rock
            return determine_winner(enemy_move, "X")
        elif strategy_input == "Y": # Draw -> Paper
            return determine_winner(enemy_move, "Y")
        elif strategy_input == "Z": # Win -> Scissors
            return determine_winner(enemy_move, "Z")

    elif enemy_move == "C": # Scissors
        if strategy_input == "X": # Lose -> Paper
            return determine_winner(enemy_move, "Y")
        elif strategy_input == "Y": # Draw -> Scissors
            return determine_winner(enemy_move, "Z")
        elif strategy_input == "Z": # Win -> Rock
            return determine_winner(enemy_move, "X")


def determine_winner(enemy_move, response):
    if enemy_move == "A": #Rock
        if response == "Y": #Paper
            # Win
            return 6 + points[response]
        elif response == "X": #Rock
            # Draw
            return 3 + points[response]
        elif response == "Z": #Scissors
            # Lose
            return 0 + points[response]

    elif enemy_move == "B": #Paper
        if response == "Z": #Scissors
            # Win
            return 6 + points[response]
        elif response == "Y": #Paper
            # Draw
            return 3 + points[response]
        elif response == "X": #Rock
            # Lose
            return 0 + points[response]

    elif enemy_move == "C": #Scissors
        if response == "X": #Rock
            # Win
            return 6 + points[response]
        elif response == "Z": #Scissors
            # Draw
            return 3 + points[response]
        elif response == "Y": #Paper
            # Lose
            return 0 + points[response]



with open("data.txt", "r") as data:
    data_lines = [x.strip() for x in data.readlines()]

point_sum = 0
point_sum_2 = 0

for game_round in data_lines:
    enemy_move = game_round[0]
    response = game_round[-1]
    strategy_input = game_round[-1]
    point_sum = point_sum + determine_winner(enemy_move, response)
    point_sum_2 = point_sum_2 + strategy(enemy_move, strategy_input)


print(f'Round 1 Points: {point_sum}')
print(f'Round 2 Points: {point_sum_2}')
