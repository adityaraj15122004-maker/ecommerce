import pandas as pd

PRODUCT_FILE = "data/products.csv"
USER_FILE = "data/users.csv"
ORDER_FILE = "data/orders.csv"

def load_products():
    return pd.read_csv(PRODUCT_FILE)

def load_users():
    return pd.read_csv(USER_FILE)

def save_user(user):
    df = load_users()
    df = pd.concat([df, pd.DataFrame([user])], ignore_index=True)
    df.to_csv(USER_FILE, index=False)

def save_order(order):
    df = pd.read_csv(ORDER_FILE)
    df = pd.concat([df, pd.DataFrame([order])], ignore_index=True)
    df.to_csv(ORDER_FILE, index=False)

def add_product(product):
    df = load_products()
    df = pd.concat([df, pd.DataFrame([product])], ignore_index=True)
    df.to_csv(PRODUCT_FILE, index=False)
