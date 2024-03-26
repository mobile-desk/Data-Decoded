import pandas as pd

raw = pd.read_excel('raw.xlsx')

#remove rows containing empty cells

new_raw = raw.dropna()

print(new_raw)

#fill empty cells

c = raw.fillna('Na')

print(c)


#fill empty cells in a column

x = raw['Revenue'].fillna('$0')

print(x.head(5))

#discover duplicates
h = raw.duplicated()
print(h)

v = raw.drop_duplicates()
print(v)

