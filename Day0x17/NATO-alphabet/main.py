# This program creates a list of phonetic code words
# from a word that the user inputs.
# The phonetic code is created from a CSV file.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dict)

word = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in word]
print(output_list)
