#TODO: Create a letter using starting_letter.txt


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#TODO 1: Open read name file, create a list with readlines

PLACEHOLDER = "[name]"
with open("/Users/ismae/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as n:
    names_list = n.readlines()

final_names = []
for name in names_list:
    final_names.append(name.strip())
print(final_names)

#TODO 2: read message template , replace name with each strip(name[index]) in name_list

with open("/Users/ismae/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as n:
    letter_template = n.read().replace("/n","")

print(letter_template)

for name in final_names:
    new_letter = letter_template.replace(PLACEHOLDER,name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter_to_send:
        letter_to_send.write(new_letter)


