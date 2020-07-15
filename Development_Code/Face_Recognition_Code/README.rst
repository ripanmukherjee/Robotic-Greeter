Instruction Documents:
**********************************
This instruction document is for all the face recognition related code, where we have codes that can take your picture and save it, code for creating face encode from the saved picture, and codes for detecting faces from Camera and Images. In this project we used face_recognition and OpenCV module.
The Face Recognition library is widely known around the web for being the world's simplest facial recognition API for Python and the command line, and the best of all is that you won't need to pay a dime for it, the project is open-source, so if you have some development knowledge and you can build a library from scratch, you will surely know how to work with this library.
OpenCV (Open Source Computer Vision Library) is an open-source computer vision library with bindings for C++, Python, and Java. It is used for a wide range of applications, including medical image analysis, stitching street view images, surveillance video, detecting and recognizing faces, tracking moving objects, extracting 3D models, and much more. OpenCV can take advantage of multi-core processing and features GPU acceleration for real-time operation.
OpenCV-Python is a library of Python bindings designed to solve computer vision problems. OpenCV-Python uses of NumPy, a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from NumPy arrays.
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

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo or administration privileges and completed all the necessary steps from the Installation_Documents_ folder.

In this tutorial, we will explain all the Face Recognition Codes that are written in Python3 on Ubuntu. We have some codes related to Face Recognition as follows:

1.	Capture_Picture_Main.py
2. Capture_Picture_Save.py
3.	Face_Encoding.py
4.	Face_Detection_Camera.py
5.	Face_Detection_Image.py

Some of the codes in this folder has one function called process_parameter_set(), which contains the different parameter value. Depending on the parameter value, the program will perform other process. Hence it is essential to validate this function and all the parameters before running any codes.

Face Recognition Code :
-----------------------------------

This folder contains all the Face Recognition related code written in Python as follow:

1. Capture_Picture_Main.py_:
Capture_Picture_Main.py program will be called from Main_Process.py. It will receive one input argument (Unique ID) from the main process, and based on the input argument, it will call to Capture_Picture_Save.py for taking and saving the picture. This process is a looping process that asks the user if he want to take multiple pictures and save it.

Also, you can run this program as a stand-alone program. In this case, the Unique ID will be 0. The concept of Unique ID in this program is because this process needs to save the user images with the same Unique ID as present in the table. So that next time, if the user comes in front of the Robotic Greeter, it can detect the faces with the Unique ID. And with the same Unique ID, it can search the user details from the table.

2. Capture_Picture_Save.py_:
Capture_Picture_Save.py program will be called from Capture_Picture_Main.py. It will receive the Unique ID from the parent program. It will first take a picture of the person and later it will prompt a pop-up screen where user can enter the name. Now, this program will merge the name with Unique ID and will save it into the Dataset directory.

First, this program will create a new folder inside the Dataset directory (If there are no same folder present) and save the picture inside the newly created folder. If the users wants to take multiple pictures then this program will automatically increase the instance ID (for the first picture, instance ID will be 001)

This program should save the picture into the following directory:
Dataset/XXX_UniqueID/XXX_UniqueID_YYY.jpg (XXX - Person Name, YYY – Instance ID)

This code has one function called process_parameter_set(), which contains the parameter of the Dataset directory. It is essential to check the Dataset directory present before running this program. If the Dataset directory is not present then, please create this directory first.

Also, you can run this program as a stand-alone program.

3. Face_Encoding.py_:
This program is the main program which will create encoding.pickle file, which is essential for Face_Detection_Camera.py & Face_Detection_Image.py. Mainly, for all the application which needs to detect the faces from camera or images.

First, this program will check if the encoding.pickle file is already present or not in the same folder. If the file exists, then it will read all the old data (old coordinate data) from the encoding file and store it into one variable, later this program will check if any new images present in the Dataset directory or not. If the Dataset directory has any new pictures or old photos, then this program will read those photos and will create coordinate for new images. After creating all the coordinate of all the latest images, this program will merge all the old coordinates with new coordinates and will write into encoding.pickle file.

This code has one function called process_parameter_set(), which contains the parameter of the Dataset directory. From this directory, this process will validate new images. So, it is essential to look at this function before running this program.

You need to run separately, since this program will not be going to call from any other program. This program will create encoding file which is essential for any face detection program.

4. Face_Detection_Camera.py_:
This program will be called from Main_Process.py.  It is the primary process of the face detection program from the real-time video camera.

First, this process will read all the coordinates present in the encoding.pickle file (If this file is not present, this program will exit) and store it into one variable (data variable). Later, it will open the video camera automatically and check if any faces are present in the real-time video or not. If it detects any faces in the video, then it will create a coordinate for the faces from the camera.

This process will then check if the newly created coordinate matches with any of the coordinates stored into the data variable. If any matches happen, this program will show the person's name in the video (also, it will create a square box over the face). If not, then it will show as Unknown.

This code has one function called process_parameter_set(), which contains the parameter of encoding_file and face_cascade. It is essential to validate encodings.pickle & haarcascade_frontalface_default.xml files are present in the same folder or not. To create encodings.pickle file, please execute Face_Encoding.py as mentioned in above, and haarcascade_frontalface_default.xml is vital to detect frontal face with OpenCV.

Also, you can run this program as a stand-alone program.

5. Face_Detection_Image.py_:
This program is a testing program of Face_Detection_Camera.py; this process is used to detect the faces from an image. This process works same as above program.

But to run this program, you need to do the follows:

a)	First, take your two pictures from your machine or just download any two images of any person from Google.
b)	Then, put one image into Dataset directory/Image_Name_Directory. (Suppose if image name is ABC then first create a directory inside Dataset directory with name ABC and put the image inside of ABC directory).
c)	Run the Face_Encoding.py (This will create encoding.pickle file with the image coordinate).
d)	Then you can put another image inside of the Sample_Images directory. You can rename the picture as your own choice (But if the image name is ABC in the dataset directory, then do not put the same name here). Then, go to process_parameter_set(), and change the image_path value.
e)	At last, run this program.

.. _Capture_Picture_Main.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Face_Recognition_Code/Capture_Picture_Main.py
.. _Capture_Picture_Save.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Face_Recognition_Code/Capture_Picture_Save.py
.. _Face_Detection_Camera.py:   https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Face_Recognition_Code/Face_Detection_Camera.py
.. _Face_Detection_Image.py:    https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Face_Recognition_Code/Face_Detection_Image.py
.. _Face_Encoding.py:           https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development_Code/Face_Recognition_Code/Face_Encoding.py

Codes Architecture:
-----------------------------------
If you want to read more about the above programs, then please go to Face_Recognition_Code_Document_

.. _Face_Recognition_Code_Document:

Executing:
-------------
If you have done all the steps mentioned above, then first validate two directory as follow::

    $ ~/Face_Recognition_Code/Dataset

    $ ~/Face_Recognition_Code/Sample_Images

If this two directory is not present inside cd ~/Face_Recognition_Code then, please
create it as follow::

    $ mkdir Dataset

    $ mkdir Sample_Images

Now please run any of the code as follow::

    $ chmod +x *.py

    $ python3 Capture_Picture_Main.py

    $ python3 Capture_Picture_Save.py

    $ python3 Face_Detection_Camera.py

    $ python3 Face_Detection_Image.py

    $ python3 Face_Encoding.py

