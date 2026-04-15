from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:Learning%40841@localhost:3306/sales_db")

# -------------------------------
# 1. Month-over-Month Growth
# -------------------------------
mom_query = """
WITH monthly_sales AS (
    SELECT 
        DATE_FORMAT(order_date, '%Y-%m-01') AS month,
        SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY month
)
SELECT 
    month,
    total_sales,
    ROUND(
        (total_sales - LAG(total_sales) OVER (ORDER BY month)) * 100.0 /
        LAG(total_sales) OVER (ORDER BY month),
    2) AS mom_growth
FROM monthly_sales;
"""

# -------------------------------
# 2. Top 3 Customers Per Month
# -------------------------------
top_customers_query = """
WITH customer_sales AS (
    SELECT 
        DATE_FORMAT(order_date, '%Y-%m-01') AS month,
        customer_id,
        SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY month, customer_id
)
SELECT *
FROM (
    SELECT 
        *,
        DENSE_RANK() OVER (
            PARTITION BY month 
            ORDER BY total_sales DESC
        ) AS rnk
    FROM customer_sales
) ranked
WHERE rnk <= 3;
"""

# -------------------------------
# 3. Avg Time Between Orders
# -------------------------------
avg_time_query = """
WITH ordered AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS rn
    FROM sales
),
pairs AS (
    SELECT 
        customer_id,
        MAX(CASE WHEN rn = 1 THEN order_date END) AS first_order,
        MAX(CASE WHEN rn = 2 THEN order_date END) AS second_order
    FROM ordered
    GROUP BY customer_id
)
SELECT 
    AVG(DATEDIFF(second_order, first_order)) AS avg_days_between_orders
FROM pairs
WHERE second_order IS NOT NULL;
"""

# Execute all queries
with engine.connect() as conn:
    print("\n MoM Growth:")
    for row in conn.execute(text(mom_query)):
        print(row)

    print("\n Top Customers:")
    for row in conn.execute(text(top_customers_query)):
        print(row)

    print("\n Avg Time Between Orders:")
    for row in conn.execute(text(avg_time_query)):
        print(row)