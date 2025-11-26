import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Retail_Sales.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull())
#fill missing amount --> quantity*UnitPrice*(1-discount)
df['Amount']=df.apply(
  lambda row: row['Quantity'] * row['UnitPrice'] * (1 - row['Discount'] )
    if pd.isnull(row['Amount'])
    else row['Amount'],axis=1
)
# find the sale in each region
region_sale=df.groupby('Region')['Amount'].sum().reset_index()
region_sale.plot(x='Region',y='Amount',kind='bar',title='sales  by Region',legend=False)
plt.show()
# print(region_sale)

# Top 3 highest value orders
top_orders=df.sort_values(by=['Amount'],ascending=False).head(3).reset_index(drop=True)
# print(top_orders)

# Analysis
# revenue by payment method
payment_summery=df.groupby('PaymentMode')['Amount'].sum().reset_index()
# print(payment_summery)

#total quantity sold per product

product_summery=df.groupby('Product')['Quantity'].sum().reset_index()
# print(product_summery)

# df.to_csv("Resulted_data.csv",index=False)
