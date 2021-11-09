import matplotlib.pyplot as plt
from numpy import arange
from pandas import read_csv

df = read_csv('files/lb6.csv')

month       = df['month_number']
facecream   = df['facecream']
facewash    = df['facewash']



plt.xlabel("Month")
plt.ylabel("Sales")
plt.bar(month,facecream,label="Facecream",width=0.4)
plt.bar(month+0.4,facewash,label="Facewash",width=0.4)
plt.xticks(month+0.4/2)
plt.legend()
plt.show()