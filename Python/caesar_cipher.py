import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                position += shift_amount
                cipher_text += alphabet[position]

            else:
                cipher_text += char
        print(f"The encoded text is {cipher_text}.")

    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for char in cipher_text:
            if char in alphabet:
                position = alphabet.index(char)
                position -= shift_amount
                plain_text += alphabet[position]
            else:
                plain_text += char
        print(f"The decoded text is {plain_text}.")

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_amount=shift)


print(art.logo)

choice = True

while choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    choice = input("\nWould you look to continue? ")

    if choice == "yes":
        choice = True

    else:
        choice = False
