import csv
import json

USD_TO_INR = 83  # fixed conversion rate

clean_data = []
seen_products = set()  # to remove duplicates

# Step 1: Read CSV file
with open('sales.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        # row format: [id, product_name, price, country]
        
        product_id = row[0].strip()
        product_name = row[1].replace('"', '').strip()
        price_raw = row[2].replace('$', '').replace('"', '').strip()
        country = row[3].strip()

        # Step 2: Convert price to float
        try:
            price_usd = float(price_raw)
        except ValueError:
            continue  # skip invalid rows

        # Step 3: Remove duplicates (same Product & Price)
        unique_key = (product_name, price_usd)
        if unique_key in seen_products:
            continue
        seen_products.add(unique_key)

        # Step 4: Convert USD to INR
        price_inr = price_usd * USD_TO_INR

        # Step 5: Prepare clean data
        clean_data.append({
            "product_id": product_id,
            "product_name": product_name,
            "price_usd": price_usd,
            "price_inr": price_inr,
            "country": country
        })

# Step 6: Save output to JSON file
with open('clean_sales.json', 'w') as json_file:
    json.dump(clean_data, json_file, indent=4)

print("Data cleaned successfully and saved to clean_sales.json")
