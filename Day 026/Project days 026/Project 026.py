#TODO 1: Create dict for nato phonetic:

list_nato_alphabet = [n for n in open('nato_phonetic_alphabet.csv', 'r')]
dict_nato_alphabet = {str(n).split(',')[0]:str(n).split(',')[1].replace('\n', '') for n in list_nato_alphabet}

#TODO 2: Create the dict for answer:
input = input("Enter the words: ").upper()
list_final = []
for char in input:
    for (key, value) in dict_nato_alphabet.items():
        if char == key:
            list_final.append(value)

print(list_final)


#Cũng là 1 cách giải:
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# import pandas
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# #TODO 1. Create a dictionary in this format:
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)
