from extract import read_customers_csv, read_orders_json, read_products_xml
from load_postgres_elt import (
    get_connection,
    load_raw_customers,
    load_raw_orders,
    load_raw_products,
    run_sql_file
)


def main():
    customers_raw = read_customers_csv()
    orders_raw = read_orders_json()
    products_raw = read_products_xml()

    connection = get_connection()

    load_raw_customers(customers_raw, connection)
    load_raw_products(products_raw, connection)
    load_raw_orders(orders_raw, connection)

    connection.commit()
    
    run_sql_file("sql/elt_transform.sql", connection) 

    connection.close()

    print("ELT completed successfully. Raw data loaded and SQL transformations applied.")


if __name__ == "__main__":
    main()