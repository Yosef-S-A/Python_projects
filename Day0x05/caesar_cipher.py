#!/usr/bin/env python3

# This is an implementation of Caesar cipher
# The Python script has both the encoding and decoding features

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue_value = 'yes'

while (continue_value == 'yes'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(message, shift_num, mode):
        '''Function that encodes a string based on a encoding shift number'''
        op_text = ""
        for x in message:
            if alphabet.__contains__(x):
                num = alphabet.index(x)
                if mode == 'encode':
                    if (num+shift_num) > (len(alphabet)-1):
                        num = (num+shift_num) - len(alphabet)
                        op_text += alphabet[num]
                    else:
                        op_text += alphabet[num+shift_num]
                elif mode == 'decode':
                    num = alphabet.index(x)
                    op_text += alphabet[num-shift_num]
                else:
                    return ("Wrong mode selected: choose 'encode' or 'decode'\n\n")
            else:
                op_text += x
        return("The {}d text is: {}\n\n".format(mode, op_text))

    print(caesar(text, shift, direction))

    continue_value = input(
        'Type "yes" if you want to go again. Otherwise type "no".\n')

print("Goodbye")
