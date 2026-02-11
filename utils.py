import streamlit as st

def init_cart():
    if "cart" not in st.session_state:
        st.session_state.cart = []

def add_to_cart(product):
    st.session_state.cart.append(product)

def calculate_total():
    total = 0
    for item in st.session_state.cart:
        total += item["price"]
    return total
