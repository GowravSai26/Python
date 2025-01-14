import random

def check_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    choices = ['rock', 'paper', 'scissors']
    score = 0

    for round in range(3):  # Play 3 rounds
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = check_result(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            score += 1

    print(f"Your final score is: {score}")

play_game()
