import pandas as pd

#load csv file
employees = pd.read_csv('employee.csv')

print(employees.head(3))

###read data

#get header
print(employees.columns)

##get data by column
print(employees['Name'])

#get multiple columns
print(employees[['Name', 'Age']])

#get rows
print(employees.iloc[1:6])


print('----------------------------------------------------------------')

#for index, row in employees.iterrows():
#    print(index, row)


#find specific data
print(employees.loc[employees['Name'] == 'John'])


print('sorting and describing')
print(employees.describe())

print(employees.sort_values('Name'))


### Modifying
#add new column
employees['Interest'] = employees['Salary'] * 0.2



#drop column
employees = employees.drop(columns=['Start_Date'])

print(employees)
#save file
employees.to_csv('new.csv')
employees.to_excel('new.xlsx', index=False)
employees.to_csv('modified/new.txt', index=False, sep='\t')

print(employees.loc[(employees['Name'] == 'John Doe') & (employees['Age'] == 35)])

#contains
print(employees.loc[(employees['Name'].str.contains('John'))])



