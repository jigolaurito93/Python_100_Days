import pandas

alphabet = pandas.read_csv("NATO Alphabet/nato_phonetic_alphabet.csv")

nato_dict = {value.letter:value.code for (row, value) in  alphabet.iterrows()}

given_word = input("Enter a word: ").upper()


converted_letters = [nato_dict[letter] if letter in nato_dict else letter for letter in given_word]
print(converted_letters)