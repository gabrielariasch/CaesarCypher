alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

game_on = True
while game_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: ")) % 26

    def caesar(message_text = text,shift_value = shift,direction_text = direction):
        end_text = ""
        if direction_text == "decode":
            shift_value *= -1
        for letter in message_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                newposition = position + shift_value
                end_text += alphabet[newposition]
            else:
                end_text += letter
        print(f"The {direction_text}d text is '{end_text}'")

    caesar(text,shift,direction)

    play_again = input("Type 'y' if you want to go again. Otherwise type 'n': ").lower()

    if play_again == 'n':
        print("Thanks for playing!")
        game_on = False
        break
    else:
        game_on = True

