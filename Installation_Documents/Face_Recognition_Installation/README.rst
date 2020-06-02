Install Face Recognition on Ubuntu 18.04
--------------------------------------------
To build our face recognition system, we’ll first perform face detection, extract
face embeddings from each face using deep learning, train a face recognition model
on the embeddings, and then finally recognize faces in both images and video streams
with OpenCV.

In this tutorial, we will show you how to install Face Recognition on Ubuntu 18.04
using the apt package manager. You can find OpenCV installation in other folder.

Prerequisites
--------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Before continuing with this tutorial, make sure you are logged in as root
or a user with sudo privileges.

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

Run the update again and install pip::

    $ pip3 install dlib

    $ pip3 install face_recognition

    $ pip3 install --upgrade imutils

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(Face_Recognition_Installation.sh_) in the Face_Recognition_Installation folder.
By running this program, it will automatically install Face Recognition for you.

.. _Face_Recognition_Installation.sh: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Development/Installation_Documents/Face_Recognition_Installation/Face_Recognition_Installation.sh

Installation done!!

Please visit the Face_Recognition_ (Python Package Index) site for more python packages
details.

.. _Face_Recognition: https://pypi.org/project/face-recognition/