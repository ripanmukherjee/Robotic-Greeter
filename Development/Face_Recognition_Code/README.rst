Instruction Documents - README :
**********************************

Face Recognition Code :
-----------------------------------

This folder contains all the Face Recognition related code written in Python as follow:

1. Capture_Picture_Main.py_:

2. Capture_Picture_Save.py_:

3. Face_Detection_Camera.py_:

4. Face_Detection_Image.py_:

5. Face_Encoding.py_:

.. _Capture_Picture_Main.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Face_Recognition_Code/Capture_Picture_Main.py
.. _Capture_Picture_Save.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Face_Recognition_Code/Capture_Picture_Save.py
.. _Face_Detection_Camera.py:   https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Face_Recognition_Code/Face_Detection_Camera.py
.. _Face_Detection_Image.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Face_Recognition_Code/Face_Detection_Image.py
.. _Face_Encoding.py:           https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Face_Recognition_Code/Face_Encoding.py

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
    >> import time
    >> import pickle
    >> import subprocess
    >> from pathlib import Path
    >> from subprocess import check_output
    >> from datetime import date, datetime

os, sys, time, pickle, subprocess, pathlib & datetime module comes Python installation.
Since it is build-in packages.

If you get any error after running the above import command, you should validate
the Python version or upgrade it. You should not acquire any mistake if you installed
Python correctly or followed all steps from the Installation_Documents_ folder.

Install OpenCV :
-----------------------------------
To check if you have OpenCV in your computer or not then run the following command.
First type as below to go to Python console::

    $ python3

Then import it::

    >> import cv2

OpenCV is an extra module that you need to import here to run this code. To
install OpenCV, please go to the OpenCV_Installation_ folder. Also,
you can find the same folder inside the Installation_Documents_ folder.

Before running any of this code, please read the documents from
OpenCV_Installation_ folder.

.. _OpenCV_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents/OpenCV_Installation

Install Face Recognition :
-----------------------------------
To check if you have Face Recognition in your computer or not then run the following
command. First type as below to go to Python console::

    $ python3

Then import it::

    >> import face_recognition

    >> from imutils.video import FPS

Face Recognition is an extra module that you need to import here to run this code. To
install Face Recognition, please go to the Face_Recognition_Installation_ folder. Also,
you can find the same folder inside the Face_Recognition_Installation_ folder.

Before running any of this code, please read the documents from
Face_Recognition_Installation_ folder.

.. _Face_Recognition_Installation: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development/Installation_Documents/Face_Recognition_Installation

Executing :
-------------
If you done all the above mentioned steps then please run any of the code as
follow ::

    $ python3 Capture_Picture_Main.py

    $ python3 Capture_Picture_Save.py

    $ python3 Face_Detection_Camera.py

    $ python3 Face_Detection_Image.py

    $ python3 Face_Encoding.py

