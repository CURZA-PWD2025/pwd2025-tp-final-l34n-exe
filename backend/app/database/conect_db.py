import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

class ConectDB:
    @staticmethod
    def get_connect():
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                port=os.getenv("DB_PORT", 3306)

            )
            return connection
        except Exception as exc:
            print(f"Error: {exc}")
            return None

    @staticmethod
    def read(sql: str, params: tuple = None):
        conn = ConectDB.get_connect()
        with conn.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result if result else None
            except Error as e:
                print(f'Error {e}')
            finally:
                conn.close()

    @staticmethod
    def write(sql: str, params: tuple):
        conn = ConectDB.get_connect()
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                conn.commit()
                if cursor.lastrowid:
                    return cursor.lastrowid
                return cursor.rowcount > 0
            except Error as e:
                print(f'Something went wrong {e}')
            finally:
                conn.close()