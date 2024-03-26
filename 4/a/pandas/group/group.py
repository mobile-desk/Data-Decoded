import pandas as pd

language = pd.read_csv('language.csv')

d = pd.DataFrame(language)


c = d.groupby(['Main Field']).mean(numeric_only=True)

#c = d.aggregate(['sum', 'min'])
c.to_excel('sum.xlsx')