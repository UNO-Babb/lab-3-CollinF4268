#RPS.py
#Name: Collin Frederick
#Date: 2/9/25
#Assignment:RPS
import random

import random

def main():
    wins = 0
    ties = 0
    losses = 0

    while True:
        computer_choice = random.choice(['R', 'P', 'S'])

        
        user_choice = input("Enter R (Rock), P (Paper), or S (Scissors): ").upper()

        
        if user_choice not in ['R', 'P', 'S']:
            print("Invalid choice. Please enter R, P, or S.")
            continue

        if user_choice == computer_choice:
            print(f"Both chose {user_choice}. It's a tie!")
            ties += 1
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'P' and computer_choice == 'R') or \
             (user_choice == 'S' and computer_choice == 'P'):
            print(f"You chose {user_choice}, computer chose {computer_choice}. You win!")
            wins += 1
        else:
            print(f"You chose {user_choice}, computer chose {computer_choice}. You lose!")
            losses += 1

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break 

    print("\nGame Over! Here are your results:")
    print("Wins \t Ties \t Losses")
    print(wins, "\t", ties, "\t", losses)

if __name__ == '__main__':
    main()
