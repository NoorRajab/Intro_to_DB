import mysql.connector
from mysql.connector import errorcode

MYSQL_USER = "root"  
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
DB_NAME = "alx_book_store"

def create_database():
    
    db_connection = None
    
    try:
        
        db_connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        
        if db_connection.is_connected():
            cursor = db_connection.cursor()
            
            
            sql_query = f"CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            print(f"Attempting to create database '{DB_NAME}'...")
            
            
            cursor.execute(sql_query)
            
           
            print(f"Database '{DB_NAME}' created successfully!")
            
           
            cursor.close()
            
    except mysql.connector.Error as err:
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Failed to connect or create database: {err}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    finally:
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
