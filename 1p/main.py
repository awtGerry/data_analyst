# Rodriguez Barragan Victor Gerardo
# Unidad 2
# 08/02/24

import pandas as pd # work with dataframes [tables]
# import matplotlib.pylab as plt # graphs
import numpy as np # arrays

src = "./imports.csv"
df = pd.read_csv(src, header=None)

print(df.head(10)) # show the first 10 rows
print(df.head()) # show the first 5 rows

print(df.tail()) # show the last 5 rows

print(df.dtypes) # show the data types of each column

headers = [
        "symboling", "normalized_losses", "make",
        "fuel_type", "aspiration", "num_doors",
        "body_style", "drive_wheels", "engine_location",
        "wheel_base", "length", "width", "height",
        "curb_weight", "engine_type", "num_of_cylinders",
        "engine_size", "fuel_system", "bore", "stroke",
        "compression_ratio", "horsepower", "peak_rpm", "city_mpg",
        "highway_mpg", "price"
]

df.columns = headers # set the headers to the dataframe
print(df.head(5)) # show the first 5 rows

print(df.describe()) # show the statistics of the dataframe
print(df.describe(include="all"))

print(df.info())

df.replace("?", np.nan, inplace=True)
print(df.head(5))

missing_data = df.isnull();
print(missing_data.head(5))

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

horse_power = df["horsepower"]
print(horse_power)

horse_power_list = horse_power.tolist
print(horse_power_list)

agv_norm_loss = df["normalized_losses"].astype("float").mean(axis=0)
print("Average of normalized losses: ", agv_norm_loss)

avg_bore = df["bore"].astype("float").mean(axis=0)
print("Average of bore: ", avg_bore)

avg_horsepower = df["horsepower"].astype("float").mean(axis=0)
print("Average of horsepower: ", avg_horsepower)

avg_peak_rpm = df["peak_rpm"].astype("float").mean(axis=0)
print("Average of peak rpm: ", avg_peak_rpm)

df["peak_rpm"].replace(np.nan, avg_peak_rpm, inplace=True)
df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)
df["bore"].replace(np.nan, avg_bore, inplace=True)
df["normalized_losses"].replace(np.nan, agv_norm_loss, inplace=True)

print(df["num_doors"].value_counts())
df["num_doors"].replace(np.nan, "four", inplace=True)
print(df["num_doors"].value_counts())
print(df.head(20))
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head(20))
