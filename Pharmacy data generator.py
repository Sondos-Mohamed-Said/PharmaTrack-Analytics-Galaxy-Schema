import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

# 1. Setup and Configurations
fake = Faker('en_US')  # Using English names for compatibility
np.random.seed(42)
random.seed(42)

# Configuration for dataset size
NUM_TRANSACTIONS = 5000  # Number of sales records
NUM_CUSTOMERS = 200      # Number of unique customers

# ==========================================
# 2. Dim_Products (Expanded List)
# ==========================================
products_data = [
    # --- Pain Killers & Cold ---
    {'Name': 'Panadol Extra', 'Category': 'Medicine', 'SubCategory': 'Pain Killer', 'Brand': 'GSK', 'Price': 45},
    {'Name': 'Panadol Cold & Flu', 'Category': 'Medicine', 'SubCategory': 'Cold & Flu', 'Brand': 'GSK', 'Price': 55},
    {'Name': 'Cataflam 50mg', 'Category': 'Medicine', 'SubCategory': 'Pain Killer', 'Brand': 'Novartis', 'Price': 38},
    {'Name': 'Brufen 600mg', 'Category': 'Medicine', 'SubCategory': 'Pain Killer', 'Brand': 'Abbott', 'Price': 42},
    {'Name': 'Voltaren Gel', 'Category': 'Medicine', 'SubCategory': 'Topical Pain', 'Brand': 'GSK', 'Price': 65},
    {'Name': 'Congestal', 'Category': 'Medicine', 'SubCategory': 'Cold & Flu', 'Brand': 'Sigma', 'Price': 32},
    {'Name': '123 Tablets', 'Category': 'Medicine', 'SubCategory': 'Cold & Flu', 'Brand': 'Hikma', 'Price': 28},
    
    # --- Antibiotics ---
    {'Name': 'Augmentin 1g', 'Category': 'Medicine', 'SubCategory': 'Antibiotic', 'Brand': 'GSK', 'Price': 110},
    {'Name': 'Hibiotic 1g', 'Category': 'Medicine', 'SubCategory': 'Antibiotic', 'Brand': 'Amoun', 'Price': 95},
    {'Name': 'Curam 1g', 'Category': 'Medicine', 'SubCategory': 'Antibiotic', 'Brand': 'Sandoz', 'Price': 105},
    {'Name': 'Zithromax', 'Category': 'Medicine', 'SubCategory': 'Antibiotic', 'Brand': 'Pfizer', 'Price': 140},
    
    # --- Chronic Diseases ---
    {'Name': 'Concor 5mg', 'Category': 'Medicine', 'SubCategory': 'Hypertension', 'Brand': 'Merck', 'Price': 56},
    {'Name': 'Concor 10mg', 'Category': 'Medicine', 'SubCategory': 'Hypertension', 'Brand': 'Merck', 'Price': 72},
    {'Name': 'Plavix 75mg', 'Category': 'Medicine', 'SubCategory': 'Blood Thinner', 'Brand': 'Sanofi', 'Price': 220},
    {'Name': 'Crestor 10mg', 'Category': 'Medicine', 'SubCategory': 'Cholesterol', 'Brand': 'AstraZeneca', 'Price': 180},
    {'Name': 'Lantus Insulin', 'Category': 'Medicine', 'SubCategory': 'Diabetes', 'Brand': 'Sanofi', 'Price': 650},
    {'Name': 'Glucophage 1000', 'Category': 'Medicine', 'SubCategory': 'Diabetes', 'Brand': 'Merck', 'Price': 48},
    {'Name': 'Eltroxin 50', 'Category': 'Medicine', 'SubCategory': 'Thyroid', 'Brand': 'GSK', 'Price': 40},

    # --- Digestion ---
    {'Name': 'Antinal', 'Category': 'Medicine', 'SubCategory': 'Digestion', 'Brand': 'Amoun', 'Price': 25},
    {'Name': 'Nexium 40mg', 'Category': 'Medicine', 'SubCategory': 'Digestion', 'Brand': 'AstraZeneca', 'Price': 90},
    {'Name': 'Gaviscon Syrup', 'Category': 'Medicine', 'SubCategory': 'Digestion', 'Brand': 'Reckitt', 'Price': 85},

    # --- Cosmetics (Skin & Hair) ---
    {'Name': 'Vichy Normaderm Cleanser', 'Category': 'Cosmetics', 'SubCategory': 'Skin Care', 'Brand': 'Vichy', 'Price': 450},
    {'Name': 'Vichy Mineral 89', 'Category': 'Cosmetics', 'SubCategory': 'Skin Care', 'Brand': 'Vichy', 'Price': 620},
    {'Name': 'La Roche-Posay Effaclar', 'Category': 'Cosmetics', 'SubCategory': 'Skin Care', 'Brand': 'La Roche', 'Price': 480},
    {'Name': 'La Roche-Posay Anthelios', 'Category': 'Cosmetics', 'SubCategory': 'Sun Care', 'Brand': 'La Roche', 'Price': 550},
    {'Name': 'Cerave Foaming Cleanser', 'Category': 'Cosmetics', 'SubCategory': 'Skin Care', 'Brand': 'Cerave', 'Price': 390},
    {'Name': 'Nivea Soft Cream', 'Category': 'Cosmetics', 'SubCategory': 'Body Care', 'Brand': 'Nivea', 'Price': 95},
    {'Name': 'Dove Shampoo Repair', 'Category': 'Cosmetics', 'SubCategory': 'Hair Care', 'Brand': 'Unilever', 'Price': 110},
    {'Name': 'Loreal Hyaluron Expert', 'Category': 'Cosmetics', 'SubCategory': 'Skin Care', 'Brand': 'Loreal', 'Price': 220},
    {'Name': 'Garnier Micellar Water', 'Category': 'Cosmetics', 'SubCategory': 'Skin Care', 'Brand': 'Garnier', 'Price': 145},

    # --- Vitamins ---
    {'Name': 'Omega 3 Plus', 'Category': 'Medicine', 'SubCategory': 'Vitamins', 'Brand': 'Sedico', 'Price': 85},
    {'Name': 'Vitacid C', 'Category': 'Medicine', 'SubCategory': 'Vitamins', 'Brand': 'Cid', 'Price': 20},
    {'Name': 'Centrum Adult', 'Category': 'Medicine', 'SubCategory': 'Vitamins', 'Brand': 'Pfizer', 'Price': 450},
    {'Name': 'Pantogar', 'Category': 'Medicine', 'SubCategory': 'Hair Care', 'Brand': 'Merz', 'Price': 135},
    {'Name': 'Kerovit', 'Category': 'Medicine', 'SubCategory': 'Vitamins', 'Brand': 'Amoun', 'Price': 95},

    # --- Baby Care ---
    {'Name': 'Pampers Size 1', 'Category': 'Baby Care', 'SubCategory': 'Diapers', 'Brand': 'Pampers', 'Price': 280},
    {'Name': 'Pampers Size 3', 'Category': 'Baby Care', 'SubCategory': 'Diapers', 'Brand': 'Pampers', 'Price': 320},
    {'Name': 'Molfix Size 4', 'Category': 'Baby Care', 'SubCategory': 'Diapers', 'Brand': 'Molfix', 'Price': 300},
    {'Name': 'Sanalac 1', 'Category': 'Baby Care', 'SubCategory': 'Milk', 'Brand': 'Sanalac', 'Price': 160},
    {'Name': 'Hero Baby 2', 'Category': 'Baby Care', 'SubCategory': 'Milk', 'Brand': 'Hero', 'Price': 175},
    {'Name': 'Johnson Shampoo 500ml', 'Category': 'Baby Care', 'SubCategory': 'Bath', 'Brand': 'Johnson', 'Price': 95},
    {'Name': 'Sudocrem 125g', 'Category': 'Baby Care', 'SubCategory': 'Skin Care', 'Brand': 'Sudocrem', 'Price': 210},

    # --- Medical Supplies ---
    {'Name': 'Accu-Chek Strips 50', 'Category': 'Supplies', 'SubCategory': 'Diabetes Care', 'Brand': 'Roche', 'Price': 350},
    {'Name': 'Alcohol Spray 70%', 'Category': 'Supplies', 'SubCategory': 'First Aid', 'Brand': 'Local', 'Price': 25},
    {'Name': 'Face Masks Box', 'Category': 'Supplies', 'SubCategory': 'Protection', 'Brand': 'Local', 'Price': 50}
]

