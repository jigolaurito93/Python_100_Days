#TODO: Create a letter using starting_letter.txt
# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name
# Save the letter in the folder "ReadyToSend"

invitees = []
with open("Mail Challenge/Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

with open("Mail Challenge/Input/Letters/starting_letter.txt", "r") as default_letter:
    def_letter = default_letter.read()
    for name in name_list:
        with open(f"Mail Challenge/Output/ReadyToSend/letter_for_{name.strip()}.docx", "w") as send_letters:
            send_letters.write(def_letter.replace("[name]", name.strip()))


