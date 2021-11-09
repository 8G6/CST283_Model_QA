import matplotlib.pyplot as plt
from pandas import read_csv

df = read_csv('files/lb6.csv')

month       = df['month_number']
toothpaste  = df['toothpaste']

plt.xlabel("Month")
plt.ylabel("Sales")
plt.scatter(month,toothpaste,label='toothpaste')
plt.legend()
plt.show()