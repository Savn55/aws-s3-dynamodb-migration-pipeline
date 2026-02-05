import pandas as pd
import os 
import pyodbc
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


conn_str = (
    "DRIVER= {ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"UID={user};"
    f"PWD={password};"
    f"encrypt=no;"
    f"TrustServerCertificate=yes;"
)

try:
    print("Connecting to Docker SQL Server...")
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()
    cursor.execute(f"USE [{db_name}];")

    print(f"Extracting data from {db_name}...")
    df = pd.read_sql("SELECT * FROM dbo.Clients", conn)

    # print("converting data to csv")
    df.to_csv("clients_export.csv", index=False)
    print("✅ Data exported to clients_export.csv successfully.")
    print(f"Total rows exported: {len(df)}")

except Exception as e:
    print(f"❌ Operation failed: {e}")

finally:
    if 'conn' in locals():
        conn.close()