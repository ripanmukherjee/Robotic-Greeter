Instruction Documents:
**********************************
This instruction document is for all the Web Application related code, where we have codes that needs to run before to access Web Application. Also, this folder contains different HTML5 + CSS3 codes for Web Pages. In this project, we have used the Python Flask API module.

Flask is a web framework. This means Flask provides you with tools, libraries, and technologies to build a web application. This web application can be some web pages, a blog, a wiki, or go as big as a web-based calendar application or a commercial website.

Flask is part of the categories of the micro-framework. Micro-framework is usually a framework with little to no dependencies on external libraries. This has pros and cons. The advantage would be that the frame is light. There is a low dependency to update and watch for security bugs; a disadvantage is that sometimes you will have to do more work by yourself or increase yourself the list of dependencies by adding plugins.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux System.

System Set-Up:
-----------------------------------
There are a couple of Python packages that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites:
-----------------------------------
•	A system running on Windows/Ubuntu APP/Ubuntu OS
•	A user account with sudo/administration privileges
•	Access to a terminal window/command-line
•	Validate Flask Module (Flask comes with Python installation in Ubuntu, but if you do not have Flask installed on your computer, please visit here_ for installation)

.. _here: https://flask.palletsprojects.com/en/0.12.x/installation/

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo or administration privileges and completed all the necessary steps from the Installation_Documents_ folder.

In this tutorial, we will explain all the Web Application Codes written in Python3 and Flask on Ubuntu.

1.	Web_Application_Frontend.py
2.	Web_Application_Backend.py

Web Application Code:
-----------------------------------
This folder contains all the Web Application related code written in Python as follow:

1. Web_Application_Frontend.py_:
Web_Application_Frontend.py is the main Python program that needs to run to access Web Application. This program will first call home.html to show to the home page in the Web Application. Based on the user’s selection, this program will call another HTML program on the home page in Web Application. Also, this program will call the Web_Application_Backend.py process if the user wants to do a specific process.

This program contains specific parameter which needs to validate and check before running this program.

Also, you can run this program as a stand-alone program.

2. Web_Application_Backend.py_:
Web_Application_Backend.py program will be call from Web_Application_Frontend.py based on user's selection. Web_Application_Frontend.py will pass an input argument to this process and based on the input argument; this process will call a different Python programs such as Customer_Insert.py. Customer_Update.py, Customer_Search_Main.py, Main_Proces.py, Speech_Emergency_Evacuation_Procedure.py etc.

This program has one function called process_parameter_set(), which contains the value of main_directory. It would be best to make sure that all the folder of Database_Code, Face_Recognition_Code, Speech_Recongnition_Code, Main_Process, and Web_Application_Code are present in this following directory. If you want another specific folder, then you need to make a change here.

Also, you can run this program as a stand-alone program.

3. templates_:
This is the folder which contains all the HTML5 + CSS3 codes.

.. _Web_Application_Frontend.py:  https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Web_Application_Code/Web_Application_Frontend.py
.. _Web_Application_Backend.py:   https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Web_Application_Code/Web_Application_Backend.py
.. _templates:                    https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development_Code/Web_Application_Code/templates

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Web_Application_Code_Document_

.. _Web_Application_Code_Document:

Executing:
-------------
If you have done all the steps mentioned above, please run any of the code::

    $ chmod +x *.py

    $ python3 Web_Application_Frontend.py

    $ python3 Web_Application_Backend.py

