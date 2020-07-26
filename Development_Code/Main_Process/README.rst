Instruction Documents:
**********************************
This instruction document is for the Main Process, which the parent process for this project. Main_Process.py is the process which is the combination of all individual process. Main Process will first call the Face Recognition process to identify the person. It will call Database-related code for register new users, modify user data, search user data, and in every step, this process will call Speech Recognition.

Also, this folder contains Python program for generating reports.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux System.

System Set-Up:
-----------------------------------
There are a couple of Python packages and databases that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites:
-----------------------------------
* A system running on Windows/Ubuntu APP/Ubuntu OS
* A user account with sudo/administration privileges
* Access to a terminal window/command-line

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo or administration privileges and completed all the necessary steps from the Installation_Documents_ folder.

In this tutorial, we will explain all the Main Process Codes that are written in Python3 on Ubuntu. We have some codes related to Database as follows:

Both of this Process deals with main customer details tables. Which contains all the information of the users. The main tables are in the following table:

•	Development (DEV) : carego_customer_dev
•	Test (TEST) : carego_customer_test
•	Production (PROD) : carego_customer_prod

This program uses database connection from Python as follow :

conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")

Main Process Code:
-----------------------------------
Main Process related code is written in Python as follow:

1. Main_Process.py_:
The main Process will first call the Face Recognition process to identify the person. It will call Database-related code for register new users, modify user data, search user data, and in every step, this process will call Speech Recognition.

It will first detect the person face in the real-time video camera, and depending on the detection, this process will perform the following steps:

1.	If the Robot detects the face, then will do some steps as follow :

•	Greet the user by saying the name.
•	Ask the user if they want to search for someone.
•	Ask the user if they are going to modify their old details.
•	Ask if they are going to see emergency evacuation procedures again.
•	Ask the user if they want to know more about TELIA.
•	Lastly, the Robot will ask the user to sign the visitor sheet.

2.	If the Robot cannot detect the face, then will do some steps as follow :

•	Ask the name of the person.
•	Ask the organization name.
•	Ask the user if they want to add or register.
•	Ask the user if they are going to save their picture.
•	Ask the user if they are going to search for someone.
•	Ask the user if they want to modify their old details.
•	Will show emergency evacuation procedures.
•	Ask the user if they want to know more about TELIA.
•	Lastly, the Robot asks the user to sign the visitor sheet.

This program has some parameter related function such as process_parameter_set(). This function contains the region value and Main_directory. Depending on the region value, the program will select the respective tables and main_directory is where you should have all the code’s folder. It would be best to make sure that all the folder of Database_Code, Face_Recognition_Code, Speech_Recongnition_Code, Main_Process, and Web_Application_Code are present in this following directory. If you want another specific folder, then you need to make a change here.

2. Carego_Customer_Reports.py_:
Carego_Customer_Reports.py program will fetch the records from the table and will create a CSV file.

This program has some parameter related function such as process_parameter_set(). This function contains the Report name, Report path (main_directory). It would be best to make sure that main_directory is present. If not, then this program will create this directory automatically. Because in this path report will generate.

.. _Main_Process.py: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Main_Process/Main_Process.py
.. _Carego_Customer_Reports.py: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Main_Process/Carego_Customer_Reports.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Main_Process_Document_

.. _Main_Process_Document: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Robotic_Greeter_Documents/Main_Process_Documents/Main_Process_Document_Version_1.pdf

Executing:
-------------
If you have done all the steps mentioned above, then please run any of the code as
follow::

    $ chmod +x *.py

    $ python3 Main_Process.py

    $ python3 Carego_Customer_Reports.py

