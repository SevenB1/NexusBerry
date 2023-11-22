import pandas as pd 
import os
ecom = pd.read_csv("Ecommerce Purchases.csv")
pd.set_option("Display.max_columns", 14)
print(ecom.head())
print(ecom["Job"])

ecom(ecom["Purchase_Price"] > 50) & (ecom["CC_Provider"] == "American Express")[["Email","CC_Provider","Purchase_Price"]]

