import streamlit as st

# Dictionary of products and their prices
products = {
    'Product 1': 10.00,
    'Product 2': 20.00,
    'Product 3': 30.00,
    'Product 4': 40.00,
}

def display_products(products):
    '''
    Function to display the products with a selectbox for quantity
    '''
    st.header('Products')
    for product, price in products.items():
        max_qty = 10
        qty = st.selectbox(f'Select Quantity for {product} (Price: ${price})', list(range(max_qty+1)))
        st.write('You selected: ', qty)

def display_cart():
    '''
    Function to display the shopping cart
    '''
    st.header('Shopping Cart')

    # Display dummy content (an empty cart) for now
    st.write('Your cart is empty.')

# Page Layout
st.title('E-Commerce Website')

display_products(products)
display_cart()
