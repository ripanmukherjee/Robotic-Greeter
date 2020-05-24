Python Package :
----------------
There are couple of python packages which needs to validate before
run any program in this folder. Assuming that you have already
installed python 3.6 (or above).

Now, go to the python console by typing following command::

    $ python3

Run the following import command inside of the python console::

    >> import re
    >> import sys
    >> import psycopg2
    >> import subprocess

If you get any error after running the above import command then you
should install the each package separately. You can install any python
packages using pip or pip3 install "python-package".

Note : Regarding psycopg2, please make sure you have already install
psycopg2. If not then please follow the psycopg2_README.md document
first for more details or you can just install as follow.

Install regex, sys, subprocess module :
---------------------------------------
Install using pip or pip3::

    $ pip install regex
    $ pip install os-sys
    $ pip install subprocess.run

Install Psycopg2 by Python pip :
--------------------------------
First of all you need Python3 version pip::

    $ sudo apt-get install python3-pip

This will install the Python3 version of pip command: pip3.
Then you can install Psycopg2 using pip3::

    $ sudo pip3 install Psycopg2

Installation done!

Please visit the PyPi_ (Python Package Index) site for more details.

.. _PyPi: https://pypi.org/