df_products = pd.DataFrame(products_data)
# Generate IDs starting from 101
df_products['Product_ID'] = range(101, 101 + len(df_products))
# Calculate Cost (Assuming cost is 70% to 85% of price)
df_products['Cost'] = (df_products['Price'] * np.random.uniform(0.70, 0.85, size=len(df_products))).astype(int)
df_products['Reorder_Level'] = np.random.randint(5, 20, size=len(df_products))

# ==========================================
# 3. Dim_Staff
# ==========================================
staff_data = [
    {'Staff_ID': 'S01', 'Name': 'Dr. Ahmed Mahmoud', 'Role': 'Manager', 'Shift': 'Morning'},
    {'Staff_ID': 'S02', 'Name': 'Dr. Sara Ali', 'Role': 'Pharmacist', 'Shift': 'Night'},
    {'Staff_ID': 'S03', 'Name': 'Mohamed Hassan', 'Role': 'Assistant', 'Shift': 'Morning'},
    {'Staff_ID': 'S04', 'Name': 'Noha Samir', 'Role': 'Pharmacist', 'Shift': 'Afternoon'},
    {'Staff_ID': 'S05', 'Name': 'Khaled Omar', 'Role': 'Cashier', 'Shift': 'Night'}
]
df_staff = pd.DataFrame(staff_data)

