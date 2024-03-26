import seaborn as sns
import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np




"""

['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 
'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 
'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']

"""

#tips = sns.load_dataset('tips')
#print(tips)


#scatter plots

### sns.scatterplot(x='tip', y='total_bill', data=tips, hue='day', size='size')
#sns.jointplot(x='tip', y='total_bill', data=tips, kind='hex', cmap='YlGnBu')
#sns.barplot(x='sex', y='tip', data=tips, palette='YlGnBu')
#sns.stripplot(x='day', y='tip', data=tips, hue='sex', palette='YlGnBu', dodge=True)
#sns.boxplot(x='day', y='tip', data=tips, hue='sex', palette='YlGnBu')
### sns.histplot(tips['tip'], kde= True, bins=15)


nnew = pd.read_csv('new.csv')
#sns.pairplot(nnew, x_vars=['Age', 'Salary'], y_vars=['Age', 'Interest'])
#nnew.corr()
#sns.heatmap(nnew.corr, annot=True, cmap="YlGnBu")


#s = sns.load_dataset('titanic')
#print(s.corr(numeric_only=True))
sns.set_theme(rc={'figure.figsize':(5,6)})

#sns.heatmap(nnew.corr(numeric_only=True), annot=True, cmap='YlGnBu')
sns.clustermap(nnew.drop('Name', axis=1))

plt.show()