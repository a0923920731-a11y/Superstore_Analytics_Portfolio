import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("superstore.csv", encoding="latin1")

# Create SQLite database
conn = sqlite3.connect("superstore.db")

# Load data into SQL table
df.to_sql("superstore", conn, if_exists="replace", index=False)

# SQL Query 1: Sales and Profit by Category

query1 = """
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

result1 = pd.read_sql_query(query1, conn)

print("\nQuery 1: Sales and Profit by Category")
print(result1)

# SQL Query 2: Profit by Sub-Category

query2 = """
SELECT
    "Sub-Category",
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY "Sub-Category"
ORDER BY Total_Profit ASC;
"""

result2 = pd.read_sql_query(query2, conn)

print("\nQuery 2: Profit by Sub-Category")
print(result2)

# SQL Query 3: Average Profit by Discount for Tables

query3 = """
SELECT
    Discount,
    AVG(Profit) AS Average_Profit
FROM superstore
WHERE "Sub-Category" = 'Tables'
GROUP BY Discount
ORDER BY Discount ASC;
"""

result3 = pd.read_sql_query(query3, conn)

print("\nQuery 3: Average Profit by Discount for Tables")
print(result3)

# SQL Query 4: Top Loss-Making Transactions

query4 = """
SELECT
    "Customer Name",
    "Product Name",
    Discount,
    Sales,
    Profit
FROM superstore
WHERE Profit < 0
ORDER BY Profit ASC
LIMIT 10;
"""

result4 = pd.read_sql_query(query4, conn)

print("\nQuery 4: Top Loss-Making Transactions")
print(result4)

# Python + SQL Integration

query1_result = pd.read_sql_query(query1, conn)

print("\nPython + SQL Integration")
print(query1_result)
query1_result.to_csv("sql_category_result.csv", index=False)
# Visualize SQL result with Python

query1_result.plot(
    kind="bar",
    x="Category",
    y="Total_Profit",
    legend=False
)

plt.title("Profit by Category - SQL Result")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.show()