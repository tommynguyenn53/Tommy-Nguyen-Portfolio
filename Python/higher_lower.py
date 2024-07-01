import random
import higher_lower_extra

data = higher_lower_extra.data

game_over = False
score = 0
random_person_a = random.choice(data)

print(higher_lower_extra.logo)

while not game_over:
    random_person_b = random.choice(data)
    while random_person_b == random_person_a:
        random_person_b = random.choice(data)

    followers_a = int(random_person_a['follower_count'])

    followers_b = int(random_person_b['follower_count'])

    print(
        f"Compare A: {random_person_a['name']}, a {random_person_a['description']}, from {random_person_a['country']}")

    print(higher_lower_extra.vs)

    print(
        f"Compare B: {random_person_b['name']}, a {random_person_b['description']}, from {random_person_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if followers_a > followers_b and choice == "a":
        score += 1
        print(f"You're right! Current score: {score}")

    elif followers_a < followers_b and choice == "b":
        score += 1
        print(f"You're right! Current score: {score}")
        random_person_a = random_person_b
        followers_a = followers_b

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
