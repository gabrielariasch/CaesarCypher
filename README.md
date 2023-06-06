# CaesarCypher

The code defines a Caesar Cipher, which is a simple encryption method that shifts each letter in a message by a certain number of positions. The code first defines a list of all 26 letters in the alphabet, twice. This is done because the Caesar Cipher can be used to encrypt or decrypt messages, and the direction of encryption affects the shift value.

The code then defines a function called caesar. The function takes three arguments: message_text, shift_value, and direction_text. message_text is the message to be encrypted or decrypted. shift_value is the number of positions to shift each letter in the message. direction_text is the direction of encryption, either "encode" or "decode".

The function first checks the value of direction_text. If direction_text is "decode", the function multiplies shift_value by -1. This is because the shift value for decryption is the opposite of the shift value for encryption.

The function then loops through each letter in message_text. For each letter, the function checks if the letter is in the alphabet. If the letter is in the alphabet, the function finds the index of the letter in the alphabet. The function then adds shift_value to the index. If the index is greater than 25, the function subtracts 26 from the index. The function then gets the letter at the new index in the alphabet. The function then adds the letter to a new string called end_text.

The function then prints the end_text string.

The code then calls the caesar function. The code first gets the user to enter the direction of encryption, the message to be encrypted or decrypted, and the shift value. The code then calls the caesar function with the user's input.

The code then asks the user if they want to play again. If the user says yes, the code starts over. If the user says no, the code prints "Thanks for playing!" and exits.
