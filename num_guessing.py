import random

def guess_the_number():
    
    secret_number = random.randint(1, 10)
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 10.")
    print("Try to guess it!")
    
    attempts = 0
    while True:
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

# Call the function to start the game
guess_the_number()
