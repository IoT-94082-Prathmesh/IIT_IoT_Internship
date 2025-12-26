
import pandas as pd
import numpy as np

df = pd.read_csv('./50_Startups.csv')

#print(df.columns)
#df.info()

#print(df.head())

unique_states = df['State'].unique()

print(unique_states)

unique_state_numbers = np.array([1, 2, 3])

print(unique_state_numbers)

mapping = dict(zip(unique_states, unique_state_numbers))
df = df.replace(mapping)

print(df.head())

