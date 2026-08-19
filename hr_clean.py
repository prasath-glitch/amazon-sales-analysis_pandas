
import pandas as pd

df=pd.read_csv(r"C:\Users\HARI PRASATH\OneDrive\Desktop\hr_analysis\hr_employee_analysis (1).csv")


# Part 1 — Understand the Dataset

# print(df.head(10))
# print(df.tail(10))
# print(len(df))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.describe)
# print(df.isnull.sum())

# Part 2 — Employee Overview

# print(df.head(6))
# print(df["Department"].value_counts())
# print(df["City"].value_counts())
# print(df["Gender"].value_counts())
# print(df.nunique())
# print(df["Department"].unique())

# Part 3 — Salary Analysis

# print(df["Salary"].max())
# print(df["Salary"].min())
# print(df["Salary"].mean())
# print(df["Salary"].median())
# print(df["Salary"].sum())
# print(df.loc[df["Salary"].idxmin()])

# lowest_salary = df["Salary"].min()

# print(df[df["Salary"] == lowest_salary])

# print(df["Salary"]> 70000 )
# print(df.loc[df["Salary"]< 40000])
# print(df.loc[df["Salary"] > 70000])
# print(df.loc[df["Salary"] . between(50000,70000)])


# Part 4 — Experience Analysis

# print(df["Experience"].mean())
# print(df["Experience"].max())
# print(df.loc[df["Experience"]>5])
# print(df.loc[df["Experience"]<3])
# print(df["Experience"] >= 5

# count = (df["Experience"] >= 5).sum()
# print(count)


# Part 5 — Department Analysis

# print(df.groupby("Department")["Salary"].mean())
# print(df.groupby("Department")["Salary"].min())
# print(df.groupby("Department")["Salary"].max())
# print(df.groupby("Department")["Salary"].sum())
# print(df.groupby("Department").count()
# print(df.groupby("Department") ["Salary"].mean())
# print(df.groupby("Department").idxmax())
# print(df.groupby("Department") ["Name"].value_counts())

# Part 6 — City Analysis

# print(df["City"].value_counts())
# print(df.groupby("City") ["Salary"].mean())
# print(df.groupby("City") ["Name"].count())

# Part 7 — Performance Analysis

# print(df["Rating"].mean())
# print(df[df["Rating"] > 4.5])
# print(df.groupby("Department")["Rating"].mean())
# print(df[df["Rating"] < 4.0])

# Part 8 — Bonus & Salary Calculation

# # print(df.head(5))
# df["HRA"] = df["Salary"] * 0.20
# df["PF"] = df["Salary"] * 0.12
# df["Annual sal"] = df["Salary"] * 12
# df["Gross_sal"] = df["Salary"] + df["HRA"] + df["Bonus"]
# print(df)


# Part 9 — Joining Date Analysis

# print(df.head(5))
# print(df["Joining_Date"])
# df["Joining_Date"] = pd.to_datetime( df["Joining_Date"], format="%d-%m-%Y")
# print(df["Joining_Date"].dtype)
# print(df)

# Part 10 — Sorting

# print(df.sort_values(by="Salary",ascending=False))
# print(df.sort_values(by="Experience",ascending=False))
# print(df.sort_values(by="Experience",ascending=True))
# print(df.sort_values(by="Rating",ascending=True))
# print(df.sort_values(by="Salary",ascending=False).head(10))

# # Part 11 — Pivot Table
# print(pd.pivot_table(df, index="Department", values="Salary", aggfunc="sum"))
# print(pd.pivot_table(df, index="Department", values="Salary", aggfunc="max"))
# print(pd.pivot_table(df, index="Department", values="Salary", aggfunc="mean"))
# print(pd.pivot_table(df, index="Department", values="Emp_ID", aggfunc="count"))
# # print(df.groupby("Department") ["Salary"].mean())

