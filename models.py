import json
import os

# Paths to JSON files (update these paths based on your directory structure)
USERS_FILE = os.path.join(os.path.dirname(__file__), 'json_data/users.json')
PRODUCTS_FILE = os.path.join(os.path.dirname(__file__), 'json_data/products.json')

# Load JSON Data
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Get Users
def get_users():
    return load_json(USERS_FILE)

# Get Products
def get_products():
    return load_json(PRODUCTS_FILE)

# Save User
def save_user(user_data):
    users = get_users()
    users.append(user_data)
    save_json(USERS_FILE, users)

# Add product to cart (in user.json)
def add_to_cart(user_email, product_id, quantity):
    users = get_users()
    for user in users:
        if user['email'] == user_email:
            product_in_cart = next((item for item in user['cart'] if item['product_id'] == product_id), None)
            if product_in_cart:
                product_in_cart['quantity'] += quantity
            else:
                user['cart'].append({'product_id': product_id, 'quantity': quantity})
            save_user(user)
            break
