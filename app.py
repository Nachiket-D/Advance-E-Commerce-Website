from flask import Flask, render_template, request, redirect, session, url_for
from models import get_users, get_products, save_user, add_to_cart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Home Page - Show Latest and Best Products
@app.route('/')
def home():
    products = get_products()[:4]
    return render_template('home.html', products=products)

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        users = get_users()
        
        # Check if the user exists
        for user in users:
            if user['email'] == email and user['password'] == password:
                session['user'] = {'email': user['email']}
                session['cart'] = user.get('cart', [])
                return redirect(url_for('home'))
        
        return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('login'))

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        users = get_users()
        if any(user['email'] == email for user in users):
            return render_template('register.html', error='Email already exists')

        # Generate a unique user ID
        new_user_id = max(user['id'] for user in users) + 1 if users else 1
        
        user_data = {
            'id': new_user_id,
            'name': name,
            'email': email,
            'password': password,
            'cart': []
        }
        save_user(user_data)
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Products Page - Show all products and handle search
@app.route('/products')
def products():
    products = get_products()
    query = request.args.get('search', '')
    if query:
        products = [p for p in products if query.lower() in p['name'].lower() or query.lower() in p['type'].lower()]

    return render_template('products.html', products=products, search=query)

# Product Details Page
@app.route('/products/<int:product_id>')
def product_detail(product_id):
    products = get_products()
    product = next((p for p in products if p["id"] == product_id), None)
    similar_products = [p for p in products if p['id'] != product_id and product['type'] == p['type']]

    return render_template('product_detail.html', product=product, similar_products=similar_products)

# Add to Cart - Add products to the cart with quantity
@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart_view(product_id):
    if 'user' in session:
        quantity = int(request.form.get('quantity', 1))
        add_to_cart(session['user']['email'], product_id, quantity)
        
        # Update session cart
        users = get_users()
        user = next((u for u in users if u['email'] == session['user']['email']), None)
        session['cart'] = user['cart']
        
        return redirect(url_for('cart'))
    
    return redirect(url_for('login'))

# Cart Page - Show user's cart with quantities and total
@app.route('/cart')
def cart():
    user_email = session.get('user', {}).get('email')
    
    if user_email:
        users = get_users()
        products = get_products()
        user = next((u for u in users if u['email'] == user_email), None)

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

        return render_template('cart.html', products=user_products, total_cost=f"${total_cost:.2f}", total=f"${total_cost+40.00}")
    
    return redirect(url_for('login'))

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f'Name: {name}, Email: {email}, Message: {message}')

        return redirect(url_for('home'))  
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
