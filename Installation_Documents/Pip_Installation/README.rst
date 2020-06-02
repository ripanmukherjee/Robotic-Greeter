Install Pip on Ubuntu 18.04
-------------------------------
Pip is a package management system that simplifies installation and management of
software packages written in Python such as those found in the Python Package Index
(PyPI). Pip is not installed by default on Ubuntu 18.04, but the installation is
pretty straightforward.

In this tutorial, we will show you how to install Python Pip on Ubuntu 18.04 using
the apt package manager. We will also walk you through the basics of installing and
managing Python packages with pip.

Prerequisites
--------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Before continuing with this tutorial, make sure you are logged in as root
or a user with sudo privileges.

Check your version of pip by entering the following::

    $ pip ––version

There are 2 way you can install the packages:

1. Install using Command Prompt.
2. Install via shell scripts.

1. Install using Command Prompt:
*********************************
First, we need to update and upgrade it::

    $ sudo apt update

    $ sudo apt upgrade

Run the update again and install pip::

    $ sudo apt install python3-pip

    $ python3 -m pip install --upgrade pip

Now, validate again::

    $ pip ––version

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(Pip_Installation.sh_) in the Pip_Installation folder.
By running this program, it will automatically install Pip for you.

.. _Pip_Installation.sh: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Installation_Documents/Pip_Installation/Pip_Installation.sh

Installation done!!

Please visit the PyPi_ (Python Package Index) site for more python packages
details.

.. _PyPi: https://pypi.org/