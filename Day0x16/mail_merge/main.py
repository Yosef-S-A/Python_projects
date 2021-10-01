#!/usr/bin/python3

with open("Input/Letters/starting_letter.docx", mode="r") as letter_draft:
    letter = letter_draft.read()
    with open("Input/Names/invited_names.txt", mode="r") as names:
        for name in names.readlines():
            with open("Output/ReadyToSend/letter_for_{}.docx".format(name.strip()), mode="w") as complete_letter:
                new_letter = letter.replace("[name]", name.strip())
                complete_letter.write(new_letter)
