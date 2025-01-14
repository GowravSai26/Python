import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Select number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players")
    else:
        print("Invalid input, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

# Main game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1. Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your current score is", current_score)

        player_scores[player_idx] += current_score
        print("Your final score is", player_scores[player_idx])

        # Check if the player reached or exceeded the max score
        if player_scores[player_idx] >= max_score:
            break
    else:
        continue
    break

# End of game - print final scores and determine the winner
print("\nGame Over!")
print("Final Scores:")
for i, score in enumerate(player_scores):
    print(f"Player {i + 1}: {score}")

# Determine the winner
winning_score = max(player_scores)
winners = [i + 1 for i, score in enumerate(player_scores) if score == winning_score]
if len(winners) > 1:
    print(f"It's a tie between players: {', '.join(map(str, winners))}!")
else:
    print(f"Player {winners[0]} wins with a score of {winning_score}!")