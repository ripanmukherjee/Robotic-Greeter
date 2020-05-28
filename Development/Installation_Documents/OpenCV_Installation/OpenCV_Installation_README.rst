OpenCV on Ubuntu 18.04 & Raspberry Pi
************************************************
OpenCV (Open Source Computer Vision Library) is an open-source computer
vision library and has bindings for C++, Python, and Java. It is used for
a very wide range of applications, including medical image analysis,
stitching street view images, surveillance video, detecting and recognizing
faces, tracking moving objects, extracting 3D models, and much more.
OpenCV can take advantage of multi-core processing and features GPU
acceleration for real-time operation.

There are 3 way you can install the packages:

1. Install OpenCV from the Ubuntu Repository.
2. Install OpenCV from the Source.
3. Install OpenCV from the script.

1. Install OpenCV from the Ubuntu Repository
************************************************
The OpenCV package is available from the Ubuntu 18.04 distribution repository.
At the time of writing, the version in the repositories is 3.2, which is not
the latest version. To install OpenCV from the Ubuntu 18.04 repositories,
follow these steps:

* Refresh the packages index and install the OpenCV package by typing::

    $ sudo apt update
    $ sudo apt install python3-opencv

* To verify the installation, import the cv2 module and print the OpenCV
version::

    $ python3 -c "import cv2; print(cv2.__version__)"

2. Installing OpenCV from the Source
************************************************
Building the OpenCV library from source is the recommended way of installing
OpenCV. It will be optimized for your particular system and you will have
complete control over the build options. To install the latest OpenCV
version from the source, perform the following steps:

* Install the required dependencies::

    $ sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
        libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
        libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
        gfortran openexr libatlas-base-dev python3-dev python3-numpy \
        libtbb2 libtbb-dev libdc1394-22-dev

* Clone the OpenCV’s and OpenCV contrib repositories::

    $ mkdir ~/opencv_build && cd ~/opencv_build
    $ git clone https://github.com/opencv/opencv.git
    $ git clone https://github.com/opencv/opencv_contrib.git

At the time of writing, the default version in the github repositories is
version 4.2.0. If you want to install an older version of OpenCV, cd to
both opencv and opencv_contrib directories and run git checkout.

* Now changed the directory after download is done::

    $ cd ~/opencv_build/opencv
    $ mkdir build && cd build

* Set up the OpenCV build with CMake::

    $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_C_EXAMPLES=ON \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D OPENCV_GENERATE_PKGCONFIG=ON \
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
        -D BUILD_EXAMPLES=ON ..

* Start the compilation process::

    $ make -j8

* Install OpenCV with::

    $ sudo make install

* Now verify the OpenCV version::

    $ pkg-config --modversion opencv4
    $ python3 -c "import cv2; print(cv2.__version__)"


3. Installing OpenCV from the Shell Scripts
************************************************
On the other hand you can run the shell script
(/OpenCV_Installation.sh) in the OpenCV_Installation folder.
By running this program, it will automatically install OpenCV for you.

Installation done!!

Please visit the OpenCV_ website for more OpenCV related details.

.. _OpenCV: https://opencv.org/