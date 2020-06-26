#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Capture_Picture_Save.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Capture_Picture_Save.py program will be called from Capture_Picture_Main.py. It will receive one input
#               argument (Unique ID) from the main process, and based on the argument, it will first take a picture of
#               the person and later save it into the Dataset directory with the help of Unique ID. This program should
#               save the picture into the following directory :
#               * Dataset/XXX_UniqueID/XXX_UniqueID_YYY.jpg (XXX - Person Name, YYY - Serial number)
# **********************************************************************************************************************
# NOTE 1:       Please check following line of code:
#               cap = cv2.VideoCapture(-1) - If with -1 video stream is not working then you can replace with 0 or 1.
# **********************************************************************************************************************
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Capture_Picture_Save.py
# **********************************************************************************************************************
"""

import os
import cv2
import sys
import time
import subprocess
from pathlib import Path
from imutils.video import FPS
from datetime import date, datetime
from subprocess import check_output


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
    print('Starting program : Capture_Picture_Save.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Capture_Picture_Save.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. dataset_path signifies the folder, where all the new images will be save.
    2. face_cascade signifies OpenCV cascade classifier from haarcascade_frontalface_default.xml file.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    dataset_path = 'Dataset'
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    return dataset_path, face_cascade


def process_get_details():
    """
    ************************************ Inside process_get_details function *******************************************
    This function is to get the name from pop-up message to save the picture.

    This function will be called when the customer takes their pictures. It will prompt a pop-up message where the
    customers will enter their names, so, that the photos will be saved with the name mentioned by the customer.
    ************************************ Inside process_get_details function *******************************************
    """

    details = None
    args_get_details = "zenity --forms --width=500 --height=200 --title='Save picture with a valid name' \
                        --text='Type only the First Name' \
                        --add-entry='First Name'"
    try:
        details = check_output(args_get_details, shell=True)
        details = details.decode().split('|')
        details = details[0].strip()
        details = details.upper()
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details function.")
        exit_program()

    return details


def process_save_picture(details, img, fps, unique_id, dataset_path):
    """
    ************************************ Inside process_save_picture function ******************************************
    It is the primary function where taken photos will be saved with a proper name and inside an appropriate folder.

    It will receive two essential parameters as below:

    1. details which will contain the name of the person (The name which customer will insert)
    2. unique_id is the id which present in the customer table.

    Initially, this will merge this above two-parameter with "_" as "details_unique_id," i.e., "Name_ID."

    Then it will check the dataset_path folder is present or not. If not, then it will directly exit from the program.
    If the dataset_path folder exists, it will check if there are any folder with "Name_ID" is present inside of the
    dataset_path or not.

    If Yes, then it will first count how many files are already present inside of this folder. Then it will add 1 with
    the file count. If the file count is 0, then it will add one on it. But if the file count is X, it will add 1 with
    X. Then, it will add this count after "Name_ID," i.e., "Name_ID_Count.jpg."

    If Not, it will create a new folder as "Name_ID" and then save the image as "Name_ID_1.jpg" Here, the count will
    be one since this is the first image saving in this folder.

    Concept of folder name and image name as follow:

    1. Folder Name - XXX_UniqueID (XXX - Person Name)
    2. Image Name  - XXX_UniqueID_YYY.jpg (YYY - Serial Number, this number will automatically increase if the
    customer wants more than one photo.
    ************************************ Inside process_save_picture function ******************************************
    """

    details = details + '_' + unique_id
    path = Path(dataset_path)
    if path.exists() is False:
        print("ERROR : path.exits() is false - Directory : Dataset is not present - "
              "inside process_save_picture function.")
        exit_program()
    else:
        path = Path(dataset_path+'/'+details)
        if path.exists() is False:
            print("Directory : " + details + ", in Dataset directory is not present. Creating the directory")
            path.mkdir()
            filename = details + '_1.jpg'
            file_path = os.path.join(path, filename)
            cv2.imwrite(file_path, img)
            print("Saving the image with name : ", filename)
            check_output(["zenity", "--info", "--width=400", "--height=200", "--text=Your Picture is saved !!!!"])
            fps.update()
            fps.stop()
            exit_program()
        else:
            print("Directory : " + details + ", in Dataset directory is present")
            dir_list = os.listdir(path)
            file_count = len(dir_list)
            file_count += 1
            filename = details + '_' + str(file_count) + '.jpg'
            file_path = os.path.join(path, filename)
            cv2.imwrite(file_path, img)
            print("Saving the image with name : ", filename)
            check_output(["zenity", "--info", "--width=400", "--height=200", "--text=Your Picture is saved !!!!"])
            fps.update()
            fps.stop()
            exit_program()


def process_picture_taking(unique_id, dataset_path, face_cascade):
    """
    ************************************ Inside process_picture_taking function ****************************************
    It is the function which will open the camera and will take the photo.

    This function is the primary function that will open the camera and will capture the image from the camera. Later,
    it will call process_save_picture function to save the picture.
    ************************************ Inside process_picture_taking function ****************************************
    """

    cap = cv2.VideoCapture(0)
    time.sleep(2.0)
    capture_duration = 3
    start_time = time.time()
    end_time = 0
    fps = FPS().start()

    while cap.isOpened():
        try:
            _, img = cap.read()
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faces = face_cascade.detectMultiScale(rgb, 1.1, 4)

            boxes = [(y, x + w, y + h, x) for (x, y, w, h) in faces]
            names = []

            if int(end_time) - int(start_time) > capture_duration:
                details = process_get_details()
                process_save_picture(details, img, fps, unique_id, dataset_path)

            for ((top, right, bottom, left), name) in zip(boxes, names):
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            cv2.imshow("Image Frame", img)
            end_time = time.time()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            fps.update()
        except cv2.error:
            print("ERROR : cv2.error - for taking photo - inside process_picture_taking function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=I cannot take your picture "
                                                                              "currently. \n\nPlease contact "
                                                                              "Admin"])
            exit_program()

    fps.stop()
    cap.release()


def process_check_input_argument(dataset_path, face_cascade):
    """
    ************************************ Inside process_check_input_argument function **********************************
    This function will decide if this program will run as stand-alone or not.

    It will receive an input argument (Unique ID) from the Main_Process and pass the Unique ID to the main
    process_calling function. If this function does not receive any argument, it will pass "0" as an argument.
    ************************************ Inside process_check_input_argument function **********************************
    """

    try:
        print('Inside Capture_Picture_Save.py - Unique ID is : ', sys.argv[1])
        print('Processing Capture_Picture_Save.py from Capture_Picture_Main.py.')
        unique_id = sys.argv[1]
        process_picture_taking(unique_id, dataset_path, face_cascade)
        exit_program()
    except IndexError:
        print("Processing Capture_Picture_Save.py stand alone")
        unique_id = "0"
        process_picture_taking(unique_id, dataset_path, face_cascade)
        exit_program()


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    dataset_path, face_cascade = process_parameter_set()
    process_check_input_argument(dataset_path, face_cascade)
    exit_program()


if __name__ == "__main__":
    main()
