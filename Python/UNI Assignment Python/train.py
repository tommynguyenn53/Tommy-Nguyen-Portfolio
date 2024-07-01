'''
Answer for Question 5 - The Training Again from Assignment 1.

Author:
SID:
unikey:
'''


def main():
    print("Larry: I'm Larry. I'll be your hunting instructor.")
    print("Larry: Let's go to the Meadow to begin your training!")
    travel = input("Press Enter to travel to the Meadow...")
    if travel and ord(travel[0]) == 27:
        quit()
    else:
        print("Travelling to the Meadow...")
        print("Larry: This is your camp. Here you'll set up your mouse trap.")
    while True:
            trap = input(
                "Larry: Let\'s get your first trap...\nPress Enter to view traps that Larry is holding...")
            if trap and ord(trap[0]) == 27:
                break
            else:
                print(f'Larry is holding...\nLeft: High Strain Steel Trap\nRight: Hot Tub Trap')
                hand = input(f'Select a trap by typing "left" or "right": ').strip().lower()
                if hand == 'left':
                    print('Larry: Excellent choice.\nYour "High Strain Steel Trap" is now set!')
                    print("Larry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!")
                elif hand == 'right':
                    print('Larry: Excellent choice.\nYour "Hot Tub Trap" is now set!')
                    print("Larry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!")
                elif hand and ord(hand[0]) == 27:
                    break
                else:
                    print('Invalid command! No trap selected.\nLarry: Odds are slim with no trap!')

                print("Sound the horn to call for the mouse...")
                sound_answer = input(f'Sound the horn by typing "yes": ').strip().lower()
                if hand == "left" and sound_answer == "yes":
                    print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
                elif hand == "right" and sound_answer == "yes":
                    print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
                elif hand == "left" and sound_answer != "yes":
                    print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
                elif hand == "right" and sound_answer != "yes":
                    print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
                elif hand != "left" and sound_answer == "yes":
                    print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
                elif sound_answer and ord(sound_answer[0]) == 27:
                    break
                else:
                    print("Nothing happens.")
                restart = input(f'\nPress Enter to continue training and "no" to stop training: ').strip().lower()
                if restart == "":
                    continue
                if restart == "no":
                    break
                elif restart and ord(restart[0]) == 27:
                    break

if __name__ == '__main__':
    main()