# ==========================================
# 4. Dim_Suppliers
# ==========================================
suppliers_data = [
    {'Supplier_ID': 'SUP_01', 'Name': 'Ibnsina Pharma'},
    {'Supplier_ID': 'SUP_02', 'Name': 'Pharma Overseas'},
    {'Supplier_ID': 'SUP_03', 'Name': 'United Company'},
    {'Supplier_ID': 'SUP_04', 'Name': 'Multipharma'}
]
df_suppliers = pd.DataFrame(suppliers_data)

# ==========================================
# 5. Dim_Customers
# ==========================================
customers_list = []
for i in range(NUM_CUSTOMERS):
    customers_list.append({
        'Customer_ID': f'CUST_{i+1:03}',
        'Name': fake.name(),
        'City': random.choice(['Nasr City', 'Maadi', 'Zamalek', 'Giza', 'Heliopolis', 'Dokki']),
        'Gender': random.choice(['M', 'F']),
        'Age': random.randint(18, 75)
    })
df_customers = pd.DataFrame(customers_list)

# ==========================================
# 6. Fact_Inventory (Stock & Expiry)
# ==========================================
inventory_list = []
today = datetime.today()

for _, row in df_products.iterrows():
    # Generate 1 to 3 batches per product
    for i in range(random.randint(1, 3)):
        # Create expiry dates: some past (expired), some future (valid)
        days_offset = random.randint(-100, 700) 
        expiry_date = today + timedelta(days=days_offset)
        
        inventory_list.append({
            'Product_ID': row['Product_ID'],
            'Batch_ID': f"B{row['Product_ID']}-{i+1}",
            'Quantity_On_Hand': random.randint(0, 50),
            'Manufacture_Date': (expiry_date - timedelta(days=730)).strftime('%Y-%m-%d'), # Approx 2 years before expiry
            'Expiry_Date': expiry_date.strftime('%Y-%m-%d'),
            'Storage_Location': random.choice(['Shelf A', 'Shelf B', 'Fridge', 'Drawer 1', 'Drawer 2'])
        })

df_inventory = pd.DataFrame(inventory_list)

# ==========================================
# 7. Fact_Sales (Transactions)
# ==========================================
sales_list = []
start_date = today - timedelta(days=365) # Sales from last year

for i in range(NUM_TRANSACTIONS):
    # Select random product and customer
    product = df_products.sample(1).iloc[0]
    customer = df_customers.sample(1).iloc[0]
    staff = df_staff.sample(1).iloc[0]
    
    qty = random.randint(1, 5)
    
    # Generate random date/time within the year
    sale_date = start_date + timedelta(days=random.randint(0, 365))
    sale_time = f"{random.randint(9, 23)}:{random.randint(0, 59):02}"
    
    sales_list.append({
        'Transaction_ID': f'TRX_{i+1:05}',
        'Date': sale_date.strftime('%Y-%m-%d'),
        'Time': sale_time,
        'Product_ID': product['Product_ID'],
        'Staff_ID': staff['Staff_ID'],
        'Customer_ID': customer['Customer_ID'],
        'Quantity_Sold': qty,
        'Unit_Price': product['Price'],
        'Total_Amount': qty * product['Price'],
        'Payment_Method': random.choices(['Cash', 'Visa', 'App'], weights=[70, 20, 10], k=1)[0]
    })

df_sales = pd.DataFrame(sales_list)

# ==========================================
# 8. Export to CSV
# ==========================================
df_products.to_csv('Dim_Products.csv', index=False)
df_staff.to_csv('Dim_Staff.csv', index=False)
df_suppliers.to_csv('Dim_Suppliers.csv', index=False)
df_customers.to_csv('Dim_Customers.csv', index=False)
df_inventory.to_csv('Fact_Inventory.csv', index=False)
df_sales.to_csv('Fact_Sales.csv', index=False)

print("Data generation complete. 6 CSV files created successfully.")
print(f"Total Transactions: {len(df_sales)}")
print(f"Total Products: {len(df_products)}")
print(f"Total Customers: {len(df_customers)}")