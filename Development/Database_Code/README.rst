Instruction Documents - README :
**********************************


Database Code :
-----------------------------------

This folder contain all the database related code written in Python as follow :

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
There are couple of python packages which needs to validate before run any above
program in this folder. Assuming that you have already installed python 3.6
(or above), Pip and Git. If not then please go to the Installation_Documents_ and
do the needful first

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents

Prerequisites :
-----------------------------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Now, after you finished Install Python Package step then validate python3, pip &
Git on your computer as following :

Run the following command to go in python console::

    $ python3

Run the following import command inside of the python console::

    >> import re
    >> import sys
    >> import subprocess
    >> import psycopg2

regex(re), sys and subprocess module comes python installation. Since it is
build-in packages.

If you get any error after running the above import command then you should validate
python version or upgrade it. You should not get any error if you installed python
correctly or followed all steps from Installation_Documents_ folder.

There are 2 way you can install the packages:

Install Psycopg2 :
-----------------------------------
Psycopg2 is an extra module that you need to import here to run this code. To
install Psycopg2, please go to the Postgresql_pgAdmin_Installation_ folder.Also,
you can find the same folder inside Installation_Documents_ folder.

Before run any of these code, please read the documents from
Postgresql_pgAdmin_Installation_ folder. Since you need to create Database, Table
etc and also needs to validate it.

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

