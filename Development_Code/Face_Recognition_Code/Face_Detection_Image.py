#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Face_Detection_Image.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Capture_Picture_Main.py program is a testing program of Face_Detection_Camera.py; this process is used
#               to detect the faces from an image. First, you need to load the image into the following line present
#               in code: image_path = 'Sample_Images/image1.jpg'.
#
#               Sample_Images is the directory you need to put your sample image and then need to run the program.
#               This process will also detect the image coordinate and check if it is present in the
#               encoding.pickle file. If the same coordinate picture details are current in the archive, this program
#               will show the known person's name on the video frame. If not, then it will show as Unknown.
#
#               But to run this program, you need to validate the follows:
#
#               * First, put your sample image into Dataset directory/Image_Name_Directory.
#               (Suppose if your name is ABC then first create a directory inside Dataset directory
#               with name ABC and put your image inside of it).
#               * Run the Face_Encoding.py (This will create encoding.pickle file with the image coordinate).
#               * Then you can put another sample image of you inside of the Sample_Images directory.
#               * At last, run this program as stand-alone.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow:
#           	$ python3 Face_Detection_Image.py
# **********************************************************************************************************************
"""

import sys
import cv2
import pickle
import face_recognition
from datetime import date, datetime


def start_program():
    """
    ************************************ Inside start_program function *************************************************
    This function will be called at the beginning to print today's date and start time.
    ************************************ Inside start_program function *************************************************
    """

    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Face_Detection_Image.py - at : ' + current_time + ' on : ' + current_date)


def exit_program():
    """
    ************************************ Inside exit_program function **************************************************
    This function will be called at the end to print today's date and end time.
    ************************************ Inside exit_program function **************************************************
    """

    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Face_Detection_Image.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. encoding_file signifies the encoding file from where this process extract the known faces co-ordinate.
    2. image_path signifies the folder, where all the new images are stored.
    3. detect_model signifies detection model.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    encoding_file = 'encodings.pickle'
    image_path = 'Sample_Images/image1.jpg'
    detect_model = 'cnn'

    return encoding_file, image_path, detect_model


def process_face_detection_image(encoding_file, image_path, detect_model):
    """
    ************************************ Inside process_face_detection_image function **********************************
    This is the main function which will detect the faces from a image.

    This function is the primary function that will first read all the data from the encoding file, and later this will
    open the input image and create co-ordinate of each faces in the picture. If any newly created co-ordinate matches
    with the co-ordinate present in the encoding file, then it will create a square box with name of the person over
    the faces on the image. But if the function can not able to find the encoding file in the directory, then it will
    exit from the program.
    ************************************ Inside process_face_detection_image function **********************************
    """

    try:
        args = {'encodings': encoding_file, 'image': image_path, 'detection_method': detect_model}

        data = pickle.loads(open(args["encodings"], "rb").read())
        image = cv2.imread(args["image"])
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        for encoding in encodings:

            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"
            if True in matches:
                matched_id = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matched_id:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)

            names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow("Image", image)
        cv2.waitKey(0)
    except EOFError:
        print("ERROR : EOFError - Pickle File : encodings.pickle,  has no data - "
              "inside process_face_detection_image function.")
        exit_program()
    except FileNotFoundError:
        print("ERROR : FileNotFoundError - Pickle File : encodings.pickle, not present in the directory "
              "- inside process_face_detection_image function.")
        exit_program()


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    encoding_file, image_path, detect_model = process_parameter_set()
    process_face_detection_image(encoding_file, image_path, detect_model)
    exit_program()


if __name__ == "__main__":
    main()
