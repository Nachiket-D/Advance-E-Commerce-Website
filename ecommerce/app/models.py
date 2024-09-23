from django.db import models
import json
import os

from django.conf import settings

# Paths to JSON files
USERS_FILE = os.path.join(settings.BASE_DIR, 'app/json_data/users.json')
PRODUCTS_FILE = os.path.join(settings.BASE_DIR, 'app/json_data/products.json')

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
def add_to_cart(user_email, product_id):
    users = get_users()
    for user in users:
        if user["email"] == user_email:
            if product_id not in user["product_id"]:
                user["product_id"].append(product_id)
    save_json(USERS_FILE, users)

