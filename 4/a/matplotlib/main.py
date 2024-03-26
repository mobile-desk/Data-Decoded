import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(9,3), dpi=150)
#basic graph
g = plt.plot([1,2,3], [2,4,6], label="d", color="#0affff", linewidth=2, marker='.', markersize=10, markeredgecolor='gold', linestyle='--')
c = np.arange(0,4.5,0.5)
h = plt.plot(c, c**2, label="np")
plt.legend()

plt.title("A Graph", fontdict={'fontsize': 20, 'fontname': 'Comic Sans MS'})
plt.xlabel('x Axis')
plt.ylabel('y Axis')

#plt.xticks([0,1,2,3,4,5])
#plt.yticks([0,1,2,3,4,5,6])

plt.savefig('fig.png', dpi=150)
plt.show()