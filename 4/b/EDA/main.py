import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### Setting up graph
plt.style.use('ggplot')
#pd.set_option('max_columns', 200)

sales = pd.read_excel('sales.xlsx')
print(sales)