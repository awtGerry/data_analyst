import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from IPython.display import display

warnings.filterwarnings('ignore')
pd.options.display.float_format = '{:,.1f}'.format
# %matplotlib inline
plotsize = (13, 5)

url = './sample.xls'
df = pd.read_excel(url)
print(df.columns)

variables = ['Order Date', 'Category', 'Sales']
group_variables = variables[:2]
outcome_variable = variables[2]
base = df.groupby(group_variables)[outcome_variable].sum().reset_index()

print("Columns: ", base.columns)
print("Index: ", base.index)

print(base.dtypes)

for x in base.columns:
    print(x, type(base[x]), base[x].dtype)

order_date = np.array(base['Order Date'])
category = np.array(base['Category'])
sales = np.array(base['Sales'])

print("Order Date: ", order_date.dtype)
print("Category: ", category.dtype)
print("Sales: ", sales.dtype)

df_from_numpy = pd.DataFrame({'Order Date': order_date, 'Category': category, 'Sales': sales})

print(df_from_numpy.dtypes)

# order_date = df_from_numpy['Order Date']
order_date_daily = np.array(order_date, dtype='datetime64[D]')
print(order_date_daily)

order_date_monthly = np.array(order_date, dtype='datetime64[M]')
print(order_date_monthly)

print(len(np.unique(order_date_daily)))

print(base.head())
print("\n Unique Categories: ", base['Category'].unique())

base.set_index('Order Date', inplace=True)
print(base.head())
