**Case Study on Data Integration (ETL) Process** 

**Introduction:**
In this case study, we have worked on fundamentals of ETL process. Focusing on the migration of data from a MySQL database to a MongoDB database using the Diamonds dataset sourced from Kaggle.


**Requirements/Technologies:**

Python: Used for scripting and data manipulation.
MySQL Workbench, Server: Source database for storing the Diamonds dataset.
MongoDB: Target NoSQL database for storing transformed data.
Libraries: mysql.connector, pymongo, pandas for database connectivity and data manipulation.

**Implementation:**

In this project, we choose MySQL workbench as our source database and MongoDB as a target database. 

**Step-1:**

Utilised MySQL Workbench as the source database.
Established connection to the MySQL database using mysql.connector library in Python.
Extracted the Diamonds dataset from MySQL using SQL queries.

**Step-2:**

Loaded the extracted data into Python as a DataFrame using the pandas library.
Performed necessary data transformations as per user requirements.
Filtered Data as per the user queries. 

**Step-3:**

Connected to MongoDB using pymongo library.
Loaded the transformed data from Python DataFrame to MongoDB collections.

**Conclusion:**
Got the basic understanding of ETL procedure. Performed CRUD operations on SQL data and Migrated structured data from SQL to MongoDB.


**References:**
Kaggle: Diamonds Dataset
MongoDB Documentation
W3Schools.com
StackOverflow.com



