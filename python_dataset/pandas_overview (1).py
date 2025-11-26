import pandas as pd

# Step 1: Load CSV
df = pd.read_csv("Retail_Sales.csv")
# print(df.shape)
# print(df.columns)
# print(df["OrderID"])
# print(df[["OrderID", "Date"]])
# print(df.iloc[1])
print(df[df["OrderID"] > 1005])



# Step 2: Show first few records
# print(df.head())
#
# # Step 3: Get basic info
# print(df.info())
#
# # Step 4: Statistical summary
# print(df.describe())
#
# # Step 5: Check missing values
# print(df.isnull().sum())
