import os 
from dotenv import load_dotenv
from faker import Faker 
import random
import pyodbc
import pandas as pd


load_dotenv()

server = os.getenv("DB_SERVER")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


conn_str = (
    "DRIVER= {ODBC Driver 18 for SQL Server};"
    "SERVER=server;"
    "UID=user;"
    "PWD=password;"
    "encrypt=no;"
    "TrustServerCertificate=yes;"
)


fake = Faker()



try:
    # 2. Connect and create the Database
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()
    cursor.execute(f"IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{db_name}') CREATE DATABASE [{db_name}];")
    print(f"✅ Database '{db_name}' is ready.")

    # 3. Create the Schema (3 Tables with Relationships)
    cursor.execute(f"USE [{db_name}];")

    '''
    cursor.execute("""
        CREATE TABLE Clients (ClientID INT PRIMARY KEY, Name NVARCHAR(100), Country NVARCHAR(50));
        CREATE TABLE Products (ProductID INT PRIMARY KEY, ProductName NVARCHAR(100), Price DECIMAL(10,2));
        CREATE TABLE Transactions (
            TxID INT PRIMARY KEY IDENTITY(1,1),
            ClientID INT FOREIGN KEY REFERENCES Clients(ClientID),
            ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
            Amount DECIMAL(18,2),
            TxDate DATETIME
        );
    """)

    # 4. Insert Mock Data using Faker
    for i in range(1, 6): # Create 5 Clients
        cursor.execute("INSERT INTO Clients VALUES (?, ?, ?)", i, fake.name(), fake.country())
    
    for i in range(1, 4): # Create 3 Products
        cursor.execute("INSERT INTO Products VALUES (?, ?, ?)", i, fake.word().capitalize(), random.uniform(10, 500))

    for _ in range(20): # Create 20 random transactions
        cursor.execute(
            "INSERT INTO Transactions (ClientID, ProductID, Amount, TxDate) VALUES (?, ?, ?, ?)",
            random.randint(1, 5), random.randint(1, 3), random.uniform(50, 2000), fake.date_this_year()
        )

    print("✅ Successfully populated 3 tables with relationships!")
    conn.close()
'''
except Exception as e:
    print(f"❌ Connection failed: {e}")

