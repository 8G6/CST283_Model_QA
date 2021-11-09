number  = input("Enter a number : ")
sum=0
rev_num = number[::-1]
for i in number:
    sum+=int(i)
print(' The reverse number is :',rev_num,'\n','The sum is :',sum)