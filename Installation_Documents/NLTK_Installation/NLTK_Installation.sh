#!/bin/ksh

echo "Starting Installing NLTK!!"
pip3 install --user -U nltk
python3 -c "import nltk; nltk.download('all')"
pip3 install --user -U numpy
echo "Ending Installing NLTK!!"

echo "                                                                                                             "
echo "Installation Done!!"