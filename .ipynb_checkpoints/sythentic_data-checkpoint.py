import pandas as pd
import numpy as np
from faker import Faker
from datetime import date
import random

# ---------------------------
# Setup
# ---------------------------
fake = Faker()
np.random.seed(42)
random.seed(42)

# 6 months daily
dates = pd.date_range('2025-01-01', '2025-06-30', freq='D')

# ---------------------------
# Define products
# ---------------------------
products = [
    {'id': f'P{i:03}', 'name': name, 'category': cat,
     'sub_category': sub, 'base_price': price}
    for i, (name, cat, sub, price) in enumerate([
        ("Men's T-shirt", "Men", "Shirt", 20),
        ("Women's Dress", "Women", "Dress", 35),
        ("Kids Jacket", "Kids", "Jacket", 40),
        ("Men's Jeans", "Men", "Pants", 30),
        ("Women's Skirt", "Women", "Skirt", 25),
        ("Kids T-shirt", "Kids", "Shirt", 15),
        ("Men's Hoodie", "Men", "Jacket", 45),
        ("Women's Hoodie", "Women", "Jacket", 45),
        ("Unisex Socks", "All", "Accessories", 5),
        ("Cap", "All", "Accessories", 10)
    ], start=1)
]

# ---------------------------
# Initialize stock levels
# ---------------------------
product_stock = {p['id']: 50 for p in products}  # starting 50 units each

# ---------------------------
# Generate sales data
# ---------------------------
sales_records = []
for current_date in dates:
    weekday = current_date.weekday()
    is_weekend = weekday >= 5
    month = current_date.month

    for product in products:
        # Probability of sale higher on weekend
        sale_prob = 0.7 if is_weekend else 0.5

        # Seasonality
        if 'Jacket' in product['sub_category'] and month in [1, 2]:
            sale_prob += 0.2
        if 'T-shirt' in product['sub_category'] and month in [5, 6]:
            sale_prob += 0.2

        if random.random() < sale_prob and product_stock[product['id']] > 0:
            quantity = np.random.randint(
                1, min(6, product_stock[product['id']]+1))
            discount = np.random.choice([0, 0, 0, 5, 10])  # mostly no discount
            total_sale = quantity * (product['base_price'] - discount)
            store = random.choices(
                ['physical', 'online'], weights=[0.6, 0.4])[0]
            customer_id = f'C{np.random.randint(1, 101):03}'
            promotion = discount > 0

            sales_records.append({
                'date': current_date,
                'store': store,
                'product_id': product['id'],
                'product_name': product['name'],
                'category': product['category'],
                'sub_category': product['sub_category'],
                'quantity_sold': quantity,
                'price_per_unit': product['base_price'],
                'discount': discount,
                'total_sale': total_sale,
                'customer_id': customer_id,
                'promotion': promotion
            })

            # Update stock
            product_stock[product['id']] -= quantity

sales_df = pd.DataFrame(sales_records)

# ---------------------------
# Generate inventory snapshot
# ---------------------------
inventory_records = []
for current_date in dates:
    for product in products:
        # small daily fluctuation
        stock_level = max(
            0, product_stock[product['id']] + np.random.randint(-2, 3))
        reorder_point = 10
        supplier = fake.company()
        inventory_records.append({
            'date': current_date,
            'product_id': product['id'],
            'stock_level': stock_level,
            'reorder_point': reorder_point,
            'supplier': supplier
        })

inventory_df = pd.DataFrame(inventory_records)

# ---------------------------
# Generate expenses
# ---------------------------
expenses_records = []
for current_date in dates:
    weekday = current_date.weekday()
    # Salaries on Monday
    if weekday == 0:
        expenses_records.append({
            'date': current_date,
            'category': 'Salaries',
            'amount': 500,
            'notes': 'Weekly salaries'
        })
    # Utilities daily
    expenses_records.append({
        'date': current_date,
        'category': 'Utilities',
        'amount': np.random.randint(20, 50),
        'notes': 'Electricity'
    })
    # Supplies correlated with sales
    day_sales = sales_df[sales_df['date'] == current_date]['total_sale'].sum()
    supplies_amount = int(day_sales * 0.3)  # ~30% of sales
    expenses_records.append({
        'date': current_date,
        'category': 'Supplies',
        'amount': supplies_amount,
        'notes': 'Restocking'
    })

expenses_df = pd.DataFrame(expenses_records)

# ---------------------------
# Generate customer data
# ---------------------------
customers_records = []
for i in range(1, 101):
    gender = random.choice(['M', 'F'])
    age = np.random.randint(18, 60)
    first_purchase_date = fake.date_between(
        start_date='-2y', end_date=date(2025, 1, 1))
    total_purchases = sales_df[sales_df['customer_id']
                               == f'C{i:03}']['quantity_sold'].sum()
    customers_records.append({
        'customer_id': f'C{i:03}',
        'name': fake.name(),
        'age': age,
        'gender': gender,
        'first_purchase_date': first_purchase_date,
        'total_purchases': total_purchases
    })

customers_df = pd.DataFrame(customers_records)

# ---------------------------
# Save CSVs
# ---------------------------
sales_df.to_csv('clothing_sales.csv', index=False)
inventory_df.to_csv('clothing_inventory.csv', index=False)
expenses_df.to_csv('clothing_expenses.csv', index=False)
customers_df.to_csv('clothing_customers.csv', index=False)

print("Realistic synthetic dataset generated!")
