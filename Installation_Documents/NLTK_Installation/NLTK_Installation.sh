#!/bin/ksh

echo "                          "
echo "Starting Installation NLTK!!"
pip3 install --user -U nltk
python3 -c "import nltk; nltk.download('all')"
pip3 install --user -U numpy
echo "Ending Installation NLTK!!"

echo "                   "
echo "Installation Done!!"