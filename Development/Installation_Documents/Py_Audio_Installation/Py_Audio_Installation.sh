#!/bin/ksh

echo "Starting Installing Pyaudio Pygame!!"
python3 -m pip install -U pygame --user
sudo apt-get install libasound-dev
tar -zxvf pa_stable_v190600_20161030.tgz
cd portaudio
./configure && make
sudo make install
sudo pip3 install pyaudio
cho "Ending Installing Face Recognition!!"

echo "                                                                                                             "
echo "Installation Done!!"