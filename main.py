# the easy has 10 attempts 
# the hard has 5 attempts
import random
from art import logo

def generate_random_number():
    return random.randint(1,100)
def game():
    print(logo)
    game_over = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty_level == 'hard':
        number_of_lives = 5
    elif difficulty_level == 'easy':
        number_of_lives = 10
    message = f"You have {number_of_lives} attempts remaining to guess the number"

    print(message)

    game_num = generate_random_number()

    while not game_over:
        # perform the check to make sure that it isn't yet game over 
        if number_of_lives == 0:
            game_over = True
            print(f"You've run out of guesses. You lose\nThe number was {game_num}")
            continue
        user_guess = int(input("Make a guess: "))
        if user_guess == game_num:
            # print that the user has won 
            print(f"You got it! The answer was {game_num}")
            game_over = True
        elif user_guess > game_num:
            number_of_lives -= 1
            print("Too high.\nGuess again.")
            print(f"You have {number_of_lives} attempts reamining to guess the number.")
        else:
            number_of_lives -= 1
            print("Too low.\nGuess again.")
            print(f"You have {number_of_lives} attempts remaining to guess the number.")

    # after the while loop has ended, we will ask the use if he wants to play again
    play_again = input("Do you want to play my number guessing game again. Input 'y' for yes and 'n' for no?: ") 
    if play_again == 'y':
        game()
    else:
        quit()

game()

        
