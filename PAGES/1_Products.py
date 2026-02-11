import streamlit as st
from database import load_products
from utils import init_cart, add_to_cart

st.title("🛍 Products")
init_cart()

products = load_products()

for index, row in products.iterrows():
    st.subheader(row["name"])
    st.write(f"Category: {row['category']}")
    st.write(f"Price: ₹{row['price']}")

    if st.button(f"Add to Cart {row['id']}"):
        add_to_cart(row.to_dict())
        st.success("Added to Cart")
