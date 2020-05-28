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
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

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

Working with Git & GitHub
****************************
After the installation is done, please go to your terminal and do the
following ::

    $ git config --global user.name "FIRST_NAME LAST_NAME"
    $ git config --global user.email "MY_NAME@example.com"

This is for configuration your name and your email id. Also, you can validate
if git is working or not by following ::

    $ git clone https://myexample.url

By doing git clone, the git folder will automatically download in your
computer. If you change any code or any documents or if you create a new code
or document or if you delete any then please do the following ::

    $ git status (This will show git status, if anything needs to update or not)
    $ git add example_code (After you add or modify)
    $ git rm example_code (after you delete)
    $ git status
    $ git commit -a -m "my_example_comment"

The above process you needs to perform for every time you make changes.

Also, you can pull and push the code to Github by following ::

    $ git pull
    $ git push

Please visit the Git_ website for more Git related details.

.. _Git: https://git-scm.com/