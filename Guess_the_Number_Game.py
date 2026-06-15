# Guess the Number Game :)

# Setting up python libraries
import random

# Introduction to the game
print("\nWelcome to Guess the Number!")
print("You have 6 rounds to get the highest score possible.")
print("For each round, you will have to guess a number between 1 and 10.")


# Setting up function that describes the game.
def guess_the_number():
    random_int = random.randint(1, 10)

    while True:
        user_num = input("\nGuess a number between 1 and 10: ")

        if not user_num.isdigit():
            print("\nPlease enter a valid number between 1 and 10.")
            continue

        user_num = int(user_num)

        if user_num < 1 or user_num > 10:
            print("\nPlease enter a valid number between 1 and 10.")
            continue

        break

    if user_num == random_int:
        print("\nAwesome, that's correct!")
        return 1
    else:
        print("\nThat's incorrect. Maybe next time!")
        print(f"The correct number was {random_int}.")
        return 0

# Setting up function to run the game.
def run_guess_the_number():
    score = 0

    user_response = input("\nAre you ready to start? (yes/no) ").lower()

    if user_response == "yes":
        print("Good luck!")

        for round_num in range(1, 7):
            print("\n----------------------------------------------------")
            print(f"\nRound {round_num}")
            score += guess_the_number()
            print(f"Score: {score}")

        if score < 3:
            print("\n----------------------------------------------------")
            print(f"\nYour final score is: {score}")
            print("Better luck next time!")

        elif score == 3:
            print("\n----------------------------------------------------")
            print(f"\nYour final score is: {score}.")
            print("Wow, half the points! Good work!")

        else:
            print("\n----------------------------------------------------")
            print(f"\nYour final score is: {score}.")
            print("That's an impressive score! Great work!")

        return True

    else:
        print("\nThat's ok. Maybe you can play next time!")
        return False

# Running the Guess the Number the first time.
played_game = run_guess_the_number()

# Asking the user if they want to play Guess the Number again.
while played_game:
    asking_again = input("\nWould you like to play again? (yes/no) ")

    if asking_again == "yes":
        print("Awesome! Glad you liked the game.")
        played_game = run_guess_the_number()

    elif asking_again == "no":
        print("\nThat's ok. I hope you enjoyed Guess the Number!")
        print("\n----------------------------------------------------")
        break

    else:
        print("Please enter yes or no.")