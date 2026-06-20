import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

products = [
    ("Laptop",1200,850),
    ("Monitor",300,180),
    ("Keyboard",75,20),
    ("Mouse",40,10),
    ("Headphones",150,60),
    ("Tablet",600,350),
    ("Printer",250,120),
    ("Webcam",80,25)
]

regions = ["West","South","Midwest","Northeast"]

rows = []

start_date = datetime(2023,1,1)

for order_id in range(1,10001):

    product, price, cost = random.choice(products)

    quantity = random.randint(1,5)

    revenue = price * quantity
    total_cost = cost * quantity
    profit = revenue - total_cost

    rows.append({
        "OrderID": order_id,
        "OrderDate": start_date + timedelta(days=random.randint(0,730)),
        "Customer": fake.name(),
        "Region": random.choice(regions),
        "Product": product,
        "Quantity": quantity,
        "Revenue": revenue,
        "Cost": total_cost,
        "Profit": profit
    })

df = pd.DataFrame(rows)

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv created successfully")