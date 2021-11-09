string = input("Enter a string : ")

num_A=0
num_a=0
num_0=0
num_char = 0

for i in string:
    if i.isupper():
        num_A+=1
    if i.islower():
        num_a+=1
    if i.isdigit():
        num_0+=1
    if i=='$' or i=='#' or i=='@':
        num_char+=1


c=0
if num_A>=1:
    c+=1
    print("Number of Upper Case Letters",num_A)
else:
    print("Not minimum number of upper case charters")

if num_a>=1:
    c+=1
    print("Number of Lower Case Letters",num_a)
else:
    print("Not minimum number of lower case charters")

if num_0>=1:
    c+=1
    print("Number of numbers",num_0)
else:
    print("Not minimum number of numbers")

if len(string)>=6:
    c+=1
    print("Length of password",len(string))
else:
    print("not matching minimum number of chars ")

if c==5:
    print("Password is valid")
else:
    print("Password is in valid")
