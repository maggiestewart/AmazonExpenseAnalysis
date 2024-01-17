#!/usr/bin/env python
# coding: utf-8

# Python Project - Data Analysis
# Analyzing data from Amazon.com to show the expense report including:
# total money spent, average cost per order, and monthly averages

# In[52]:

# imports pandas package; nickname pd
import pandas as pd

# DataFrame (df) stores Amazon data
# has pandas read the specified csv file as a Dataframe
df = pd.read_csv('my-amazon-orders.csv')

# looks ahead 5 rows of our data
df.head()


# In[53]:

# gives the dimensions of the DataFrame (rows, columns)
df.shape

# fill in all the NaN (not a number) values with 0
df = df.fillna(0)

# look ahead 5 rows
df.head()


# In[54]:

# data cleaning
# - replacing all $ in the "Total Charged", "Subtotal", "Shipping Charge", "Tax Charged" column with a space
# - converting to type float
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)
df["Subtotal"] = df["Subtotal"].str.replace('$','').astype(float)
df["Shipping Charge"] = df["Shipping Charge"].str.replace('$','').astype(float)

df.head()


# In[55]:

# Cost calculations using "Total Charged" column
df["Total Charged"].sum()
df["Total Charged"].mean()
df["Total Charged"].median()
df["Total Charged"].max()
df["Total Charged"].min()


# In[56]:

# Sales Tax (in "Tax Charged" column)
# - must clean the column first like we did for "Total Charged"

df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
df.head()


# In[57]:

# Tax Calculations
df["Tax Charged"].sum()
df["Tax Charged"].mean()
df["Tax Charged"].median()
df["Tax Charged"].max()
df["Tax Charged"].min()

# Overall Tax Rate
total_tax = df["Tax Charged"].sum()
total_amount = df["Total Charged"].sum()
total_tax_rate = (total_tax / total_amount) * 100

# using print("string {:.2f}".format())
# - formats float to 2 decimal places
# - modified to include a label and %
print("Total Tax Rate: {:.2f}%".format(total_tax_rate))


# In[58]:

# convert the dates to a datetime data type
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.head()


# In[80]:

# creates basic bar graph
# - passes desired X and Y axis columns as function parameters
# - rot rotates the x-axis labels (90 degrees)
# - figsize defines the size of the graph by width and height
df.plot.bar(x = "Order Date", y = "Total Charged", rot = 90, figsize = (20, 10), xlabel = 'Order Date', ylabel = 'Amount Charged')


# In[60]:

import calendar

df['Month'] = pd.to_datetime(df['Order Date']).dt.month
df['Month'] = df['Month'].apply(lambda x: calendar.month_name[x])

df.head()


# In[78]:

monthly_orders = df.groupby("Month").sum()["Total Charged"]

# df.plot.bar(x = "Month", y = "Total Charged", rot = 90, figsize = (20, 10))

monthly_orders.plot.bar(figsize = (20, 10), color = "#483d8b", xlabel = 'Month', ylabel = 'Amount Charged', rot=0)


# In[79]:

monthlyavg_orders = df.groupby("Month").mean()["Total Charged"]

monthlyavg_orders.plot.bar(figsize = (20, 10), color = "#483d8b", xlabel = 'Month', ylabel = 'Average Charged', rot = 0)


# In[64]:

# group orders by day (so each order is not listed but each date of purchase)
# - daily orders is a Series not a DataFrame
daily_orders = df.groupby("Order Date").sum()["Total Charged"]
daily_orders.head()

# show daily_orders as a bar graph
# - form is Series.plot.bar()
# - change color of bars since there is no meaning for the color
daily_orders.plot.bar(figsize = (20, 10), color = "#61D199", xlabel = 'Order Date', ylabel = 'Amount Charged')

