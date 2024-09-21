import random

def guess_the_number():
    secret_number = random.randint(1, 10)  # Generate random number between 1 and 10
    attempts = 0  # Initialize attempts counter

    while True:
        guess = int(input("Guess the secret number (between 1 and 10): "))  # Get user input and convert to integer
        attempts += 1  # Increment the number of attempts

        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations, you guessed it in {attempts} attempts!")
                break  # Exit loop when guessed correctly
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

# Main loop to allow the user to play again
while True:
    guess_the_number()
    play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask if the user wants to play again
    if play_again != 'yes':
        print("Thanks for playing!")
        break
