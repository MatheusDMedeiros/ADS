import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv('cliente.csv')


print(a.head())

plt.plot(a['bps'])
plt.show()