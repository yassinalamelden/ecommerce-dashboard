# 🛍️ E-Commerce Dashboard

An interactive **sales analytics dashboard** built with **Streamlit**, **SQLite**, and **Plotly** — visualize product performance, customer spending, and overall revenue trends in real time.

---

## 📊 Demo Preview

> This dashboard provides real-time sales insights using an SQLite database (`ecommerce.db`) and visualizes the results through Streamlit and Plotly.



> Example: Sales by Product section displaying total sales and units sold per product.

---

## 🧠 Features

- 📦 **Product-level analytics** — sales totals and quantities per product  
- 👥 **Customer insights** — spending and order frequency  
- 📅 **Sales trends** — daily revenue visualization  
- 💾 **SQLite backend** — lightweight, file-based database  
- 🧩 **Streamlit UI** — interactive web dashboard for instant visualization  

---

## 🗂️ Project Structure
```bash
ecommerce-dashboard/
│
├── app.py → Streamlit dashboard script
├── ecommerce.db → SQLite database (with sample data)
├── requirements.txt → Dependencies list
└── README.md → Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/ecommerce-dashboard.git
cd ecommerce-dashboard
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app
```bash
streamlit run app.py
```
Then open the local URL (usually http://localhost:8501) in your browser.

---

## 🧩 Database Info

The database file **`ecommerce.db`** includes:

- `categories`
- `products`
- `customers`
- `orders`
- `order_items`
- `payments`

### 🔍 Analytical Views

- `v_sales_by_product`
- `v_sales_by_customer`
- `v_sales_daily`

You can recreate the database anytime using:

```bash
sqlite3 ecommerce.db
```

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **Database** | SQLite |
| **Data Analysis** | Pandas |
| **Visualization** | Plotly |
| **Language** | Python 3.x |

---

## 📈 Example Queries

```sql
-- Sales by Product
SELECT * FROM v_sales_by_product;

-- Sales by Customer
SELECT * FROM v_sales_by_customer;

-- Daily Revenue
SELECT * FROM v_sales_daily;
```

---

## 🧑‍💻 Author

**Yassin Mahmoud Alam Elden**  
3rd Year CSE Student, Egypt-Japan University of Science and Technology  

📧 Email: [yassin.alam@gmail.com](mailto:yassin.alam@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/yassin-mahmoud-6130b5228) \
[GitHub](https://github.com/yassinalamelden)
