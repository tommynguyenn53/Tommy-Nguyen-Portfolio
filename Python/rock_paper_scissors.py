import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choice = [rock, paper, scissors]

random_number = random.randint(0, 2)

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(choice[user_input])
print(f'Computer chose:\n{choice[random_number]}')


if user_input == random_number:
    print("It is a draw")

elif (user_input == 0 and random_number == 1) or (user_input == 1 and random_number == 2) or user_input == 2 and \
        random_number == 0:
    print("You lose")

elif (user_input == 1 and random_number == 0) or (user_input == 2 and random_number == 1) or user_input == 0 and \
        random_number == 2:
    print("You win")
