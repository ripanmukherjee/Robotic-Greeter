#!/bin/ksh

echo "Checking Pip Version before installing!!!"
pip_version="$(pip --version)"
echo "${pip_version}"

echo "                                                                                                             "
echo "Starting Installing Pip!!"
sudo apt update
sudo apt install python3-pip
python3 -m pip install --upgrade pip
echo "Ending Installing Pip!!"

echo "                                                                                                             "
echo "Checking Pip Version after installing!!!"
pip_version="$(pip --version)"
echo "${pip_version}"

echo "                                                                                                             "
echo "Installation Done!!"