#!/bin/ksh

echo "Starting Installing regex........."
pip3 install regex
echo "Ending Installing regex........."

echo "                                                                                                             "
echo "============================================================================================================="
echo "                                                                                                             "

echo "Starting Installing os-sys........."
pip3 install os-sys
echo "Ending Installing os-sys........."
echo "PLEASE IGNORE IF OS-SYS GIVING - ERROR: No matching distribution found for pywin32 (from wmi->os-sys)"

echo "                                                                                                             "
echo "============================================================================================================="
echo "                                                                                                             "

echo "Starting Installing subprocess........."
pip3 install subprocess.run
echo "Ending Installing subprocess........."