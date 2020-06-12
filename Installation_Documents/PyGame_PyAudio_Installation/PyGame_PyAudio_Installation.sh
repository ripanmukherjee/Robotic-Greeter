#!/bin/ksh

echo "                                      "
echo "Starting Installation PyGame & PyAudio!!"
sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
python3 -m pip install -U pygame --user
sudo apt-get install python3-pyaudio

# If apt-get install python3-pyaudio doesn't work then do as below:
# First we need to install port audio modules:
#-------------------------------------------------------------------------
#         $sudo apt-get install libasound-dev
#-------------------------------------------------------------------------
#
# Then You should have one port audio file inside Py_Audio_Installation folder or else you can download the port audio archive from: http://portaudio.com/download.html. But if you prefer to download it then please put the tar file into this folder. Then run the below command:
#-------------------------------------------------------------------------
#         $ tar -zxvf pa_stable_v190600_20161030.tgz
#         $ cd portaudio
#         $ ./configure && make
#-------------------------------------------------------------------------
#
# Then install make and pyaudio as below:
#-------------------------------------------------------------------------
#         $ sudo make install
#         $ sudo pip3 install pyaudio
#-------------------------------------------------------------------------
cho "Ending Installation PyGame & PyAudio!!"

echo "                   "
echo "Installation Done!!"