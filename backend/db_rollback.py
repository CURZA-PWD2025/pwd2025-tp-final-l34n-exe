import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
database_name = os.getenv("DB_NAME")

database_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': int(os.getenv("DB_PORT", "3306")),
    'raise_on_warnings': False,
    "database": database_name
}

DROPPED_TB = {}

DROPPED_TB["items_venta_sabores"] = "DROP TABLE IF EXISTS items_venta_sabores;"
DROPPED_TB["items_ventas"] = "DROP TABLE IF EXISTS items_ventas;"
DROPPED_TB["ventas"] = "DROP TABLE IF EXISTS ventas;"
DROPPED_TB["productos"] = "DROP TABLE IF EXISTS productos;"
DROPPED_TB["sabores"] = "DROP TABLE IF EXISTS sabores;"
DROPPED_TB["empleados"] = "DROP TABLE IF EXISTS empleados;"
DROPPED_TB["clientes"] = "DROP TABLE IF EXISTS clientes;"
DROPPED_TB["categoria"] = "DROP TABLE IF EXISTS categoria;"
DROPPED_TB["proveedores"] = "DROP TABLE IF EXISTS proveedores;"



def rollback_db():
    cxn = None
    cursor = None
    try:
        cxn = mysql.connector.connect(**database_config)
        cursor = cxn.cursor()
        for table in DROPPED_TB:
            print(f"Dropped table: {table}", end=" ")
            try:
                cursor.execute(DROPPED_TB[table])
                print('ok')
                cxn.commit()
            except Error as e:
                print(f"Error: {e}")
    except Error as e:
        print(f"Connection error: {e}")
    finally:
        if cursor:
            cursor.close()
        if cxn:
            cxn.close()

rollback_db()
