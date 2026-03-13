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

def load_sales_report(records):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM sales_report_etl;")

    insert_query = """
        INSERT INTO sales_report_etl (
            order_id,
            order_date,
            customer_id,
            customer_name,
            city,
            product_id,
            product_name,
            category,
            quantity,
            price,
            total_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    for record in records:
        cursor.execute(
            insert_query,
            (
                record["order_id"],
                record["order_date"],
                record["customer_id"],
                record["customer_name"],
                record["city"],
                record["product_id"],
                record["product_name"],
                record["category"],
                record["quantity"],
                record["price"],
                record["total_amount"]
            )
        )

    connection.commit()
    cursor.close()
    connection.close()