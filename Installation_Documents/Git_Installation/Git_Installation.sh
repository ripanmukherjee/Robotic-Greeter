#!/bin/ksh

echo "Checking Git Version before installing!!!"
git_version="$(git --version)"
echo "${git_version}"
echo "                                                                                                             "
echo "Starting Installing Git!!"
sudo apt update
sudo apt install git
echo "Ending Installing Git!!"

echo "                                                                                                             "
echo "Checking Git Version after installing!!!"
git_version="$(git --version)"
echo "${git_version}"

echo "                                                                                                             "
echo "Installation Done!!"