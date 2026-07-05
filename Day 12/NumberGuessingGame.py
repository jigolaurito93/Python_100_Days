import random
import art

def guessing_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    secret_num = random.randint(2,99)
    print("Im thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        tries = 10
    elif level == 'hard':
        tries = 5
    
    game_over = False

    print(secret_num)

    for i in range(tries):
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == secret_num:
            print("You guessed the number!\n")
            break
        elif guess > secret_num:
            print("Too high.")
            if tries > 1:
                print("Guess again.\n")
            tries-=1
        elif guess < secret_num:
            print("Too low.")
            if tries > 1:
                print("Guess again.\n")
            tries-=1
    if tries == 0:
        print("You failed to guess the number.")
        print(f"The number is {secret_num}.\n")
    while input("Do you want to play again? 'y' or 'n': ") == "y":
        print("\n" * 20)
        guessing_game()
    quit()

    

    


guessing_game()
    