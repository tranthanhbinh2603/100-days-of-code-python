f = open("file2.txt", "r")
list_1 = [int(n) for n in f.readlines()]

f2 = open("file1.txt", "r")
result = [int(n) for n in f2.readlines() if int(n) in list_1]

# Write your code above 👆

print(result)


