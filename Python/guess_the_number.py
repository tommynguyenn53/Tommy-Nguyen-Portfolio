import random
import art

print(art.logo3)
print("Welcome to the Number Guessing Game!")

list_of_numbers = list(range(1, 101))
random_number = random.choice(list_of_numbers)


def number_guesser(attempts, number_generated):
    answer_correctly = False

    while not answer_correctly and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number_generated:
            attempts -= 1
            print("Too high.")

            if attempts >= 1:
                print("Guess again.")

            elif attempts == 0:
                print(f"You've run out of guesses, you lose.\nThe number was {number_generated}.")

        elif guess < number_generated and attempts >= 1:
            attempts -= 1
            print("Too low.")

            if attempts >= 1:
                print("Guess again.")

            elif attempts == 0:
                print(f"You've run out of guesses, you lose.\nThe number was {number_generated}.")

        elif guess == number_generated:
            print(f"You got it! The answer is {number_generated}.")
            answer_correctly = True


print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choice == "easy":
    number_guesser(10, number_generated=random_number)

elif choice == "hard":
    number_guesser(5, number_generated=random_number)
