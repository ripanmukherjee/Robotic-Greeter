Install Speech Recognition on Ubuntu 18.04
------------------------------------------------
The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for
symbolic and statistical natural language processing (NLP) for English written in the
Python programming language.

Prerequisites
--------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo
privileges.

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

Then we need to install NLTK module as follow::

    $ pip3 install --user -U nltk

    $ pip3 install --user -U numpy

Then we need to download nltk data as follow::

    $ python3 -c "import nltk; nltk.download('all')"

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script NLTK_Installation.sh_ in the NLTK_Installation
folder. By running this program, it will automatically install NLTK for you.

.. _NLTK_Installation.sh: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Installation_Documents/NLTK_Installation/NLTK_Installation.sh

You can run the shell script as follow::

    $ chmod +x *.sh

    $ sh NLTK_Installation.sh

Installation done!!

Please visit the NLTK_ website for more Natural Language Toolkit related details.

.. _NLTK: https://www.nltk.org/data.html