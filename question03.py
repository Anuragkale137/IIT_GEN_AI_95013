import pandas as pd

data = pd.read_csv('C:\\Users\\Anurag\\Downloads\\products.csv')
print(data)

print("The total rows of the table is :",len(data))

products = data[data["price"]>500].shape[0]
print("products with price greater than 500 are :",products)

avarage_price = data["price"].mean()
print("Avarage price :",avarage_price)

user_category = input("Enter the category you want to filter products:")
filterd_products = data[data["category"].str.lower()==user_category.lower()]
print("products in the category",user_category,"are :")
print(filterd_products)

total_quantity = data["quantity"].sum()
print("Total quantity of all stock products is :",total_quantity)