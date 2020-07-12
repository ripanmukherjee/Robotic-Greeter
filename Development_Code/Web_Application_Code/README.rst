Instruction Documents:
**********************************
This instruction document is for all the Web Application related code, where we have codes that needs to run before to access Web Application. Also, this folder contains different HTML5 + CSS3 codes for Web Pages.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux for this project.

Speech Recognition Code:
-----------------------------------

This folder contains all the Web Application related code written in Python as follow:

1. Web_Application_Frontend.py_:
Web_Application_Frontend.py is the main python program which needs to run to access web application. This program will first call home.html to show to home page in the web application. On the home page in web application, based on customer selection, this program will call other html program. Also, this program will call Web_Application_Backend.py process if user wants to do certain process.

Also, you can run this program as a stand-alone program.

2. Web_Application_Backend.py_:
Web_Application_Backend.py program will be call from Web_Application_Frontend.py based on user's selection. Web_Application_Frontend.py will pass an input argument to this process and based on the input argument this process will call different python program.

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

System Set-Up:
-----------------------------------
There are a couple of Python packages that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites:
-----------------------------------
* A system running on Windows/Ubuntu APP/Ubuntu OS
* A user account with sudo/administration privileges
* Access to a terminal window/command-line

Executing:
-------------
If you have done all the steps mentioned above, please run any of the code::

    $ chmod +x *.py

    $ python3 Web_Application_Frontend.py

    $ python3 Web_Application_Backend.py

