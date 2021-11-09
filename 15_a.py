string = input("Enter a string : ")
char_key   = {}
c=0
list_of_frequency = []
for char in string:
    for a in string:
        if a==char:
            c+=1
    char_key[char]     = c
    list_of_frequency.append(c)
    c=0

print(list_of_frequency,char_key)

for i in range(len(list_of_frequency)):
    for j in range(len(list_of_frequency)-1):
        if list_of_frequency[i]<list_of_frequency[j]:
            t = list_of_frequency[i]
            list_of_frequency[i] = list_of_frequency[j]
            list_of_frequency[j] = t



