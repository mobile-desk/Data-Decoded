#### Bar Chart
import matplotlib.pyplot as plt

a = ['A', 'B', 'C']
b = [3,6,9]

bars = plt.bar(a, b)
bars[0].set_hatch('.')
plt.show()