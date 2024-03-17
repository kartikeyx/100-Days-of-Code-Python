# file = open("Day 24/mail-merge-project/Input/Letters/starting_letter.txt", "r")
# content = file.read()
# with open("Day 24/mail-merge-project/Input/Names/invited_names.txt", "r") as letter_names:
#   for x in letter_names:
#     # name = f"Letter_for_{x}"
#     # ot = open(f"Day 24/mail-merge-project/Output/Letter_for_{x}", "w")
#     with open(f"Day 24/mail-merge-project/Output/ReadyToSend/Letter_for_{x}.txt", "w") as ot:
#       new_content = content.replace("[name]", f"{x}")
#       ot.write(new_content)
#       # ot.close()
# file.close()
PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

