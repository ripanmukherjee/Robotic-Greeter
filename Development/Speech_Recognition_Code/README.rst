Instruction Documents - README :
**********************************

Speech Recognition Code :
-----------------------------------

This folder contains all the Speech Recognition related code written in Python as
follow:

1. Speech_Question.py_:

2. Speech_Normal.py_:

3. Speech_Start_End.py_:

4. Speech_Name_Organization.py_:

.. _Speech_Question.py:
.. _Speech_Normal.py:
.. _Speech_Start_End.py:
.. _Speech_Name_Organization.py:

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

Run the following import command inside of the Python console::

    >> import os

    >> import sys

    >> import glob

    >> from datetime import date, datetime

Os, sys, glob & datetime module comes with Python installation. Since it is
build-in packages.

If you get an error after running the above import command, you should validate
the Python version or upgrade it. You should not acquire any mistake if you installed
Python correctly or followed all steps from the Installation_Documents_ folder.

There are a couple of essential packages you need to install as well. Please
follow the below steps for that.

Install SpeechRecognition :
-----------------------------------
To check if you have SpeechRecognition in your computer or not then run the following
command. First type as below to go to Python console::

    $ python3

Then import it::

    >> import gtts

    >> from gtts import gTTS

    >> import speech_recognition

If gtts and speech_recognition import successfully, then you no need to install it
again. But if you get an error "ImportError: No module named gtts" or
"ImportError: No module named speech_recognition," then you need to install it.

Speech_recognition and gtts is an extra module that you need to import first to
run this code. To install it, please go to the Speech_recognition_Installation_
folder. Also, you can find the same folder inside the Installation_Documents_ folder.

Before running any of this code, please read the documents (README) from
Speech_recognition_Installation_ folder.

.. _Speech_recognition_Installation:

Install NLTK :
-----------------------------------
To check if you have NLTK in your computer or not then run the following
command. First type as below to go to Python console::

    $ python3

Then import it::

    >> import nltk

    >> from nltk.corpus import stopwords

    >> from nltk.tokenize import word_tokenize

If nltk import successfully, then you no need to install it again. But if you get an
error "ImportError: No module named nltk"  or any others, then you need to install it.

NLTK is an extra module that you need to import first to run this code. To
install it, please go to the NLTK_Installation_ folder. Also,
you can find the same folder inside the Installation_Documents_ folder.

Before running any of this code, please read the documents (README) from
NLTK_Installation_ folder.

.. _NLTK_Installation:

Install pygame & pyaudio :
-----------------------------------
To check if you have pygame & pyaudio in your computer or not then run the following
command. First type as below to go to Python console::

    $ python3

Then import it::

    >> import pygame

    >> import pyaudio

If pygame & pyaudio import successfully, then you no need to install it again. But
if you get an error "ImportError: No module named pygame" or
"ImportError: No module named pyaudio" or any others, then you need to install it.

pygame & pyaudio is an extra module that you need to import here to run this code. To
install it, please go to the Py_Audio_Installation_ folder. Also,
you can find the same folder inside the Installation_Documents_ folder.

Before running any of this code, please read the documents (README) from
Py_Audio_Installation_ folder.

.. _Py_Audio_Installation:

Executing :
-------------
If you have done all the steps mentioned above, please run any of the code::

    $ python3 Speech_Name_Organization.py

    $ python3 Speech_Normal.py

    $ python3 Speech_Question.py

    $ python3 Speech_Start_End.py

