Install Git on Ubuntu 18.04
-------------------------------
Git is a version control systems and is used by the majority of developers
nowadays. It allows you to keep track of your code changes, revert to
previous stages, create branches, and to collaborate with your fellow
developers.

Git is originally developed by Linus Torvalds, the creator of the Linux
kernel.

This tutorial will guide you through the steps required to install Git on
Ubuntu 18.04. The same instructions apply for Ubuntu 16.04 and any other
Ubuntu-based distribution, Linux Mint and Elementary OS.

Prerequisites
--------------
A system running Ubuntu 18.04
A user account with sudo privileges
Access to a terminal window/command-line (Ctrl+Alt+T)

Before continuing with this tutorial, make sure you are logged in as root
or a user with sudo privileges.

Check your version of Git by entering the following::

    $ git ––version

There are 2 way you can install the packages:

1. Install using Command Prompt.
2. Install via shell scripts.

1. Install using Command Prompt:
*********************************
First, we need to update and upgrade it::

    $ sudo apt update
    $ sudo apt upgrade

Run the update again and install Git::

    $ sudo apt install git

Now, validate again::

    $ git ––version

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(/Git_Installation.sh) in the Git_Installation folder.
By running this program, it will automatically install Git for you.

Installation done!!

Please visit the PyPi_ (Python Package Index) site for more python packages
details.

.. _PyPi: https://pypi.org/