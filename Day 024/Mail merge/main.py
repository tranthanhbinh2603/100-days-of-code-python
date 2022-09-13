#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", mode='r') as r:
    str_original = r.read()

with open("./Input/Names/invited_names.txt", mode='r') as r:
    list = r.readlines()

for name in list:
    str1 = str_original
    str2 = str1.replace("[name]", str(name.replace('\n','')))
    with open("./Output/ReadyToSend/letter_for_" + name.replace('\n','') + ".txt", mode='w') as w:
        w.write(str2)