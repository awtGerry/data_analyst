import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xls')

df_1 = df[['Customer Name', 'State', 'Sales', 'Profit']].sample(n=4)
df_2 = df[['Customer Name', 'State', 'Sales', 'Profit']].sample(n=4)
df_3 = df[['Customer Name', 'State', 'Sales', 'Profit']].sample(n=4)
print(df_1)

df_cat1 = pd.concat([df_1, df_2, df_3], axis=0)
print(df_cat1)

df_cat2 = pd.concat([df_1, df_2, df_3], axis=1)

df_1=df[['Customer Name', 'Ship Date', 'Ship Mode']][0:4]
df_2=df[['Customer Name', 'Product Name', 'Quantity']][0:4]
print(df_1)
print(df_2)

pd.merge(df_1, df_2, on='Customer Name', how='inner').drop_duplicates()
pd.merge(df_1, df_2, on='Customer Name', how='outer').drop_duplicates()

df_3 = df[['Customer Name', 'Product Name', 'Quantity']][2:6]
pd.merge(df_1, df_3, on='Customer Name', how='inner').drop_duplicates()
pd.merge(df_1, df_3, on='Customer Name', how='outer').drop_duplicates()

print(df_1)
df_1=df[['Customer Name', 'Ship Date', 'Ship Mode']][0:4]
df_1.set_index(['Customer Name'], inplace=True)
print(df_1)

df_2=df[['Customer Name', 'Product Name', 'Quantity']][2:6]
df_2.set_index(['Customer Name'], inplace=True)
print(df_2)

print(df_1.join(df_2, how='left').drop_duplicates())
print(df_1.join(df_2, how='right').drop_duplicates())
print(df_1.join(df_2, how='inner').drop_duplicates())
print(df_1.join(df_2, how='outer').drop_duplicates())
