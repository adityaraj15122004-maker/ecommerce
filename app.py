import streamlit as st
from database import load_users, save_user

st.title("🛒 Streamlit E-Commerce")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        user = users[(users.email == email) & (users.password == password)]

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.user = user.iloc[0].to_dict()
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

elif choice == "Register":
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        save_user({
            "id": 0,
            "name": name,
            "email": email,
            "password": password,
            "role": "user"
        })
        st.success("Registration Successful")
