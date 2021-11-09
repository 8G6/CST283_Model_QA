import matplotlib.pyplot as plt
from pandas import read_csv

df = read_csv('files/lb6.csv')

month       = df['month_number']
toothpaste  = df['toothpaste']
facecream   = df['facecream']
moisturizer = df['moisturizer']
facewash    = df['facewash']
shampoo     = df['shampoo']
bathingsoap = df['bathingsoap']

toothpaste  = sum(toothpaste)
facecream   = sum(facecream)
moisturizer = sum(moisturizer)
facewash    = sum(facewash)
shampoo     = sum(shampoo)
bathingsoap = sum(bathingsoap)

y = [toothpaste, facecream, moisturizer, facewash, shampoo, bathingsoap]

labels = ['toothpaste', 'facecream', 'moisturizer', 'facewash', 'shampoo', 'bathingsoap']

plt.title('Sales of products')
plt.pie(y, labels=labels, autopct='%1.1f%%')


plt.show()