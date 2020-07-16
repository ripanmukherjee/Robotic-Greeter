Speech Recognition Code Document:
**********************************
This instruction document is for all the Speech recognition related code, where we have codes that can convert the text into speech or speech into text and codes that can make conversation with users. Here we used gTTS, playsound, NLTK etc. module for speech recognition concepts.

gTTS (Google Text-to-Speech) is a Python library with Google Translate text-to-speech API. This package writes spoken mp3 data to a file, a file-like object for further audio manipulation, or stdout. It features flexible pre-processing and tokenizing, as well as automatic retrieval of supported languages.

Play sound on Python is easy. There are several modules that can play a sound file. These solutions are cross platform (Windows, Mac, Linux). The main difference is in the ease of use and supported file formats. All of them should work with Python 3. The audio file should be in the same directory as your python program unless you specify a path.

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux System.

System Set-Up:
-----------------------------------
There are a couple of Python packages that need to validate before running any above program in this folder. Please go to the Installation_Documents_ folder and follow all the steps.

.. _Installation_Documents: https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Installation_Documents

Pre-Requisites
-----------------------------------
•	A system running on Windows/Ubuntu APP/Ubuntu OS
•	A user account with sudo/administration privileges
•	Access to a terminal window/command-line
•	Internet connection

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo or administration privileges and completed all the necessary steps from the Installation_Documents_ folder.

In this tutorial, we will explain all the Speech Recognition Codes that are written in Python3 on Ubuntu. We have some codes related to Speech Recognition as follows:
1.	Speech_Question.py
2.	Speech_Normal.py
3.	Speech_Name_Organization.py
4.	Speech_Emergency_Evacuation_Procedures.py

Each of the codes in this folder has one function called process_parameter_set(), which contains the different parameter value. Depending on the parameter value, the program will perform other process. Hence it is essential to validate this function and all the parameters before running any codes.

Also, it is crucial to test the microphone index. In this process, we are automatically taking all the microphone devices present into the device_list variable. Later, checking if 'pulse' or 'USB PnP' is present in the device list or not. If that is present, we are assigning the device_index to the index position of 'pulse' or 'USB PnP,' but if that is not present then, we are setting as 0.

For your case, this value (USB details) may change. So, it is better to validate those in python console as below::


    >> device_list = sr.Microphone.list_microphone_names()

    >> print(device_list)



Speech Recognition Code:
-----------------------------------

This folder contains all the Speech Recognition related code written in Python as follow:

1. Speech_Question.py_:
Speech_Question.py is to ask YES or NO related questions to the user. If this program does not get input from users within a given time, it will prompt a pop-up message to click OK or Cancel. This process will be called from Main_Process.py with the question as an argument. Depending on the person's response, this program will write an output file (Speech_Question_Output.txt) as YES or NO or NONE.

Also, you can run this program as a stand-alone program.

2. Speech_Normal.py_:
Speech_Normal.py is a standard speech-related program. It will be called from the Main_Process.py with a text message that Robot needs to speak. This process will not ask anything. It will talk whatever text message it will receive.

Also, you can run this program as a stand-alone program.

3. Speech_Name_Organization.py_:
Speech_Name_Organization.py is to ask the Name & Organization to Unknown Person. Later, it will ask the person if they want to save their details or not. If this program does not get input from users within a given time, then it will prompt a pop-up message to enter the details or to click OK or Cancel. Depending on the person's response, this program will write an output file (Speech_Name_Organization_Output.text) as YES or NO or NONE.

Also, you can run this program as a stand-alone program.

4. Speech_Emergency_Evacuation_Procedures.py_:
Speech_Emergency_Evacuation_Procedures.py program is to show the emergency and evacuation procedure to the users and while showing the image, this program will describe the image by gTTS. All the pictures of emergency and evacuation procedures are present inside Emergency_Evacuation_Procedures folder. Please check def process_parameter_set() function and check the path before executing this process.

Also, you can run this program as a stand-alone program.

.. _Speech_Question.py:             https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Question.py
.. _Speech_Normal.py:               https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Normal.py
.. _Speech_Name_Organization.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Name_Organization.py
.. _Speech_Emergency_Evacuation_Procedures.py: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Speech_Recognition_Code/Speech_Emergency_Evacuation_Procedures.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Speech_Recognition_Code_Document_

.. _Speech_Recognition_Code_Document:

Executing:
-------------
If you have done all the steps mentioned above, please run any of the code::

    $ chmod +x *.py

    $ python3 Speech_Name_Organization.py

    $ python3 Speech_Normal.py

    $ python3 Speech_Question.py

    $ python3 Speech_Emergency_Evacuation_Procedures.py

