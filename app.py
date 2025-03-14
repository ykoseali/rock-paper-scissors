import random
from collections import defaultdict

opponent_move_counts = defaultdict(lambda: {'R': 1, 'P': 1, 'S': 1})
previous_outcome = None
previous_opponent_move = None

def update_probabilities(outcome, opponent_move):
    global previous_outcome, previous_opponent_move
    
    if previous_outcome is not None and previous_opponent_move is not None:
        opponent_move_counts[(previous_outcome, previous_opponent_move)][opponent_move] += 1
    
    previous_outcome = outcome
    previous_opponent_move = opponent_move

def choose_next_move():
    if previous_outcome is None or previous_opponent_move is None:
        return random.choice(['R', 'P', 'S'])

    counts = opponent_move_counts[(previous_outcome, previous_opponent_move)]
    total = sum(counts.values())
    probabilities = {move: count / total for move, count in counts.items()}
    predicted_opponent_move = max(probabilities, key=probabilities.get)
    
    if predicted_opponent_move == 'R':
        return 'P' 
    elif predicted_opponent_move == 'P':
        return 'S'
    else:
        return 'R' 
def get_outcome(user_move, opponent_move):
    if user_move == opponent_move:
        return 'D'  
    elif (user_move == 'R' and opponent_move == 'S') or \
         (user_move == 'P' and opponent_move == 'R') or \
         (user_move == 'S' and opponent_move == 'P'):
        return 'W' 
    else:
        return 'L'  

def play_round(opponent_move):
    user_move = choose_next_move()
    outcome = get_outcome(user_move, opponent_move)
    update_probabilities(outcome, opponent_move)
    print(f"Opponent played: {opponent_move}, User played: {user_move}, Outcome: {outcome}")

def play_against_user():
    global previous_outcome, previous_opponent_move
    while True:
        user_move = input("Enter your move (R for Rock, P for Paper, S for Scissors, Q to quit): ").upper()
        if user_move == 'Q':
            break
        if user_move not in ['R', 'P', 'S']:
            print("Invalid move. Please enter R, P, S, or Q to quit.")
            continue

        opponent_move = choose_next_move()
        outcome = get_outcome(user_move, opponent_move)
        update_probabilities(outcome, opponent_move)
        print(f"You played: {user_move}, Opponent played: {opponent_move}, Outcome: {outcome}")

def main():
    while True:
        choice = input("Press 1 to simulate the game, 2 to play as the user, or Q to quit: ").strip()
        if choice == '1':
            opponent_moves = ['R', 'S', 'S', 'S', 'P', 'R', 'P', 'S', 'R']
            for opponent_move in opponent_moves:
                play_round(opponent_move)
        elif choice == '2':
            play_against_user()
        elif choice.upper() == 'Q':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or Q to quit.")

main()
