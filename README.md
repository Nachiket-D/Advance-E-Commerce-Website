Ecommerce Website

An ecommerce website built using Django, which allows users to register, log in, browse products, add items to the cart, and view similar products. The website also includes a contact page and features like unique user registration and cart management.
Features

    User Registration and Login
    Browse Products
    Product Search Functionality
    View Product Details
    Add Products to Cart
    Cart Management (View products, update quantities, see total cost)
    Logout and Session Management
    Contact Us Form with integrated Google Maps
    View similar products based on product type

Technologies Used

    Backend: Django (Python)
    Frontend: HTML, CSS, JavaScript
    Session Management: Django Sessions
    Database: Mock functions to handle users and products (can be extended to use an actual database like PostgreSQL or SQLite)

Setup Instructions
Prerequisites

    Python 3.x
    Django

1. Clone the Repository

bash

git clone https://github.com/yourusername/ecommerce-website.git
cd ecommerce-website

2. Create a Virtual Environment and Activate it

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

bash

pip install -r requirements.txt

4. Run the Development Server

bash

python manage.py runserver

The website will be running at http://127.0.0.1:8000/.
5. Access the Website

    Home Page: Browse latest products
    Login: /login/ - User login page
    Register: /register/ - User registration page
    Products: /products/ - View all products
    Product Details: /products/<product_id>/ - View individual product details and similar products
    Cart: /cart/ - View and manage cart
    Contact: /contact/ - Contact form with integrated Google Maps
