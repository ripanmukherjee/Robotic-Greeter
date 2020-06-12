#!/bin/ksh

echo "                         "
echo "Starting Installation Pip!!"
sudo apt update
sudo apt install python3-pip
python3 -m pip install --upgrade pip
echo "Ending Installation Pip!!"

echo "                   "
echo "Installation Done!!"