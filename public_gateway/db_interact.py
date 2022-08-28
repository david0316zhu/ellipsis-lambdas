import os
import psycopg2
import json
from datetime import datetime, timedelta
from .custom_trace import log_trace_message

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')

def get_db_connection() -> object:
    """This function attempts connection with Database"""
    try:
        print({
                "message": "Getting Database Connection"
              })
        connection = psycopg2.connect(user=DB_USER,
                                      password=DB_PASS,
                                      host=DB_HOST,
                                      database=DB_DATABASE
                                     )
        print({
                "message": "Database Connected"
              })       
        return connection
    except Exception as e:
        print({"message": e.args})
        log_trace_message()
        return None

def get_merchant_services(cursor, merchant_id):
    """This function get kbank credentials"""
    try:
        print({
            "message": "Get Merchant Data"
        })
        
        query = """SELECT data from merchant_services WHERE merchant_id = %s"""
        cursor.execute(query, merchant_id)
        data = cursor.fetchone()[0]
        merchant_data = json.loads(data)
        
        return merchant_data

    except Exception as e:
        print({"message": e.args})
        log_trace_message()
        return None



