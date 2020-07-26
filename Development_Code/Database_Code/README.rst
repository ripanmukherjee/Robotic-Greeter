Database Code Document:
**********************************
This instruction document is for all the database related code, where we have codes for inserting data into the database, search the data from database based on ID or Name and, codes for update the details on the database. In this project, we are using PostgreSQL Database.

PostgreSQL is a powerful, open-source object-relational database system with over 30 years of active development that has earned a strong reputation for reliability, feature robustness, and performance. PostgreSQL is available in all Ubuntu versions by default. However, Ubuntu "snapshots" a specific version of PostgreSQL that is supported throughout the lifetime of that Ubuntu version. Other versions of PostgreSQL are available through the PostgreSQL apt repository. You can also download and install it on Windows 10.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux System for this project.

System Set-Up:
-----------------------------------
There are a couple of Python packages and databases that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites
-----------------------------------
•	A system running on Windows/Ubuntu APP/Ubuntu OS
•	A user account with sudo/administration privileges
•	Access to a terminal window/command-line

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo or administration privileges and completed all the necessary steps from the Installation_Documents_ folder.

In this tutorial, we will explain all the Database Codes that are written in Python3 on Ubuntu. We have some codes related to Database as follows:

1.	Customer_Insert.py
2.	Customer_Search_Main.py
3.	Customer_Search_ID.py
4.	Customer_Search_Name.py
5.	Customer_Update.py

All the Python codes in Database Code folder deals with main customer details tables. Which contains all the information of the users. The main tables are in the following table:

•	Development (DEV) : carego_customer_dev
•	Test (TEST) : carego_customer_test
•	Production (PROD) : carego_customer_prod

Only, Customer_Insert.py program uses following sequence table. Sequence table is important which helps to create auto increment ID for the main table.

•	carego_customer_dev_ID_seq

Most of the program uses database connection from Python  as follow :
conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")

Currently, we only used the carego_customer_dev table since it is only in the development phase. Each of the codes in this folder has one function called process_parameter_set(), which contains the region value. Depending on the region value, the programs will select the respective tables. Hence it is essential to validate this function before running any codes.

Also, it is crucial to verify the tables and database connection details before running any programs. Please go through the PostgreSQL_pgAdmin4_Installation_ document, which is present inside of Installation_Documents_ folder for all the necessary details.

.. _PostgreSQL_pgAdmin4_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents/PostgreSQL_pgAdmin4_Installation

Database Code :
-----------------------------------
Database related code is written in Python as follow:

1. Customer_Insert.py_:
Customer_Insert.py is use for inserting the data of the user into the table mentioned above. This program will be called from Main_Process.py. If the user wants to save their details in the database, then Main_Process.py will call this program, and this process will insert the data into the table mentioned above.

Also, you can run this program as a stand-alone program.

2. Customer_Search_Main.py_:
Customer_Search_Main.py is used to search the user's data, and it will be called from Main_Process.py. If the user wants to explore the data, this process will ask the user wants to search by ID or Name, and as per the selection, this program will call the below two programs:

Also, you can run this program as a stand-alone program.

* Customer_Search_ID.py_: Customer_Search_ID.py is used to search the user's data from the table mentioned above by using an ID. This program will be called from Customer_Search_Main.py based on search criteria. If the user selects the ID option in Customer_Search_Main.py, then it will call Customer_Search_ID.py. And this program will ask the ID and search the data. Also, you can run this program as a stand-alone program.

* Customer_Search_Name.py_: Customer_Search_Name.py is used to search the data of the user from the table mentioned above. This program will be called from Customer_Search_Main.py based on search criteria. If the user selects the Name option in Customer_Search_Main.py, then it will call Customer_Search_Name.py. And this program will ask the Name and search the data. Also, you can run this program as a stand-alone program.

3. Customer_Update.py_:
Customer_Update.py is used to update the data of the user into the table mentioned above. This program will be called from Main_Process.py if the user wants to update their details. To update the details, the user should know their unique ID, as this program will ask to confirm the ID before updating.

Also, you can run this program as a stand-alone program.

.. _Customer_Insert.py:         https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Insert.py
.. _Customer_Search_Main.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Search_Main.py
.. _Customer_Search_ID.py:      https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Search_ID.py
.. _Customer_Search_Name.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Search_Name.py
.. _Customer_Update.py:         https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Update.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Database_Code_Document_

.. _Database_Code_Document: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Robotic_Greeter_Documents/Database_Code_Documents/Database_Code_Document_Version_1.pdf

Executing:
-------------
If you have done all the steps mentioned above, then please run any of the code as
follow::

    $ chmod +x *.py

    $ python3 Customer_Insert.py

    $ python3 Customer_Search_Main.py

    $ python3 Customer_Search_ID.py

    $ python3 Customer_Search_Name.py

    $ python3 Customer_Update.py

