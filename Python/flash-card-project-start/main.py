from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:

    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")

else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background_image, image=card_back_img)

def is_known():
    data_dict.remove(current_card)

    data = pandas.DataFrame(data_dict)

    data.to_csv("data/words_to_learn", index=False)

    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=is_known)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
