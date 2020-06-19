Instruction Documents - README :
**********************************
This instruction document is for all the face recognition related code, where we have codes that can convert the text into speech or speech into text, and also codes that can do conversation with customer.

Note: This project is developed on a Linux System (Ubuntu), so, it is advisable to use Linux for this project.

Speech Recognition Code :
-----------------------------------

This folder contains all the Speech Recognition related code written in Python as follow:

1. Speech_Question.py_:
Speech_Question.py is to ask YES or NO related questions to the customer. If this program does not get an input from customer within given time then it will prompt a pop up message to to click ok or cancel. It will be called from Main_Process.py and Main_Process.py will pass the question as an argument in this program. Depending on the person's response, this program will give an output (inside of a text file : Speech_Question_Output.txt) as YES or NO or NONE. And with thatresponse, Main_Process.py will perform different tasks.

Also, you can run this program as stand alone program.

2. Speech_Normal.py_:
Speech_Normal.py is a standard speech-related program. It will be called from the Main_Process.py with a text message that robots need to speak. This process will not be going to ask anything. It will talk just whatever text message this program will receive.

Also, you can run this program as stand alone program.

3. Speech_Start_End.py_:
Speech_Start_End.py is to greet the Known and Unknown person. It will be called from Main_Process.py with first argument as follow:

* Case when 0 (For Unknown person): It will greet to Unknown Person
* Case when Specific Name (For Known person): It will welcome to known Person
* Case when 1 (For Known & Unknown): It will say Bye

Also, you can run this program as stand alone program.

4. Speech_Name_Organization.py_:
Speech_Name_Organization.py is to ask the Name & Organization to Unknown Person. Later it will ask to the person if they want to save their details or not. If this program does not get an input from customer within given time then it will prompt a pop up message to enter the details or to click ok or cancel. It will be called from ~/Main_Process/Main_Process.py and depending on the person's response this program will give an output (inside of a text file : Speech_Name_Organization_Output.text) as YES or NO or NONE. And with that response Main_Process.py will perform different task.

Also, you can run this program as stand alone program.

.. _Speech_Question.py:             https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Question.py
.. _Speech_Normal.py:               https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Normal.py
.. _Speech_Start_End.py:            https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Start_End.py
.. _Speech_Name_Organization.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Name_Organization.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs then please go to Speech_Recognition_Code_Document_

.. _Speech_Recognition_Code_Document:

System Set Up:
-----------------------------------
There are a couple of Python packages that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites:
-----------------------------------
* A system running on Windows/Ubuntu APP/Ubuntu OS
* A user account with sudo/administration privileges
* Access to a terminal window/command-line

Executing :
-------------
If you have done all the steps mentioned above, please run any of the code::

    $ chmod +x *.py

    $ python3 Speech_Name_Organization.py

    $ python3 Speech_Normal.py

    $ python3 Speech_Question.py

    $ python3 Speech_Start_End.py

