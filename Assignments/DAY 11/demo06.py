
import pandas as pd

df = pd.read_csv('./50_Startups.csv')

#print(df)

#print(df.columns)

#print(df.head())
#print(df.tail())

#print(df.head(9))
#print(df.tail(7))

#df.info()

#print(df.describe())

print(df['RnD'])
