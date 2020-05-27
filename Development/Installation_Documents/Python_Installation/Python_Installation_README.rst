Install Python 3.6 (or above)
-------------------------------
Python is a popular programming language often used to write scripts for
operating systems. It’s versatile enough for use in web development and
app design. In this project we have used python and hence we need to install
and verify it.

Prerequisites
--------------
A system running Ubuntu 18.04
A user account with sudo privileges
Access to a terminal window/command-line (Ctrl–Alt–T)

This process uses the apt package manager to install Python. There are
fewer steps, but it’s dependent on a third party hosting software updates.
You may not see new releases as quickly on a third-party repository.

Most factory versions of Ubuntu 18.04 come with Python pre-installed.
Check your version of Python by entering the following::

    $ python ––version
    $ python3 ––version
    $ python3.7 ––version

There are 2 way you can install the packages:

1. Install using Command Prompt.
2. Install via shell scripts.

1. Install using Command Prompt:
*********************************
First, we need to update and upgrade it. Go to the python console by
typing following command::

    $ sudo apt update
    $ sudo apt upgrade

The software-properties-common package gives you better control over your
package manager by letting you add PPA (Personal Package Archive)
repositories. Install the supporting software with the command::

    $ sudo apt install software-properties-common
    $ sudo add-apt-repository ppa:deadsnakes/ppa

Run the update again and install python::

    $ sudo apt update
    $ sudo apt install python
    $ sudo apt install python3
    $ sudo apt install python3.7

Now, validate again::

    $ python ––version
    $ python3 ––version
    $ python3.7 ––version

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(/Python_Installation.sh) in the Python_Installation folder.
By running this program, it will automatically install python for you.

Installation done!!

Please visit the PyPi_ (Python Package Index) site for more python packages
details.

.. _PyPi: https://pypi.org/