#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Face_Encoding.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  This program is the main program which will create encoding.pickle file, which is essential for
#               Face_Detection_Camera.py & Face_Detection_Image.py. Mainly, for all the application which needs to
#               detect the faces from camera or images.
#
#               First, this program will check if the encoding.pickle file is already present or not in the same
#               folder. If the file exists, then it will read all the old data (old coordinate data) from the encoding
#               file and store it into one variable, later this program will check if any new images present in the
#               Dataset directory or not. If the Dataset directory has any new pictures or old photos, then this
#               program will read those photos and will create coordinate for new images. After creating all the
#               coordinate of all the latest images, this program will merge all the old coordinates with new
#               coordinates and will write into encoding.pickle file.
# **********************************************************************************************************************
# NOTE 1:       This code has one function called process_parameter_set(), which contains the parameter of the Dataset
#               directory. From this directory, this process will validate new images. So, it is essential to look at
#               this function before running this program.
# **********************************************************************************************************************
# NOTE 2:       You need to run separately, since this program will not be going to call from any other program. This
#               program will create encoding file which is essential for any face detection program.
#               This program can be run separately or as a stand-alone program as follow:
#               $ python3 Face_Encoding.py
# **********************************************************************************************************************
"""

import os
import cv2
import sys
import pickle
import face_recognition
from pathlib import Path
from imutils import paths
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
    print('Starting program : Face_Encoding.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending Program : Face_Encoding.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. image_path signifies the folder, where all the new images are stored.
    2. detect_model signifies detection model.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    image_path = 'Dataset'
    detect_model = 'cnn'

    return image_path, detect_model


def process_face_encode(image_path, detect_model):
    """
    ************************************ Inside process_face_encode function *******************************************
    This is the main function which creates encoding file by reading the images.

    This function is the primary function that will first check if the image_path is present or not. If the path does
    not exist, then the program will exit, and if the folder exists, then this function will check if any new images
    present inside of the image_path or not. If there are any new images, this function will create an encoding file,
    and if not, then it will exit the program.
    Also, while creating an encoding file, this function will first check if this file is present or not. If not, then
    this function will create encoding file with new data, but if the data exist then first, it will read all the data
    from encoding.pickle file and load it into old data variable and later will merge old data with new data. and will
    write in the encoding file.
    ************************************ Inside process_face_encode function *******************************************
    """

    args = {'dataset': image_path, 'detection_method': detect_model}

    path = Path(image_path)
    if path.exists() is False:
        print("ERROR : path.exists() is false - Directory : Dataset is not present - "
              "inside process_face_encode function.")
        exit_program()
    else:
        print("Quantifying faces....")
        image_paths = list(paths.list_images(args["dataset"]))

        known_encodings = []
        known_names = []

        for (i, imagePath) in enumerate(image_paths):
            name = imagePath.split(os.path.sep)[-2]
            print("Processing image {}/{} - image data : {}".format(i + 1, len(image_paths), name))
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
            encodings = face_recognition.face_encodings(rgb, boxes)
            for encoding in encodings:
                known_encodings.append(encoding)
                known_names.append(name)

        if len(known_encodings) == 0:
            if len(known_names) == 0:
                print("ERROR : There are no new images in the data set - inside process_face_encode function.")
                exit_program()
            else:
                print("ERROR : There are no encoding created for the images but has name - "
                      "inside process_face_encode function.")
                exit_program()

        else:
            print("Serializing encodings....")
            try:
                with open("encodings.pickle", "rb") as file:
                    print("Reading from old encoding file....")
                    unpickler = pickle.Unpickler(file)
                    old_data = unpickler.load()
                    for old_k, old_v in old_data.items():
                        if old_k == "encodings":
                            old_known_encodings = old_v
                        else:
                            if old_k == "names":
                                old_known_names = old_v

                    new_known_encodings = old_known_encodings + known_encodings
                    new_known_names = old_known_names + known_names
                    print("Writing new data in encoding file....")
                    new_data = {"encodings": new_known_encodings, "names": new_known_names}

                    with open("encodings.pickle", "wb") as pickle_file:
                        pickle_file.write(pickle.dumps(new_data))

            except EOFError:
                print("ERROR : EOFError - Pickle File : encodings.pickle,  has no data - "
                      "inside process_face_encode function.")
                print("Writing new data in encoding file : encodings.pickle....")
                new_data = {"encodings": known_encodings, "names": known_names}
                with open("encodings.pickle", "wb") as pickle_file:
                    pickle_file.write(pickle.dumps(new_data))

            except FileNotFoundError:
                print("encodings.pickle, is not present, Creating encoding file : encodings.pickle....")
                print("Writing new data in encoding file : encodings.pickle....")
                new_data = {"encodings": known_encodings, "names": known_names}
                with open("encodings.pickle", "wb+") as pickle_file:
                    pickle_file.write(pickle.dumps(new_data))


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    image_path, detect_model = process_parameter_set()
    process_face_encode(image_path, detect_model)
    exit_program()


if __name__ == "__main__":
    main()
