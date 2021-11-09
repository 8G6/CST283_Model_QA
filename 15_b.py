limit = int(input('Enter a limit : '))
k=[]
for i in range(limit):
    k.append(int(input("Enter number : ")))

b=len(k)

for i in range(b):
    for j in range(b-1):
        if k[i]<k[j]:
            t = k[i]
            k[i] = k[j]
            k[j] = t

print(k)
