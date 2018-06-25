import numpy as np
import pandas as pd
import seaborn as sns
k1 = 5
k2 = 8
k3 = k2*k1
df = pd.DataFrame({
    'qwerty' : [k1,  '0', '0',  4, 'w'],
    'asdfgh' : ['1', '1', '1',  5, 'w'],
    'zxcvbn' : [k3,  '2',  k2,  6, 'w'],
    '1'      : [1,    2,    3,  7,  9 ],
    '2'      : [10,  11,   12, 13,  14]
}, index = ['Q1', 'Q2', k3, '9', 98])

print(df)

print(' ') 

print(df['asdfgh'])

print(' ')

print(df.loc[k3])

print(' ')

print(df.loc[['Q1', 'Q2'], 'qwerty'])

print(' ')

print(df.loc['Q1': '9', :])

df['3'] = df['1'] * df['2'] /100

print('')

print(df)

del df['1']

print('')

print(df)
