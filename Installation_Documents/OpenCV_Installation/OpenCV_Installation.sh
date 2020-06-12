#!/bin/ksh

echo "                            "
echo "Starting Installation OpenCV!!"
sudo apt update
sudo apt install python3-opencv
echo "                                        "
python3 -c "import cv2; print(cv2.__version__)"

sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
    gfortran openexr libatlas-base-dev python3-dev python3-numpy \
    libtbb2 libtbb-dev libdc1394-22-dev

# shellcheck disable=SC2164
mkdir ~/opencv_build && cd ~/opencv_build
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git

# shellcheck disable=SC2164
cd ~/opencv_build/opencv
# shellcheck disable=SC2164
mkdir build && cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..

make -j8
sudo make install
pkg-config --modversion opencv4
echo "Ending Installation OpenCV!!"

echo "                   "
echo "Installation Done!!"
