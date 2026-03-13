
from extract import read_customers_csv, read_orders_json, read_products_xml 
from transform_etl import build_sales_report, clean_customers, clean_orders, clean_products
from load_postgres import get_connection

def main():
    # test extract files
    customers = read_customers_csv()
    orders = read_orders_json()
    products = read_products_xml()

    print("/n=== 1. Test extract files ===")
    print(f"Customers: {customers[:2]}")
    print(f"Orders: {orders[:2]}")
    print(f"Products: {products[:2]}")

    # test report-ready dataset (before load)
    cleaned_customers = clean_customers(customers)
    cleaned_products = clean_products(products)
    cleaned_orders = clean_orders(orders)
    sales_report =  build_sales_report(cleaned_customers, cleaned_products, cleaned_orders)

    print("/n=== 2. Test report-ready dataset (before load) ===")
    print(f"Sales report: {sales_report[:2]}")

    # test connection
    print("/n=== 3. Test connection ===")
    try:
        conn = get_connection()
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")


if __name__ == "__main__":
    main()