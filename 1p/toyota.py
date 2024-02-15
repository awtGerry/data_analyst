# Rodriguez Barragan Victor Gerardo
# Evaluacion
# 15/02/24

import pandas as pd # work with dataframes [tables]
# import matplotlib.pylab as plt # graphs
import numpy as np # arrays

src = "./toyota.csv"
df = pd.read_csv(src, header=None)
print(df.head(10)) # show the first 10 rows

# Delete the first row
# df = df.iloc[1:]
df = df.drop([0], axis=0)
print(df.head(10)) # show the first 10 rows

# Replace the header (NaN) for id
headers = [
        "id", "price", "age",
        "km", "fuel_type", "hp",
        "met_color", "automatic", "cc",
        "doors", "weight"
]
df.columns = headers # set the headers to the dataframe
print(df.head(10)) # show the first 5 rows

# drop id column
df.drop(["id"], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head(10)) # show the first 5 rows

df["met_color"].replace(np.nan, 0, inplace=True)
print(df.head(10))

# check in doors the type of the column
print(df["doors"].value_counts())
# replace all non-numeric values for their respective numeric value
non_numeric = ["three", "four", "five"]
numeric = [3, 4, 5]
for i in range(0, len(non_numeric)):
    df["doors"].replace(non_numeric[i], numeric[i], inplace=True)
print(df.head(10))

# replace hp all ?* values to NaN
avg_hp = df["hp"].astype("float").mean(axis=0)
print("Average of hp: ", avg_hp)
