Instruction Documents:
**********************************
This instruction document is for the main process which the parent process for this project. Main_Process.py is the process which will perform all the process together.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use
Linux for this project.

Main Process Code:
-----------------------------------
The Main_Process.py python code deals with the following table:

* Development (DEV) : carego_customer_dev
* Test (TEST) : carego_customer_test
* Production (PROD) : carego_customer_prod


1. Main_Process.py_:
This program is the main program which will perform face_detection, speech_recognition & database_code.

It will first detect the person face in the real time video camera and later it will perform some other features.

* If the Robot detect the face then will do some steps as follow :

  1. Greet by saying the name of the person,
  2. Ask the person if they want to meet or search somebody, if they want to modify their old data,
  3. etc.

* If the Robot cannot detect the face then will do some steps as follow :
  1. Ask the person name and organization,
  2. Ask the person if they want to save their details and photos,
  2. Ask the person if they want to meet or search somebody, if they want to modify their old data
  3. etc.

2. Carego_Customer_Reports.py_: Carego_Customer_Reports.py program will fetch the records from the table and will create a CSV file.


.. _Main_Process.py: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Main_Process/Main_Process.py
.. _Carego_Customer_Reports.py: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Main_Process/Carego_Customer_Reports.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Main_Process_Document_

.. _Main_Process_Document:

System Set-Up:
-----------------------------------
There are a couple of Python packages and databases that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

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

    $ python3 Main_Process.py

    $ python3 Carego_Customer_Reports.py

