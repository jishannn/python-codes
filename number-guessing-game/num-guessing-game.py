import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")


    # This generates a random number between 1 and 100.
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # This gets the user's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        # It would check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

def main():
    start_game()
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            start_game()
        elif play_again == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
