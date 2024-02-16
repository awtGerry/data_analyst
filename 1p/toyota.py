# Rodriguez Barragan Victor Gerardo
# Evaluacion
# 15/02/24

import pandas as pd # work with dataframes [tables]
# import matplotlib.pylab as plt # graphs
import numpy as np # arrays

src = "./toyota.csv"
df = pd.read_csv(src, header=None)
print(df.head(10)) # show the first 10 original rows

# Delete the first row
df = df.drop([0], axis=0) # delete the first row (non-data id)

# Replace the headers for better understanding
headers = [
        "id", "price", "age",
        "km", "fuel_type", "hp",
        "met_color", "automatic", "cc",
        "doors", "weight"
]
df.columns = headers # set the headers to the dataframe
# print(df.head(10)) # show the new headers

# drop id column
df.drop(["id"], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)
# print(df.head(10)) # show the result

df["met_color"].replace(np.nan, 0, inplace=True) # replace NaN for 0
print(df.head(10))

# check in doors the type of the column
# print(df["doors"].value_counts())
# replace all non-numeric values for their respective numeric value
non_numeric = ["three", "four", "five"]
numeric = [3, 4, 5]
for i in range(0, len(non_numeric)):
    df["doors"].replace(non_numeric[i], numeric[i], inplace=True)
# print(df["doors"].value_counts())

# Get the ?** values in the hp column
print("-- HP --")
print(df["hp"].value_counts())
print("--------")
# replace the ?** values for the mean of the column
df["hp"].replace("????", np.nan, inplace=True)
avg_hp = df["hp"].astype(float).mean() # get the average of the column
df["hp"].replace(np.nan, avg_hp, inplace=True)
df["hp"] = df["hp"].astype(int) # re-convert the column

# Check the fuel_type column for NaN values
print(df["fuel_type"].value_counts())
# replace NaN for the most common value
df["fuel_type"].replace(np.nan, "Petrol", inplace=True)

# Replace km ?** for the mean of the column
# check the column for the ?** values
print("-- KM --")
print(df["km"].value_counts())
print("--------")
df["km"].replace("??", np.nan, inplace=True)
avg_km = df["km"].astype(float).mean()
df["km"].replace(np.nan, avg_km, inplace=True)
df["km"] = df["km"].astype(int)

print(df.head(10)) # show the result
