
import pandas as pd

df=pd.read_csv(r"C:\Users\HARI PRASATH\Downloads\amazon_sales.csv")


# print(df)
# df.head()
# print(df.notnull().sum())
# print(df.shape)
# print(df.columns)


# # filering

# print(df[df["Category"] == "Electronics"])
# print(df[df["Price"]>30000])
# print(df[df["City"]=="Chennai"])
# print(df[df["Payment"]=="Card"])
# print([df[df["Category"]=="Electronics"] & (df["City"]=="Chennai")])
# print([df(df["Category"] == "Electronics") & (df["City"] == "Chennai")])

# #  sorting

# print(df.sort_values(by="Price",ascending=False))
# print(df.sort_values("Price"))
# print(df.head(10))
# df["multi_total"] = df["Quantity"]*df["Price"]
# df["Gst"] =df["multi_total"] * 0.18
# print(df)

# # analaysics

# print(df["Price"].mean())
# print(df["Price"].min())
# print(df["Price"].max())
# print(df["Price"].sum())
# print(df["Quantity"].sum())
# print(df["Customer"].nunique())
# print(df["Payment"].mode())
# print(df.head(5))

# group by

# print(df.groupby("Category") ["multi_total"].sum())
# print(df.groupby("City") ["multi_total"].sum())
# print(df.groupby("Payment").size())
# print(df.groupby("Product") ["Price"].mean())
# print(df.groupby("Category")["Price"].mean())
# print(df.groupby("City") ["Price"].sum())
# print(df.groupby("City")["Price"].sum().sort_values(ascending=False).head(3))
# print(df)

# pivot table 
# df.head(7)
# print(df["Category","Product"] ,)
# df = df.groupby("City").agg( revenue_bro=("multi_total", "sum"), Average_Price=("   Price", "mean"))
# df = pd.pivot_table(df, index=["City", "Category"], values=["Price", "Quantity"], aggfunc=["sum", "mean","median"])

# print(df)

