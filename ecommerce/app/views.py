from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import get_users, get_products, save_user, add_to_cart

# Home Page - Show Latest and Best Products
def home(request):
    products = get_products()[:4]
    return render(request, 'home.html', {'products': products})

# Login Page
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = get_users()
        
        # Check if the user exists
        for user in users:
            if user['email'] == email and user['password'] == password:
                request.session['user'] = {'email': user['email']}
                request.session['cart'] = user.get('cart', [])
                return redirect('home')
        
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

# Logout
def logout_view(request):
    request.session.flush()
    return redirect('login')

# Register Page
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email already exists
        users = get_users()
        if any(user['email'] == email for user in users):
            return render(request, 'register.html', {'error': 'Email already exists'})

        # Generate a unique user ID
        if users:
            new_user_id = max(user['id'] for user in users) + 1  # Get the highest user ID and increment it
        else:
            new_user_id = 1  # If no users exist, start with ID 1
        
        # Prepare new user data, starting with an empty cart
        user_data = {
            'id': new_user_id,
            'name': name,
            'email': email,
            'password': password,
            'cart': []  # Empty cart upon registration
        }
        
        # Save the new user
        save_user(user_data)
        return redirect('login')
    
    return render(request, 'register.html')

# Products Page - Show all products and handle search
def products(request):
    products = get_products()
    
    # Handle search query (search by product name or details)
    query = request.GET.get('search', '')
    if query:
        products = [p for p in products if query.lower() in p['name'].lower() or query.lower() in p['details'].lower()]

    return render(request, 'products.html', {'products': products, 'search': query})

# Product Details Page
def product_detail(request, product_id):
    products = get_products()
    product = next((p for p in products if p["id"] == product_id), None)

    similar_products = [p for p in products if p['id'] != product_id and product['type'] == p['type']]
                
    return render(request, 'product_detail.html', {'product': product, 'similar_products': similar_products})

# Add to Cart - Add products to the cart with quantity
def add_to_cart_view(request, product_id):
    if request.session.get('user'):
        # Get quantity from POST request
        quantity = int(request.POST.get('quantity', 1))
        
        # Add product to the user's cart with the specified quantity
        add_to_cart(request.session['user']['email'], product_id, quantity)
        
        # Update session cart after adding the item
        users = get_users()
        user = next((u for u in users if u['email'] == request.session['user']['email']), None)
        request.session['cart'] = user['cart']
        
        return redirect('cart')
    
    return redirect('login')

# Cart Page - Show user's cart with quantities and total
def cart(request):
    user_email = request.session.get('user', {}).get('email')
    
    if user_email:
        users = get_users()
        products = get_products()
        user = next((u for u in users if u['email'] == user_email), None)

        # Fetch products in the user's cart with quantities
        user_products = []
        total_cost = 0
        
        for item in user['cart']:
            product = next((p for p in products if p['id'] == item['product_id']), None)
            if product:
                product['quantity'] = item['quantity']
                product_cost = float(product['cost'].replace('$', '').strip()) * product['quantity']
                total_cost += product_cost
                product['total_cost'] = f"${product_cost:.2f}"
                user_products.append(product)

        return render(request, 'cart.html', {'products': user_products, 'total_cost': f"${total_cost:.2f}", 'total': f"${total_cost+40.00}"})
    
    return redirect('login')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')
