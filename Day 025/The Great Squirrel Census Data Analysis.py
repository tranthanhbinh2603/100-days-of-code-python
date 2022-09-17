import pandas
from collections import Counter

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#print(data["Primary Fur Color"].to_dict())
color = data["Primary Fur Color"].to_dict()
gray = 0
black = 0
cinnamon = 0
n = range(1, len(color))
for n in color:
    #print(color[n])
    if color[n] == 'Gray':
        gray+=1
    if color[n] == 'Black':
        black+=1
    if color[n] == 'Cinnamon':
        cinnamon+=1

dict = {
    "Furcolor": ["gray", "black", "cinnamon"],
    "Count": [gray, black, cinnamon]
}
dict_pandas = pandas.DataFrame(dict)
dict_pandas.to_csv("squirrel_count.csv")
