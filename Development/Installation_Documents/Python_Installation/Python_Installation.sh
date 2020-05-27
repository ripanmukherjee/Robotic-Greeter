#!/bin/ksh

echo "Checking Python Version before installing!!!"
python_version="$(python --version)"
python_version="$(python3 --version)"
echo "${python_version}"
python_version="$(python3.7 --version)"
echo "${python_version}"

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
python_version="$(python --version)"
python_version="$(python3 --version)"
echo "${python_version}"
python_version="$(python3.7 --version)"
echo "${python_version}"

echo "                                                                                                             "
echo "Installation Done!!"