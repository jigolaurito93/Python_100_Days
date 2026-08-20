import pandas

alphabet = pandas.read_csv("NATO Alphabet/nato_phonetic_alphabet.csv")

nato_dict = {value.letter:value.code for (row, value) in  alphabet.iterrows()}

while True:

    given_word = input("Enter a word: ").upper()
    
    # converted_letters = [nato_dict[letter] if letter in nato_dict else letter for letter in given_word]
    
    try:
        converted_letters = [nato_dict[letter] for letter in given_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(converted_letters)
        break