print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

total_people = int(input("How many people to split the bill? "))

tip_per_person = (total_bill * (tip_percentage / 100)) / total_people

total_per_person = round(((total_bill/total_people) + tip_per_person), 2)

print(f'Each person should pay: ${total_per_person}')
