Install Python Package :
-------------------------
There are couple of python packages which needs to validate before
run any python program in Database_Code folder. Assuming that you have
already installed python 3.6 (or above), Pip and Git. If not then please
go to the following folder and do the needful.

1. Python_Installation_
2. Pip_Installation_
3. Git_Installation_

.. _Python_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents/Python_Installation
.. _Pip_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents/Pip_Installation
.. _Git_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents/Git_Installation

Prerequisites
--------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Now, after you validate python3, pip & Git on your computer then please
continue the following :

Go to the python console by typing following command::

    $ python3

Run the following import command inside of the python console::

    >> import re
    >> import sys
    >> import subprocess

    >> import psycopg2

Although, regex(re), sys and subprocess module comes python installation.
Since it is build-in packages.

If you get any error after running the above import command then you
should install the each package separately. You can install any python
packages using pip or pip3 install "python-package".

There are 2 way you can install the packages:

1. Install using Command Prompt.
2. Install via shell scripts.

1. Install using Command Prompt:
*********************************
Install using pip or pip3::

    $ pip3 install regex
    $ pip3 install os-sys
    $ pip3 install subprocess.run

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(/Database_Python_Packages_Installation.sh) in the Database_Code folder.
By running this program, it will automatically install all the above
mentioned packages for you.

|
|

Install Psycopg2:
------------------
Note : To install Psycopg2, please go to the Postgresql_pgAdmin_Installation_
folder. Also, you can check Postgresql_pgAdmin_Installation.doc for more
information.

.. _Postgresql_pgAdmin_Installation:

Installation done!!

Please visit the PyPi_ (Python Package Index) site for more python packages
details.

.. _PyPi: https://pypi.org/