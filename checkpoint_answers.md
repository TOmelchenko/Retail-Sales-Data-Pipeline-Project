# Checkpoint Question 1
What is the main difference between ETL and ELT in this mini-project?
In this mini-project for ETL version we have the following sequence:
- extract data from 3 files
- transform them in memory with python scripts
- load transformed data into final table **sales_report_etl**
For ELT there is such  sequence:
- extract data from 3 files
- load data into local Postgres database
- transform and load data into final table **sales_report_elt** with SQL-query 
  
# Checkpoint Question 2
Why does the ETL version transform data in Python before loading it into PostgreSQL?
Because to be align with ETL approach the cleaned/transformed data is loaded into database

# Checkpoint Question 3
Why does the ELT version load raw data into PostgreSQL first before transforming it?
With ELT the raw data uploaded can be used by different users(analysts, BI engineers, ML engineers). They can perform the transformations, what they need.
The second point - with the huge amount of data is better to load it first. The python on memory transformation ca be difficult.  

# Checkpoint Question 4
What are the three raw source files in this project, and what does each one represent in the business scenario?
There are 3 type of files: 
customers.csv - represents raw data about customers. This is dictionary or lookup.
products.xml -  contains data about products. This is also dictionary.
orders.json - consists data about orders: what customer which product/products orders. It's fact data.


# Checkpoint Question 5
Why is this project useful as a portfolio project for future job interviews?

It shows the understanding of ETL and ELT and how these both scenarios can be performed using python and PostgreSQL.

# What I've changed vs original project.

1. The virtual environment **.venv** has been created.
2. I created a separate file **tests.py** for tests.
3. I add **.env** and to read DB_PASSWORD.
4. I use **settings.json** to read 
   ```python
   with open("config/settings.json") as f:
    settings = json.load(f)
   ```
5. For **city** in customers data the empty sting has been replaced with **Unknown**
6. In the **elt_transform.sql** the following row has been added to remove previous data from the report
   ```sql
   DELETE FROM sales_report_elt;
   ```
7. Instead of one **load_postgres.py** the separate scripts for ETL and ELT have been created
8. Open and close database connection in **get_connection()** has been called once in **main** in **run_elt.py**. Accordingly the following functions have been updated not to call **get_connection**
   ```python
   load_raw_customers(customers_raw, connection)
   load_raw_products(products_raw, connection)
   load_raw_orders(orders_raw, connection)
   ```

