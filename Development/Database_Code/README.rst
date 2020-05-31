Instruction Documents - README :
**********************************

Database Code :
-----------------------------------

This folder contains all the database related code written in Python as follow:

1. Customer_Insert.py_ :

2. Customer_Search_Main.py_ :

* A. Customer_search_ID.py_ :
* B. Customer_search_Name.py_ :

3. Customer_Update.py_ :

.. _Customer_Insert.py : https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Insert.py
.. _Customer_Search_Main.py : https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Search_Main.py
.. _Customer_search_ID.py : https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Search_ID.py
.. _Customer_search_Name.py : https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Search_Name.py
.. _Customer_Update.py : https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Update.py

Install Python Package :
-----------------------------------
There are a couple of python packages that need to validate before running any above
program in this folder. Assuming that you have already installed python 3.6
(or above), Pip, and Git. If not, then please go to the Installation_Documents_ and
do the needful first

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents

Prerequisites :
-----------------------------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Now, after you finished, Install Python Package step then validate python3, pip &
Git on your computer as follows:

Run the following command to go in python console::

    $ python3

Run the following import command inside of the python console::

    >> import re
    >> import sys
    >> import subprocess
    >> from datetime import date, datetime
    >> from subprocess import check_output, call
    >> import psycopg2

Regex (re), sys, and subprocess module comes python installation. Since it is
build-in packages.

If you get any error after running the above import command, you should validate
the python version or upgrade it. You should not acquire any mistake if you installed
Python correctly or followed all steps from the Installation_Documents_ folder.

There are two way you can install the packages:

Install Psycopg2 :
-----------------------------------
Psycopg2 is an extra module that you need to import here to run this code. To
install Psycopg2, please go to the Postgresql_pgAdmin_Installation_ folder. Also,
you can find the same folder inside the Installation_Documents_ folder.

Before running any of this code, please read the documents from
Postgresql_pgAdmin_Installation_ folder. Since you need to create a Database,
Table, etc., and also need to validate it.

.. _Postgresql_pgAdmin_Installation:

Executing :
-------------
If you done all the above mentioned steps then please run any of the code as
follow ::

    $ python3 Customer_Insert.py
    $ python3 Customer_Search_Main.py
    $ python3 Customer_Search_ID.py
    $ python3 Customer_Search_Name.py
    $ python3 Customer_Update.py

