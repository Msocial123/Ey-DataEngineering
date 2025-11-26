# pandas(python Data Analysis Library) --> open source library
# its is used to manipulate , cleaning, analysis of the data
# its built on top of Numpy --> widely used in data_eng, data_science, ETL
from tkinter.constants import BROWSE

# Why pandas important?:
# --> it is very usefull to clean messy data
#-->its is used to read data from multiple source(csv,excel,json,databases,API)
#-->transforming the data before loading into DW( snowflake,redshit, bigquery)
#--> used to build ETL pipelines

# how to install:
# terminal -->pip install pandas
# import pandas pd
# series --A 1D labeled array(column in excel)
import pandas as pd



# s=pd.Series([10,20,30,40],name='department')
# print(s)
# Dataframe:- A 2D labeled data structure (like excel, sql)
# data={
#     "Employee":["amit","kumar","raju"],
#     "Department":["IT","HR","Finance"],
#     "salary":[10000,20000,30000]
# }
# df=pd.DataFrame(data)
# print(df)
# Reading and writing data
#         read function           write function
# CSV --> pd.read_csv()           df.to_csv()
#
# EXcel -> pd.read_excel()        df.to_excel()
#
# JSON --> pd.read_json()         df.to_json()
#
# SQL  -> pd.read_sql()           df.to_sql()

# Data Exploration Methods
# df.head() --> show first 5 ROWS
# df.tail() --> show last 5 rows
# df.shape() -->retuns(rows,columns)
#df.info() --> summary of columns and datatypes
#df.describe() -->statisctical summery of numerical columns
#df.columns     --> list of column names
# df.dtypes --> data type of columns
# df=pd.read_csv("weather_data.csv")
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# # print(df.describe())
# print(df.columns)
# print(df.dtypes)
# print(df["city"])
# selecting the data
# print(df.loc[0]) #--> by label
# print(df.iloc[1])  #--> by position
# print(df[df["temparature"] > 30.0])

#data cleaning

# missing values--> df.isnull(), df.fillna() ,df.dropna()

# print(df.isnull())
# print(df.fillna('Future records'))
# print(df.dropna())
# df.to_csv('weather_data.csv', index=False)

#rename column ---df.rename(columns={old:new}
# print(df.rename(columns={'time':'timestamp'}))
#remove duplicates
# print(df.drop_duplicates())

#reset index
df=pd.DataFrame(
    {
        "Name":['amith','kiran','raju','vinay'],
        "Salary":[15000,2500,60000,65000],
        "Department":['HR','IT','fin','IT']
    }
)
# print(df)
# filter_data=df[df["Salary"]>20000].reset_index(drop=True)
# print(filter_data)
# filter_data=df.sort_values(by=['Salary'],ascending=False).reset_index(drop=True)
# print(filter_data)

# Data transformation
# add new column
df["bonus"]=df['Salary'] * 0.10
# df['Department']=df['HR','IT','fin','IT']
# print(df)
# Apply function
# df['Name']=df['Name'].apply(str.upper)
# print(df)
# replace values
df['Department'].replace("fin",'Finance',inplace=True)
# print(df)
# Grouping
# print(df.groupby('Department')['Salary'].mean())
# print(df.groupby('Department')['Salary'].sum())

# Merging and joining

# employee=pd.DataFrame({
#     "EmpID":[1,2,3],
#     "Name":['amit','murali','sneha']
# })
# department=pd.DataFrame({
#     "EmpID":[1,2,3],
#     "Department":['IT','HR','Finance']
# })
# merged=pd.merge(employee,department,on="EmpID")
# print(merged)