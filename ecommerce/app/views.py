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
        for user in users:
            if user['email'] == email and user['password'] == password:
                request.session['user'] = {'email': user['email'], 'product_id': user['product_id']}
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
        user_data = {
            'id': len(get_users()) + 1,
            'name': name,
            'email': email,
            'password': password,
            'product_id': []
        }
        save_user(user_data)
        return redirect('login')
    return render(request, 'register.html')

# Products Page - Show all products
def products(request):
    products = get_products()
    return render(request, 'products.html', {'products': products})

# Product Details Page
def product_detail(request, product_id):
    products = get_products()
    product = next((p for p in products if p["id"] == product_id), None)
    return render(request, 'product_detail.html', {'product': product})

# Add to Cart
def add_to_cart_view(request, product_id):
    if request.session.get('user'):
        add_to_cart(request.session['user']['email'], product_id)
        return redirect('cart')
    return redirect('login')

# Cart Page
def cart(request):
    user_email = request.session.get('user', {}).get('email')
    if user_email:
        users = get_users()
        products = get_products()
        user = next((u for u in users if u['email'] == user_email), None)
        
        # Get user products based on product IDs
        user_products = [p for p in products if p['id'] in user['product_id']]
        
        # Calculate total price
        total = sum(float(p['cost'].replace('$', '').strip()) for p in user_products)

        return render(request, 'cart.html', {'products': user_products, 'total': total})
    
    return redirect('login')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')
