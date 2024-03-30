import pyautogui as pg 
import time
from faker import Faker
import os
import random
fake = Faker()


def job_title():
    new_i=random.randint(1,49)
    title_names = [
        "CEO (Chief Executive Officer)",
        "CFO (Chief Financial Officer)",
        "COO (Chief Operating Officer)",
        "CTO (Chief Technology Officer)",
        "CMO (Chief Marketing Officer)",
        "CHRO (Chief Human Resources Officer)",
        "CIO (Chief Information Officer)",
        "General Manager",
        "Project Manager",
        "Team Lead",
        "Software Engineer",
        "Marketing Manager",
        "Sales Representative",
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
        "Customer Success Manager",
        "Scrum Master",
        "Database Administrator",
        "Sales Manager",
        "Compliance Officer",
        "Logistics Coordinator",
        "Front-end Developer",
        "Back-end Developer",
        "DevOps Engineer",
        "Technical Support Specialist",
        "Facilities Manager",
        "Public Relations Specialist",
        "Executive Assistant",
        "Business Development Manager",
        "Data Scientist"
    ]
    return title_names[new_i]


def login():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\MySQL\\MySQL Server 8.0\\MySQL 8.0 Command Line Client.lnk")
    time.sleep(1)
    pg.write('ved24072003')
    pg.press('enter')

def create_phone_num(n):
    num=0
    for i in range(n):
        num=random.randint(1000000000,9999999999)
    return num


def create_use_db(Database_name):
    Create_database=f'CREATE DATABASE IF NOT EXISTS {Database_name};'
    pg.write(Create_database)
    pg.press('enter')
    use_db=f'USE {Database_name};'
    pg.write(use_db)
    pg.press('enter')

def create_table(table_name):
    
    table=f"CREATE TABLE IF NOT EXISTS {table_name} (id INT PRIMARY KEY,username VARCHAR(50),email VARCHAR(100),phone_num BIGINT,salary DOUBLE(12,2),job_title VARCHAR(50));"
    pg.write(table)
    pg.press('enter')

def get_email():
    fake_emails = [fake.email() for _ in range(100)]
    for idx, email in enumerate(fake_emails, start=1):
        return email


def insert_data(no_of_data,table_name):
    for i in range(no_of_data+1):
        time.sleep(0.10)
        pg.write(f"INSERT INTO {table_name} VALUES ({i}, '{get_email()[0:7]}', '{get_email()}', {create_phone_num(no_of_data)},{create_phone_num(no_of_data)//(random.randint(999,99999))}, '{job_title()}');")
        pg.press('enter')

DB_name=input("Enter database name: ")
table_name=input("Enter table name: ")
no_of_data=int(input("Enter number of data: "))

time.sleep(1)

login()
create_use_db(DB_name)
create_table(table_name)
insert_data(no_of_data,table_name)



