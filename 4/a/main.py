import pandas as pd
import matplotlib.pyplot as plt


c = pd.read_csv('pandas//employee.csv')
plt.style.use('fivethirtyeight')
x = c['Age']
y = c['Salary']

bars = plt.scatter(x, y, c=y, s=x)

cbar = plt.colorbar()
cbar.set_label('Salary')

plt.xlabel('Age')
#plt.ylabel('Salary')
plt.xticks([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47])

plt.show()
