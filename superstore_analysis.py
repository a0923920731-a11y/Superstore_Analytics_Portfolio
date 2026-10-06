import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
# Category profitability analysis

category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

category_summary["Profit Margin"] = (
    category_summary["Profit"] / category_summary["Sales"] * 100
)

print(category_summary)



# Chart 1: Profit Margin by Category

category_summary["Profit Margin"].plot(kind="bar")

plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)

plt.show()


# Tables discount analysis

tables = df[df["Sub-Category"] == "Tables"]

tables_discount = (
    tables.groupby("Discount")["Profit"]
    .mean()
    .sort_index()
)

print(tables_discount)

# Chart 2: Average Profit by Discount Level

tables_discount.plot(kind="bar")

plt.title("Average Profit by Discount Level - Tables")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.axhline(0, linewidth=1)

plt.show()

# Customer transaction-level analysis

cindy = df[df["Customer Name"] == "Cindy Stewart"].copy()

cindy = cindy[["Product Name", "Profit"]].sort_values("Profit")

print(cindy)

# Chart 3: Profit by Transaction

cindy.plot(
    kind="barh",
    x="Product Name",
    y="Profit",
    legend=False
)

plt.title("Cindy Stewart: Profit by Transaction")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.axvline(0, linewidth=1)

plt.show()