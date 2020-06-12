#!/bin/ksh

echo "                            "
echo "Starting Installation Python!!"
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python
sudo apt install python3
sudo apt install python3.7
echo "Ending Installation Python!!"

echo "                   "
echo "Installation Done!!"