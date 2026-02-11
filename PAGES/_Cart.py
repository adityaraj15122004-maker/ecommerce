import streamlit as st
from utils import calculate_total, init_cart

st.title("🛒 Your Cart")
init_cart()

if len(st.session_state.cart) == 0:
    st.write("Cart is empty")
else:
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ₹{item['price']}")

    st.write("### Total:", calculate_total())
