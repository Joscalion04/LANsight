import time
import psycopg2
import os

db_host = os.getenv("POSTGRES_HOST", "db")
db_port = int(os.getenv("POSTGRES_PORT", 5432))
db_user = os.getenv("POSTGRES_USER", "postgres")
db_pass = os.getenv("POSTGRES_PASSWORD", "postgres")
db_name = os.getenv("POSTGRES_DB", "lansight")

while True:
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_pass,
            dbname=db_name
        )
        conn.close()
        print("PostgreSQL is ready!")
        break
    except Exception:
        print("Waiting for PostgreSQL...")
        time.sleep(2)
