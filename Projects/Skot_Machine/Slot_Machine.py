import random

MAX_LINES = 3
MAX_BET_AMOUNT = 100
MIN_BET_AMOUNT = 1

GRID_ROWS = 3
GRID_COLS = 3

symbol_quantity = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_multiplier = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def calculate_winnings(spin_result, num_lines, bet_per_line, multipliers):
    total_winnings = 0
    winning_rows = []
    for row in range(num_lines):
        selected_symbol = spin_result[0][row]
        for col in spin_result:
            if col[row] != selected_symbol:
                break
        else:
            total_winnings += multipliers[selected_symbol] * bet_per_line
            winning_rows.append(row + 1)

    return total_winnings, winning_rows

def generate_slot_spin(rows, cols, symbols):
    symbol_pool = []
    for symbol, count in symbols.items():
        symbol_pool.extend([symbol] * count)

    generated_columns = []
    for _ in range(cols):
        column_symbols = []
        temp_pool = symbol_pool[:]
        for _ in range(rows):
            chosen_symbol = random.choice(temp_pool)
            temp_pool.remove(chosen_symbol)
            column_symbols.append(chosen_symbol)
        generated_columns.append(column_symbols)

    return generated_columns

def display_slot_machine(slot_result):
    for row in range(len(slot_result[0])):
        row_output = " | ".join([col[row] for col in slot_result])
        print(row_output)

def ask_for_deposit():
    while True:
        deposit_amount = input("Enter deposit amount: $")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                return deposit_amount
            else:
                print("Deposit must be greater than $0.")
        else:
            print("Please enter a valid number.")

def get_lines_to_bet():
    while True:
        chosen_lines = input(f"Choose the number of lines to bet on (1-{MAX_LINES}): ")
        if chosen_lines.isdigit():
            chosen_lines = int(chosen_lines)
            if 1 <= chosen_lines <= MAX_LINES:
                return chosen_lines
            else:
                print(f"Please select a line count between 1 and {MAX_LINES}.")
        else:
            print("Input must be a number.")

def get_bet_per_line():
    while True:
        bet_input = input(f"Enter your bet per line (${MIN_BET_AMOUNT}-${MAX_BET_AMOUNT}): $")
        if bet_input.isdigit():
            bet_input = int(bet_input)
            if MIN_BET_AMOUNT <= bet_input <= MAX_BET_AMOUNT:
                return bet_input
            else:
                print(f"Bet amount must be between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}.")
        else:
            print("Please enter a valid number.")

def play_round(player_balance):
    lines = get_lines_to_bet()
    while True:
        bet_per_line = get_bet_per_line()
        total_wager = bet_per_line * lines

        if total_wager > player_balance:
            print(f"Insufficient funds! Your balance is ${player_balance}.")
        else:
            break

    print(f"Betting ${bet_per_line} on {lines} lines, for a total of ${total_wager}.")

    slot_spin = generate_slot_spin(GRID_ROWS, GRID_COLS, symbol_quantity)
    display_slot_machine(slot_spin)
    winnings, winning_rows = calculate_winnings(slot_spin, lines, bet_per_line, symbol_multiplier)
    print(f"You won: ${winnings}. Winning lines:", *winning_rows)
    return winnings - total_wager

def main():
    balance = ask_for_deposit()
    while True:
        print(f"Current balance: ${balance}")
        play_response = input("Press Enter to spin, or 'q' to quit: ")
        if play_response.lower() == 'q':
            break
        balance += play_round(balance)

    print(f"Game over! You left with ${balance}")

main()
