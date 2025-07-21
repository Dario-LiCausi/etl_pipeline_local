import os
import mysql.connector
from dotenv import load_dotenv
from datetime import datetime

def load_to_mysql(clean_sales):
    # Load environment variables
    load_dotenv(dotenv_path='db/.env')

    # Connect to db
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=os.getenv('MYSQL_PORT'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    cursor = conn.cursor()

    # Create table if not exists
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS sales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Drink VARCHAR(100),
        Qty INT,
        Price FLOAT,
        Branch VARCHAR(100),
        Payment_Type VARCHAR(50),
        Date_Time DATETIME
    )
    '''
    cursor.execute(create_table_query)

    # SQL Insert Query
    insert_query = """
        INSERT INTO sales (Drink, Qty, Price, Branch, Payment_Type, Date_Time)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for _, row in clean_sales.iterrows():
        # Convert 'Date/Time' from 'DD/MM/YYYY' to Python datetime object
        dt = datetime.strptime(row['Date/Time'], '%d/%m/%Y')
        cursor.execute(insert_query, (
            row['Drink'],
            int(row['Qty']),
            float(str(row['Price']).replace('£', '')),
            row['Branch'],
            row['Payment Type'],
            dt
        ))

    # Finalize
    conn.commit()
    cursor.close()
    conn.close()