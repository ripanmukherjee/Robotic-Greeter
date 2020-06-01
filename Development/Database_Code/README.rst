Instruction Documents - README :
**********************************

Database Code :
-----------------------------------

This folder contains all the database related code written in Python as follow:

1. Customer_Insert.py_:

2. Customer_Search_Main.py_:

* A. Customer_Search_ID.py_:
* B. Customer_Search_Name.py_:

3. Customer_Update.py_:

.. _Customer_Insert.py:         https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Insert.py
.. _Customer_Search_Main.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Search_Main.py
.. _Customer_Search_ID.py:      https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Search_ID.py
.. _Customer_Search_Name.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Search_Name.py
.. _Customer_Update.py:         https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Database_Code/Customer_Update.py

Install Python Package :
-----------------------------------
There are a couple of Python packages that need to validate before running any above
program in this folder. Assuming that you have already installed Python 3.6
(or above), Pip, and Git. If not, then please go to the Installation_Documents_ and
do the needful first.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents

Prerequisites :
-----------------------------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Now, after you finished installation from Installation_Documents_ then do the
following::

    $ python3 --version

    $ pip3 --version

    $ git --version

    $ python3

Run the following import command inside of the python console::

    >> import re

    >> import sys

    >> import subprocess

    >> from datetime import date, datetime

    >> from subprocess import check_output, call

Regex (re), sys, and subprocess module comes with Python installation. Since it is
build-in packages.

If you get any error after running the above import command, you should validate
the Python version or upgrade it. You should not acquire any mistake if you installed
Python correctly or followed all steps from the Installation_Documents_ folder.

There are a couple of essential packages you need to install as well. Please
follow the below steps for that.

Install Psycopg2 :
-----------------------------------
To check if you have Psycopg2 in your computer or not then run the following command::
First type as below to go to Python console::

    $ python3

Then import it::

    >> import psycopg2

If psycopg2 import successfully, then you no need to install it again. But if you get
an error "ImportError: No module named psycopg2" then you need to install it.

Psycopg2 is an extra module that you need to import first to run this code. To
install Psycopg2, please go to the Postgresql_pgAdmin_Installation_ folder. Also,
you can find the same folder inside the Installation_Documents_ folder.

Before running any of this code, please read the documents from
Postgresql_pgAdmin_Installation_ folder. Since you need to create a Database,
Table, etc., and also need to validate it.

.. _Postgresql_pgAdmin_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents/Postgresql_pgAdmin_Installation

Executing :
-------------
If you have done all the steps mentioned above, then please run any of the code as
follow::

    $ python3 Customer_Insert.py

    $ python3 Customer_Search_Main.py

    $ python3 Customer_Search_ID.py

    $ python3 Customer_Search_Name.py

    $ python3 Customer_Update.py

