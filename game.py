"""
This module implements a simple Rock, Paper, Scissors game.
"""

import random


def get_user_choice():
    """
    Prompt the user to enter their choice of rock, paper, or scissors.
    """
    choices = ['rock', 'paper', 'scissors']
    user_choice = ''
    while user_choice not in choices:
        user_choice = input(
            "Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
    return user_choice


def get_computer_choice():
    """
    Generate a random choice of rock, paper, or scissors for the computer.
    """
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game based on the user's choice and 
    the computer's choice.
    """
    if user_choice == computer_choice:
        return 'draw'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'


def play_game():
    """
    Play the Rock, Paper, Scissors game.
    """
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'draw':
            print("It's a draw!")
        elif winner == 'user':
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()
