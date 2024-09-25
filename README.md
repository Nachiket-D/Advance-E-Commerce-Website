# E-commerce Website

An e-commerce website built using Flask, which allows users to register, log in, browse products, add items to the cart, and view similar products. The website also includes a contact page with a contact form for user inquiries.

## Features

- **User Registration and Login**: Users can create an account and log in to access their cart and manage their profile.
- **Browse Products**: Users can view the latest and best-selling products available in the store.
- **Product Search Functionality**: Users can search for products by name or details.
- **View Product Details**: Users can see detailed information about a specific product, including similar products.
- **Add Products to Cart**: Users can add selected products to their shopping cart with specified quantities.
- **Cart Management**: Users can view their cart, update item quantities, and see the total cost of their selected items.
- **Logout and Session Management**: Users can log out, and their session information is managed securely.
- **Contact Us Form**: A contact form that allows users to reach out for inquiries, integrated with Google Maps for location display.
- **View Similar Products**: Users can view products similar to the one they are currently viewing based on product type.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Session Management**: Flask Sessions
- **Database**: Mock functions to handle users and products (can be extended to use an actual database like PostgreSQL or SQLite)

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask

### Installation Steps

1. **Clone the Repository**

   ```
   git clone https://github.com/Nachiket-D/Advance-E-Commerce-Website.git
   cd Advance-E-Commerce-Website/ecommerce
   ```

2. **Create a Virtual Environment and Activate it**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**

   Ensure that Flask is installed in your virtual environment:

   ```
   pip install Flask
   ```

4. **Run the Development Server**

   ```
   python app.py
   ```

   The website will be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

5. **Access the Website**

   - **Home Page**: Browse the latest products at `/`.
   - **Login**: Access the user login page at `/login/`.
   - **Register**: Create a new user account at `/register/`.
   - **Products**: View all products at `/products/`.
   - **Product Details**: View individual product details and similar products at `/products/<product_id>/`.
   - **Cart**: Manage your cart at `/cart/`.
   - **Contact**: Reach out through the contact form at `/contact/`.

## Contribution

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and create a pull request.
