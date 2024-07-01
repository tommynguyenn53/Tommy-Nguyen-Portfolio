import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

end = False

while not end:

    try:
        user_input = input("What name would you like to use? ").upper()
        final = [nato_dict[letter] for letter in user_input]

    except KeyError:
        print("Sorry only letters in the alphabet please.")

    else:
        print(final)
        end = True
