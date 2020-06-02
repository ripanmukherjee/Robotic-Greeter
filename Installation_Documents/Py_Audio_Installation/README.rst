Install pyGame and pyAudio on Ubuntu 18.04
------------------------------------------------
pygame is a Python wrapper for the SDL library, which stands for Simple DirectMedia Layer.
SDL provides cross-platform access to your system’s underlying multimedia hardware components,
such as sound, video, mouse, keyboard, and joystick. pygame started life as a replacement for
the stalled PySDL project. The cross-platform nature of both SDL and pygame means you can write
games and rich multimedia Python programs for every platform that supports them!

pyaudio provides bindings for PortAudio, the cross-platform audio I/O library. This means that
you can use pyaudio to play and record audio on a variety of platforms, including Windows,
Linux, and Mac. With pyaudio, playing audio is done by writing to a .Stream:

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

Then we need to install pygame and pyaudio as follow:

To install pygame run the following command::

    $ python3 -m pip install -U pygame --user

To install pyaudio please follow the steps:

* First we need to install port audio modules::

    $ sudo apt-get install libasound-dev

* You should have one port audio file inside Py_Audio_Installation folder or else you can download the port audio archive from: http://portaudio.com/download.html. But if you prefer to download it then please put the tar file into this folder. Then run the below command::

    $ tar -zxvf pa_stable_v190600_20161030.tgz

* Enter the directory, then run::

    $ cd portaudio

    $ ./configure && make

* Install make and pyaudio finally::

    $ sudo make install
    $ sudo pip3 install pyaudio

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(Py_Audio_Installation.sh_) in the Python_Installation folder.
By running this program, it will automatically install python for you.

.. _Py_Audio_Installation.sh: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Installation_Documents/Py_Audio_Installation/Py_Audio_Installation.sh

Installation done!!

Please visit the pygame_ & pyaudio_ website for more python related details.

.. _pygame: https://www.pygame.org/wiki/GettingStarted
.. _pyaudio: https://people.csail.mit.edu/hubert/pyaudio/