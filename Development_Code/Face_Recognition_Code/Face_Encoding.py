#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Face_Encoding.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# ----------------------------------------------------------------------------------------------------------------------
# Description:  This program is the main program which will create encoding.pickle file, which is essential for
#               Face_Detection_Camera.py & Face_Detection_Image.py. Mainly, for all the application which needs to
#               detect the faces. First, this program will check if the encoding.pickle file is already present or
#               not in the same folder. If the file exists, then it will read all the old data (old coordinate data)
#               from the encoding file and store it into one variable, later this program will check if any new images
#               present in the Dataset directory or not. If the Dataset directory has any new pictures or old photos,
#               then this program will read those photos and will create a new encoding coordinate. After reading all
#               the latest images, this program will merge all the old coordinates with new coordinates and will write
#               again into encoding.pickle file.
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 1:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Face_Encoding.py
# ----------------------------------------------------------------------------------------------------------------------

import os
import cv2
import sys
import pickle
import face_recognition
from pathlib import Path
from imutils import paths
from datetime import date, datetime


def start_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Face_Encoding.py - at : ' + current_time + ' on : ' + current_date)


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending Program : Face_Encoding.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_face_encode():
    image_path = 'Dataset'
    detect_model = 'cnn'
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
    start_program()
    process_face_encode()
    exit_program()


if __name__ == "__main__":
    main()
