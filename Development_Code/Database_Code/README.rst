Instruction Documents:
**********************************
This instruction document is for all the database related code, where we have codes for inserting data into database, search the data from database based on ID or Name and also, codes for update the details on the database.

Note: This project is developed on a Linux System (Ubuntu), so, it is advisable to use Linux for this project.

Database Code:
-----------------------------------
All the python code in Database Code folder deals with the following table:

* Development (DEV) : carego_customer_dev
* Test (TEST) : carego_customer_test
* Production (PROD) : carego_customer_prod

Database related code written in Python as follow:

1. Customer_Insert.py_:
Customer_Insert.py is use for inserting the data of the customer into the above mentioned table.

This program will be called from Main_Process.py. If the customer wants to save their details in the database then Main_Process.py will call this program, and this process will insert the data into the table mentioned above.

Also, you can run this program as stand alone program.

2. Customer_Search_Main.py_:
Customer_Search_Main.py is used to search the customer's data, and it will be called from Main_Process.py. If the customer wants to explore the data, then this process will ask to the customer wants to search by ID or Name, and as per the selection this program will call the below two program:

Also, you can run this program as stand alone program.

* Customer_Search_ID.py_: Customer_Search_ID.py is use to search the data of the customer from the above mentioned table by using ID.  This program will be called from Customer_Search_Main.py based on search criteria. If the customer select ID option in Customer_Search_Main.py, then it will call Customer_Search_ID.py. And this program will ask the ID and search the data. Also, you can run this program as stand alone program.
* Customer_Search_Name.py_: Customer_Search_Name.py is use to search the data of the customer from the above mentioned table. This program will be called from Customer_Search_Main.py based on search criteria. If the customer select Name option in Customer_Search_Main.py, then it will call Customer_Search_Name.py. And this program will ask the Name and search the data. Also, you can run this program as stand alone program.

3. Customer_Update.py_:
Customer_Update.py is use to update the data of the customer into the above mentioned table. This program will be called from ~/Main_Process/Main_Process.py, if the customer wants to update their details. To update the details, customer should know their unique ID, as this program will ask confirm the ID before to update.

Also, you can run this program as stand alone program.

.. _Customer_Insert.py:         https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Insert.py
.. _Customer_Search_Main.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Search_Main.py
.. _Customer_Search_ID.py:      https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Search_ID.py
.. _Customer_Search_Name.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Search_Name.py
.. _Customer_Update.py:         https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Database_Code/Customer_Update.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs then please go to Database_Code_Document_

.. _Database_Code_Document:

System Set Up:
-----------------------------------
There are a couple of Python packages and database that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites:
-----------------------------------
* A system running on Windows/Ubuntu APP/Ubuntu OS
* A user account with sudo/administration privileges
* Access to a terminal window/command-line

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

