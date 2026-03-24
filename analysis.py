import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df)

print()

print("Adding a new column:")

df["total_price"]= df["Price"] * df["Quantity"]
print(df)

print()

print("Selcting only product and totalprice column")
print(df[["Product", "total_price"]])

print()

total_sales= df["total_price"].sum()

print(f'Total_sales : {total_sales}')

print()

print("\nCity Wise Total:\n",df.groupby("City")["total_price"].sum())

print()

result = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
top_products = result.head(3)
print("\n Top_products\n",top_products)


