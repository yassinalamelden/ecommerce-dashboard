import sqlite3, pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "data" / "ecommerce.db"

st.set_page_config(page_title="E-commerce Dashboard", layout="wide")
st.title("📊 E-commerce Dashboard")

if not DB_PATH.exists():
    st.error(f"Database file not found: {DB_PATH}")
    st.stop()

if DB_PATH.stat().st_size == 0:
    st.error(f"Database file is empty: {DB_PATH}")
    st.stop()

st.sidebar.write("Database path:")
st.sidebar.code(str(DB_PATH.resolve()))

with sqlite3.connect(DB_PATH) as con:
    tables = pd.read_sql(
        "SELECT name FROM sqlite_master WHERE type='table';", con
    )
st.sidebar.subheader("Tables in this database")
st.sidebar.dataframe(tables)

@st.cache_data
def load_df(query: str, db_path: str):
    with sqlite3.connect(db_path) as con:
        return pd.read_sql(query, con)

# --- Query 1: Total sales per product
q_products = """
SELECT p.product_name,
       SUM(oi.quantity * oi.price) AS total_sales,
       SUM(oi.quantity) AS units_sold
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC;
"""

# --- Query 2: Top customers
q_customers = """
SELECT c.customer_name,
       SUM(oi.quantity * oi.price) AS total_spent,
       COUNT(DISTINCT o.order_id) AS orders_count
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
"""

# --- Query 3: Sales over time
q_sales_time = """
SELECT DATE(o.order_date) AS day,
       SUM(oi.quantity * oi.price) AS total_sales
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
GROUP BY DATE(o.order_date)
ORDER BY day;
"""

# --- Tabs layout
tabs = st.tabs(["Products", "Customers", "Sales Over Time"])

with tabs[0]:
    st.header("🛒 Sales by Product")
    try:
        df = load_df(q_products, str(DB_PATH))
        st.dataframe(df)
        st.plotly_chart(px.bar(df, x="product_name", y="total_sales",
                               title="Total Sales by Product"))
    except Exception as e:
        st.error(f"Query failed: {e}")

with tabs[1]:
    st.header("👥 Top Customers")
    try:
        df = load_df(q_customers, str(DB_PATH))
        st.dataframe(df)
        st.plotly_chart(px.bar(df.head(20), x="customer_name", y="total_spent",
                               title="Top 20 Customers"))
    except Exception as e:
        st.error(f"Query failed: {e}")

with tabs[2]:
    st.header("📈 Sales Over Time")
    try:
        df = load_df(q_sales_time, str(DB_PATH))
        st.dataframe(df)
        st.plotly_chart(px.line(df, x="day", y="total_sales",
                                title="Sales Trend Over Time"))
    except Exception as e:
        st.error(f"Query failed: {e}")




