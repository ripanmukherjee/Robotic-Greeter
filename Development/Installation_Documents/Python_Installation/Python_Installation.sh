#!/bin/ksh

echo "Checking Python Version before installing!!!"
python -c 'import sys; print(sys.version_info[:])'
python3 -c 'import sys; print(sys.version_info[:])'
python3.7 -c 'import sys; print(sys.version_info[:])'

echo "                                                                                                             "
echo "Starting Installing Python!!"
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python
sudo apt install python3
sudo apt install python3.7
echo "Ending Installing Python!!"

echo "                                                                                                             "
echo "Checking Python Version after installing!!!"
python -c 'import sys; print(sys.version_info[:])'
python3 -c 'import sys; print(sys.version_info[:])'
python3.7 -c 'import sys; print(sys.version_info[:])'

echo "                                                                                                             "
echo "Installation Done!!"