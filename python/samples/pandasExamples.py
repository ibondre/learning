import csv
import pandas as pd
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    in_stock: bool

def to_bool(value: str) -> bool:
    return value.strip().lower() in ("true", "1", "yes")


feedPath = "C:\\Users\\irfanb\\Downloads\\feed-all-2.csv"

df = pd.read_csv(feedPath,
                 dtype={                     
                     "gtin": str  ,
                     "google_product_category": str,
                     "size": str,
                     "custom_label_2": int,
                     "pattern": str, 
                     "upc": str
                     #"sale_price": float,
                     #"price": float        
                 }
                )

#header = list(df.columns)

#print("List of column names:", header)

#print(df.dtypes)

#print(df.head())

#print(df.describe())
#df.info()

#print(df["gtin"].head())
#print(df.gtin.head())

#print(df.count())
newdf = df[["id", "title", "price", "sale_price", "gtin"]].where(pd.notnull(df.gender))

out_of_stock = df[
    (df["availability"] != "IN_STOCK") & (pd.notnull(df.custom_label_2))
]

df_sorted = df.sort_values(by="id", ascending=True).head(10)

df_grouped = df.groupby("seller_name")["custom_label_2"].mean()


df_grouped.to_csv("C:\\Users\\irfanb\\Downloads\\feed-sample_1.csv", index=False)


'''
for _, row in df.iterrows():
    print(row["name"], row["price"])

'''