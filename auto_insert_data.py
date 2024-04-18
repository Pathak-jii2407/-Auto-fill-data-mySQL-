
import mysql.connector
from faker import Faker
import random

host=input('Enter Host: ')
user=input('Enter User: ')
password=input('Enter Password: ')

fake = Faker()

def job_title():
    title_names = [
        "CEO (Chief Executive Officer)",
        "CFO (Chief Financial Officer)",
        "HR Specialist",
        "Accountant",
        "Customer Support Specialist",
        "Data Analyst",
        "Graphic Designer",
        "Operations Manager",
        "Quality Assurance Analyst",
        "Business Analyst",
        "Product Manager",
        "IT Administrator",
        "Network Engineer",
        "Administrative Assistant",
        "Legal Counsel",
        "Research and Development Specialist",
        "UX/UI Designer",
        "Systems Analyst",
        "Financial Analyst",
        "Procurement Specialist",
        "Training Coordinator",
        "Event Coordinator",
        "Content Writer",
        "Social Media Manager",
    ]
    return random.choice(title_names)

def create_phone_num():
    return random.randint(1000000000, 9999999999)

def get_email():
    return fake.email()

def create_database_and_table(conn, cursor, database_name, table_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), email VARCHAR(100), phone_num BIGINT, salary INT, job_title VARCHAR(100))")
        conn.commit()
        print(f"Database '{database_name}' and table '{table_name}' created successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)

def insert_data(cursor, table_name, num_rows):
    for i in range(num_rows):
        email = get_email()
        phone_num = create_phone_num()
        salary = random.randint(1000, 10000)  
        job = job_title()
        cursor.execute(f"INSERT INTO {table_name} (username, email, phone_num, salary, job_title) VALUES (%s, %s, %s, %s, %s)", (email[:7], email, phone_num, salary, job))

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    database_name = input("Enter database name: ")
    table_name = input("Enter table name: ")
    num_rows = int(input("Enter number of rows to insert: "))

    create_database_and_table(conn, cursor, database_name, table_name)
    insert_data(cursor, table_name, num_rows)
    conn.commit()
    print(f"{num_rows} rows inserted successfully.")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'conn' in locals():
        conn.close()
