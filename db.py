from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
driver = os.getenv('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
encoded_connection_string = urllib.parse.quote_plus(connection_string)
engine_url = f"mssql+pyodbc:///?odbc_connect={encoded_connection_string}"

engine = create_engine(engine_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
