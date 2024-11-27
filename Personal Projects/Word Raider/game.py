import random

# Game setup
game_title = "It's time to Guess!!!"

misplaced_letters = []  # Correct letters in the wrong place
incorrect_letters = []  # Letters not in the word
max_turns = 6
current_turns = 0
game_over = False

# Load words and select a random word
word_bank = []
with open('words.txt', 'r') as f:
    word_bank = [line.strip() for line in f]

random_word = random.choice(word_bank)

# Start game
print(game_title)
print(f'The number of letters you will need to guess is {len(random_word)}!')
print(f'You have {max_turns} turns to guess the word.')

# Game loop
while not game_over:
    print(f'\nTurns left: {max_turns - current_turns}')
    the_guess = input("Enter your guess: ").strip().lower()

    # Validate input
    if len(the_guess) != len(random_word):
        print(f"Your guess must be {len(random_word)} letters long.")
        continue  # Restart the loop without incrementing turns

    if not the_guess.isalpha():
        print("Your guess must contain only alphabetic characters.")
        continue  # Restart the loop without incrementing turns

    # Increment turn count
    current_turns += 1

    # Index variable initialized outside the loop
    index = 0
    feedback = ""  # To store letters and underscores for current guess feedback

    # Loop through each character in the player's guess
    for letter in the_guess:
        if letter == random_word[index]:
            feedback += letter  # Correct letter in the correct position
        elif letter in random_word and letter != random_word[index]:
            misplaced_letters.append(letter)  # Correct letter, wrong position
            feedback += "_"
        else:
            incorrect_letters.append(letter)  # Incorrect letter
            feedback += "_"

        index += 1  # Update index to move to the next position

    # Print feedback for the current guess
    print(feedback)  # Shows letters or underscores on the same line

    # Check for correct guess
    if the_guess == random_word:
        print(f"Congratulations! You guessed the word: {random_word}")
        game_over = True
    elif current_turns >= max_turns:
        print(f"Game over! The correct word was: {random_word}")
        game_over = True
