from turtle import shape
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/HP/Documents/KirstieData1.csv')

x, y, z = df.to_numpy().transpose()

plt.scatter(x, y, c=z, marker='s', s=250)
plt.show()


