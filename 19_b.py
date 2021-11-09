from pandas import read_csv

df = read_csv('files/auto.csv')

names   = df['name']
milage  = df['mpg']
prices   = df['price']
companys = df['company']

print('Total cars of all compny ',names)
print('Avarge of all milages in mile per galon',sum(milage)/len(milage))

l=len(companys)

dit = {}

for i in range(l):
    arr = []
    for j in range(l):
        if companys[i]==companys[j]:
            arr.append(prices[j])
        dit[companys[i]]=arr

for i in dit.keys():
    print("highest price offerd by ",i,"is ",max(dit[i]),"euros")
    