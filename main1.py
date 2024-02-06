#importing all the required libraries and packages.

import pymongo
from pymongo import MongoClient
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

# connecting to mysql workbench & MongoDB server (database)

try:
    connection = mysql.connect(host='localhost',database='diamonds',user='root',password='root')  #connection with MySQL
    cluster = pymongo.MongoClient("mongodb://localhost:27017")     # connecting with MongoDB

    if connection.is_connected():
        db_Info = connection.get_server_info() 
        print("Connected to MySQL Server version ", db_Info)  # getting the  server info
        cursor = connection.cursor()                          # initializing the cursor
        cursor.execute("select database();")                  # selecting the database diamond 'executing sql cmnd'
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        mycursor = connection.cursor()
except Error as e:
    print("Error while connecting to Database", e)     


def ip_execution_query():
    exe_query=input("Enter a execution query\n")

    return exe_query


# Function to extract Data from the database

def extract_data(exe_query):
    mycursor.execute(exe_query)  # executing the query to fetch all record from diamond record
    table_rows = mycursor.fetchall()  # used to fetch all the rows from mycursor

    return table_rows
       
# Function to transform the data using pandas dataFrame

def transform_data(table_rows):
    df = pd.DataFrame(table_rows,columns=["carat","cut", "color","clarity","depth","table1","price","x","y","z"])
    dup=df  
    new_df = dup.drop(columns=["depth","table1"])   # Transforming the data by Dropping unwanted fields
 
    print(new_df)
    return new_df


def close_connection():
    if connection.is_connected():
        cursor.close()
        connection.close()                     # close the database connection
        print('mysql connection is closed')


def load_data_into_MongoDB(dataFrame):
    new_df=dataFrame
    db = cluster["testdb"]
    collection = db["test"]
    
    # Inserting values to table test 
    x = collection.insert_many(new_df.to_dict('records')) #myresult comes from mysql cursor
    
    print(len(x.inserted_ids))
    print("data loaded into MongoDB\n")


if __name__ == "__main__":
    userQuery=ip_execution_query()
    xtractedData=extract_data(userQuery)
    dataFrame=transform_data(xtractedData)
   
    load_data_into_MongoDB(dataFrame)
    close_connection()
    




