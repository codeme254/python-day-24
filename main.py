#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

for name in name_list:
    letter = content.replace("[name]", name)
    path = ".\\Output\\ReadyToSend\\invitation_for_"+name.strip('\n')+".txt"
    with open(f"{path}", mode="w") as ready_file:
        ready_file.write(letter)
    