alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(text, shift, direction):
    if direction == "encode":
        print("Here's the encoded result: " + encrypt(text, shift))
    elif direction == "decode":
        print("Here's the decoded result: " + decrypt(text, shift))

def encrypt(original_text, shift_amount):
    shifted_text = ""
    for letter in original_text:
        if letter == " ":
            shifted_text += " "
        elif letter not in alphabet:
            shifted_text += letter
        else:
            shifted_text += alphabet[(alphabet.index(letter) + shift_amount) % 26]
    return shifted_text

def decrypt(encrypt_text, shift_amount):
    decrypt_text = ""
    for letter in encrypt_text:
        if letter == " ":
            decrypt_text += " "
        elif letter not in alphabet:
            decrypt_text += letter
        else:
            decrypt_text += alphabet[alphabet.index(letter) - shift_amount]
    return decrypt_text

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    play_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if play_again == 'no':
        break
    else:
        continue









