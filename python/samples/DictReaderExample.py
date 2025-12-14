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

products = []


with open(feedPath, "r") as f:
    csv_reader  = csv.DictReader(f, delimiter=',')
    firstRow = next(csv_reader)
    header = list(firstRow.keys())
    print("List of column names:", header)
    
    for row in csv_reader:
        print(row['item_group_id'])


    
"""
with open(feedPath, "r", newline="") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        product = Product(
            id=int(row["id"]),
            name=row["name"],
            price=float(row["price"]),
            in_stock=to_bool(row["in_stock"])
        )
        products.append(product)
        
for p in products:
    if p.in_stock and p.price < 100:
        print(f"{p.name} is cheap and available 🎉")
        
"""