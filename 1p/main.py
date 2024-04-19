# Rodriguez Barragan Victor Gerardo
# Unidad 2
# 08/02/24

import pandas as pd # work with dataframes [tables]
import matplotlib.pylab as plt # graphs
import numpy as np # arrays
import seaborn as sns

src = "./imports.csv"
df = pd.read_csv(src, header=None)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

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

print(df.info()) # show the information of the dataframe

df.replace("?", np.nan, inplace=True) # replace "?" with NaN
print(df.head(5))

missing_data = df.isnull(); # check for missing data
print(missing_data.head(5)) # show the first 5 rows

for column in missing_data.columns.values.tolist(): # show the missing data of each column
    print(column) # show the column name
    print(missing_data[column].value_counts()) # show the count of missing data
    print("") # print a new line

horse_power = df["horsepower"] # show the horsepower column
print(horse_power) # show the horsepower column

horse_power_list = horse_power.tolist # convert the column to a list
print(horse_power_list) # show the list

agv_norm_loss = df["normalized_losses"].astype("float").mean(axis=0) # calculate the average of the normalized losses
print("Average of normalized losses: ", agv_norm_loss) # show the average of the normalized losses

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

# Rodriguez Barragan Victor Gerardo
# Unidad 2
# 20/02/24
print("--- Day 2 ---")
print("")
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head(20))
print(df.dtypes)

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized_losses"]] = df[["normalized_losses"]].astype("float")
df[["price"]] = df[["price"]].astype("float")
df[["peak_rpm"]] = df[["peak_rpm"]].astype("float")
print(df.dtypes)

print(df.head(5))
df["city_L/100km"] = 235 / df["city_mpg"]

print(df.head(5))
df["highway_mpg"] = 235 / df["highway_mpg"] # convert the highway_mpg to L/100km
df.rename(columns={"highway_mpg": "highway_L/100km"}, inplace=True) # rename the column
print(df.head(5))

df["length"] = df["length"] / df["length"].max() # normalize the length column
df["width"] = df["width"] / df["width"].max() # normalize the width column
df["height"] = df["height"] / df["height"].max() # normalize the height column
print(df[["length", "width", "height"]].head(5)) # show the first 5 rows of the columns

print(df.columns)
dummy_variable_1 = pd.get_dummies(df["fuel_type"]) # create a dummy variable for the fuel type
print(dummy_variable_1.head())
dummy_variable_1.rename(columns={"gas": "fuel_type_gas", "diesel": "fuel_type_diesel"}, inplace=True) # rename the columns
print(dummy_variable_1.head())

df=pd.concat([df, dummy_variable_1], axis=1)
df.drop("fuel_type", axis=1, inplace=True)
print(df.head())

dummy_variable_2 = pd.get_dummies(df["aspiration"])
dummy_variable_2.rename(columns={"std": "aspiration_std", "turbo": "aspiration_turbo"}, inplace=True)
print(df.head())
df=pd.concat([df, dummy_variable_2], axis=1)
df.drop("aspiration", axis=1, inplace=True)
print(df.head(5))

df.to_csv("clean_df.csv")

# show the correlation of the dataframe
print(df.dtypes)
print(df.corr())

df[['bore', 'stroke', 'compression_ratio', 'horsepower']].corr()
sns.regplot(x="engine_size", y="price", data=df)
plt.ylim(0,)
df[["engine_size", "price"]].corr()
sns.regplot(x="highway_L/100km", y="price", data=df)
sns.boxplot(x="peak_rpm", y="price", data=df)
