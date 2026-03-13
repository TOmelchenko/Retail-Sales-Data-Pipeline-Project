import json
import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()

with open("config/settings.json") as f:
    settings = json.load(f)

def get_connection():
    return psycopg2.connect(
        dbname=settings["db_name"],
        user=settings["db_user"],
        password=os.getenv("DB_PASSWORD"),
        host=settings["db_host"],
        port=settings["db_port"]
    )

def load_raw_customers(customers, connection):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM raw_customers;")

    insert_query = """
        INSERT INTO raw_customers (
            customer_id,
            customer_name,
            city,
            signup_date
        )
        VALUES (%s, %s, %s, %s);
    """

    for customer in customers:
        cursor.execute(
            insert_query,
            (
                customer.get("customer_id"),
                customer.get("customer_name"),
                customer.get("city"),
                customer.get("signup_date")
            )
        )
    cursor.close()


def load_raw_products(products, connection):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM raw_products;")

    insert_query = """
        INSERT INTO raw_products (
            product_id,
            product_name,
            category,
            price
        )
        VALUES (%s, %s, %s, %s);
    """

    for product in products:
        cursor.execute(
            insert_query,
            (
                product.get("product_id"),
                product.get("product_name"),
                product.get("category"),
                product.get("price")
            )
        )
    cursor.close()

def load_raw_orders(orders, connection):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM raw_orders;")

    insert_query = """
        INSERT INTO raw_orders (
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
        )
        VALUES (%s, %s, %s, %s, %s);
    """

    for order in orders:
        cursor.execute(
            insert_query,
            (
                order.get("order_id"),
                order.get("customer_id"),
                order.get("product_id"),
                order.get("quantity"),
                order.get("order_date")
            )
        )
    cursor.close()
from pathlib import Path


def run_sql_file(file_path, connection):
    cursor = connection.cursor()

    sql_path = Path(file_path)
    sql_content = sql_path.read_text(encoding="utf-8")

    cursor.execute(sql_content)
    connection.commit()
    cursor.close()




