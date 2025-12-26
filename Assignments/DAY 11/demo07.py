
import pandas as pd

df = pd.read_csv("Salary_Data.csv")

#print(df)
#print(df.head())
#print(df.tail())

df['bonus'] = df['Salary'] * 0.10

#print(df.head())
#print(df.tail())

df.to_csv('Salary_Data_modified.csv')

df = df.drop(['bonus'], axis=1)

print(df.head())
print(df.tail())