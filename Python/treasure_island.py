print('''
                    _____
                ___/     \___
               `-._)     (_,-`
                   \O _ O/
                    \ - /
                     `-(
                      ||
                     _||_
                    |-..-|
                    |/. \|
                    |\__/|
                  ._|//\\|_,
                  `-((  ))-'
                   __\\//__ gnv
                   >_ /\ _<,
                     '  '
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure")

print("In this treasure hunt, if you pick right you will get what you seek for. Else, you will LOSE!")

first_option = input("Would you like to go left or right? Pick wisely. ").lower()

if first_option == "left":
    print("Good choice")
    print("Now, you've entered into a room filled with water, the water will fall if you choose to wait? Are you "
          "desperate for this treasure or are you willing to wait...")

    second_option = input("Now choose. Swim or Wait? ").lower()

    if second_option == "wait":
        print('Good patience.\nThe water starts draining down after your five minute wait.\nYou are greeted to three '
              'different doors. Red, Blue & Yellow. Now one of the doors holds this treasure that you have been '
              'seeking for. You have done well so far. Now, it is time for your final choice.''')

        third_option = input("What will it be? Red, Blue or Yellow? ")

        if third_option == "yellow":
            print("Yellow it is (the door opens...). Congratulations, you have found the treasure. Open it and show"
                  "to yourself that you have won!")

        elif third_option == "blue":
            print("Blue it is ... Well unfortunately, there is nothing in here so that means you are stuck in here "
                  "to suffocate. Game Over.")

        elif third_option == "red":
            print("Red it is ... Well unfortunately, there is nothing in here so that means you are stuck in here "
                  "to burn. Game Over.")

    else:
        print("You triggered a sensor in the water, the water is struck with electricity.\nDon't be too desperate "
              "next time.\nGame Over. ")


else:
    print("There is nothing there... Boom, Game Over.")
