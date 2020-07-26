Development Code:
-----------------------------------
Robotic-Greeter is a humanoid Robot, which has AI capabilities such as Face Recognition, Voice Recognition & interact with human.

This folder contains all the codes written in Python as follow :

Note: This project is developed on a Linux System (Ubuntu), so it is advisable to use Linux System.

1. Database_Code_:
This folder contains all the database related code, where we have codes for inserting data into the database, search the data from database based on ID or Name and, codes for update the details on the database. In this project, we are using PostgreSQL Database.

PostgreSQL is a powerful, open-source object-relational database system with over 30 years of active development that has earned a strong reputation for reliability, feature robustness, and performance. PostgreSQL is available in all Ubuntu versions by default. However, Ubuntu "snapshots" a specific version of PostgreSQL that is supported throughout the lifetime of that Ubuntu version. Other versions of PostgreSQL are available through the PostgreSQL apt repository. You can also download and install it on Windows 10.

2. Face_Recognition_Code_:
This folder contains all the face recognition related code, where we have codes that can take your picture and save it, code for creating face encode from the saved picture, and codes for detecting faces from Camera and Images. In this project we used face_recognition and OpenCV module.

The Face Recognition library is widely known around the web for being the world's simplest facial recognition API for Python and the command line, and the best of all is that you won't need to pay a dime for it, the project is open-source, so if you have some development knowledge and you can build a library from scratch, you will surely know how to work with this library.

OpenCV (Open Source Computer Vision Library) is an open-source computer vision library with bindings for C++, Python, and Java. It is used for a wide range of applications, including medical image analysis, stitching street view images, surveillance video, detecting and recognizing faces, tracking moving objects, extracting 3D models, and much more. OpenCV can take advantage of multi-core processing and features GPU acceleration for real-time operation.

OpenCV-Python is a library of Python bindings designed to solve computer vision problems. OpenCV-Python uses of NumPy, a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from NumPy arrays.

3. Speech_Recognition_Code_:
This folder contains all the Speech recognition related code, where we have codes that can convert the text into speech or speech into text and codes that can make conversation with users. Here we used gTTS, playsound, NLTK etc. module for speech recognition concepts.

gTTS (Google Text-to-Speech) is a Python library with Google Translate text-to-speech API. This package writes spoken mp3 data to a file, a file-like object for further audio manipulation, or stdout. It features flexible pre-processing and tokenizing, as well as automatic retrieval of supported languages.

Play sound on Python is easy. There are several modules that can play a sound file. These solutions are cross platform (Windows, Mac, Linux). The main difference is in the ease of use and supported file formats. All of them should work with Python 3. The audio file should be in the same directory as your python program unless you specify a path.

The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical Natural Language Processing (NLP) for English written in the Python programming language.

4. Main_Process_:
This instruction document is for the Main Process, which the parent process for this project. Main_Process.py is the process which is the combination of all individual process. Main Process will first call the Face Recognition process to identify the person. It will call Database-related code for register new users, modify user data, search user data, and in every step, this process will call Speech Recognition.

Also, this folder contains Python program for generating reports.

5. Web_Application_:
This folder contains all the Web Application related code, where we have codes that needs to run before to access Web Application. Also, this folder contains different HTML5 + CSS3 codes for Web Pages. In this project, we have used the Python Flask API module.

Flask is a web framework. This means Flask provides you with tools, libraries, and technologies to build a web application. This web application can be some web pages, a blog, a wiki, or go as big as a web-based calendar application or a commercial website.

Flask is part of the categories of the micro-framework. Micro-framework is usually a framework with little to no dependencies on external libraries. This has pros and cons. The advantage would be that the frame is light. There is a low dependency to update and watch for security bugs; a disadvantage is that sometimes you will have to do more work by yourself or increase yourself the list of dependencies by adding plugins.

.. _Database_Code:            https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development_Code/Database_Code
.. _Face_Recognition_Code:    https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development_Code/Face_Recognition_Code
.. _Speech_Recognition_Code:  https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development_Code/Speech_Recognition_Code
.. _Main_Process:             https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development_Code/Main_Process
.. _Web_Application:          https://github.com/ripanmukherjee/Robotic-Greeter/tree/master/Development_Code/Web_Application_Code
