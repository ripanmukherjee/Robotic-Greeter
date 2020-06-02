Install Speech Recognition on Ubuntu 18.04
------------------------------------------------
Speech recognition, as the name suggests, refers to automatic recognition of human speech.
Speech recognition is one of the most important tasks in the domain of human computer interaction.
If you have ever interacted with Alexa or have ever ordered Siri to complete a task, you have
already experienced the power of speech recognition.

Speech recognition has various applications ranging from automatic transcription of speech data
(like voice mails) to interacting with robots via speech.

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

Then we need to install gTTS(Google Text to Speech) and SpeechRecognition module as follow::

    $ pip3 install gTTS

    $ pip3 install SpeechRecognition

2. Install via shell scripts:
*********************************
On the other hand you can run the shell script
(Speech_Recognition_Installation.sh_) in the Speech_Recognition_Installation folder.
By running this program, it will automatically install SpeechRecognition for you.

.. _Speech_Recognition_Installation.sh: https://github.com/ripanmukherjee/Robotic-Greeter/blob/master/Installation_Documents/Speech_Recognition_Installation/Speech_Recognition_Installation.sh

Installation done!!

Please visit the SpeechRecognition_ website for more python related details.

.. _SpeechRecognition: https://pypi.org/project/SpeechRecognition/