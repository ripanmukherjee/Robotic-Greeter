Instruction Documents:
**********************************
This instruction document is for all the Speech recognition related code, where we have codes that can convert the text into speech or speech into text and codes that can make conversation with customers.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux for this project.

Speech Recognition Code:
-----------------------------------

This folder contains all the Speech Recognition related code written in Python as follow:

1. Speech_Question.py_:
Speech_Question.py is to ask YES or NO related questions to the customer. If this program does not get input from customers within a given time, it will prompt a pop-up message to click ok or cancel. It will be called from Main_Process.py and Main_Process.py will pass the question as an argument in this program. Depending on the person's response, this program will give an output (inside of a text file: Speech_Question_Output.txt) as YES or NO or NONE. And with that response, Main_Process.py will perform different tasks.

Also, you can run this program as a stand-alone program.

2. Speech_Normal.py_:
Speech_Normal.py is a standard speech-related program. It will be called from the Main_Process.py with a text message that robots need to speak. This process will not be going to ask anything. It will talk just whatever text message this program will receive.

Also, you can run this program as a stand-alone program.

3. Speech_Name_Organization.py_:
Speech_Name_Organization.py is to ask the Name & Organization to Unknown Person. Later it will ask the person if they want to save their details or not. If this program does not get input from customers within a given time, then it will prompt a pop-up message to enter the details or to click ok or cancel. It will be called from ~/Main_Process/Main_Process.py, and depending on the person's response, this program will give an output (inside of a text file: Speech_Name_Organization_Output.text) as YES or NO or NONE. And with that response, Main_Process.py will perform different task.

Also, you can run this program as a stand-alone program.

4. Speech_Emergency_Evacuation_Procedures.py_:
Speech_Emergency_Evacuation_Procedures.py program is to show the emergency and evacuation procedure and while showing the image, this program will describe the image by gTTS. All the pictures of emergency and evacuation procedures are present inside Emergency_Evacuation_Procedures folder. Please check def process_parameter_set() function and check the path before executing this process.

Also, you can run this program as a stand-alone program.

.. _Speech_Question.py:             https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Question.py
.. _Speech_Normal.py:               https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Normal.py
.. _Speech_Name_Organization.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Name_Organization.py
.. _Speech_Emergency_Evacuation_Procedures.py: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Emergency_Evacuation_Procedures.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Speech_Recognition_Code_Document_

.. _Speech_Recognition_Code_Document:

System Set-Up:
-----------------------------------
There are a couple of Python packages that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites:
-----------------------------------
* A system running on Windows/Ubuntu APP/Ubuntu OS
* A user account with sudo/administration privileges
* Access to a terminal window/command-line

Executing:
-------------
If you have done all the steps mentioned above, please run any of the code::

    $ chmod +x *.py

    $ python3 Speech_Name_Organization.py

    $ python3 Speech_Normal.py

    $ python3 Speech_Question.py

    $ python3 Speech_Start_End.py

