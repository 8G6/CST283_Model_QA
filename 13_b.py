k=[]
pos=[]
neg=[]
sum=0
for i in range(4):
    k.append(float(input("Enter a number : ")))
    pos.append(k[i]) if k[i]>0 else neg.append(k[i])
    sum+=k[i]

print("Positive Numbers ",pos)
print("Negative Numbers ",neg)

avg = sum / 4

print("Avarage is %.2f " % avg)


