#!/usr/bin/env python3

# Project : Robotic Greeter - CareGo Tek
# Program Name : Capture_Picture_Save.py
# Author : Somak Mukherjee
# Date : Friday 24 April, 2020
# Version : 1
# Description: Capture_Picture_Save.py program will be called from ~/Face_Recognition_Code/Capture_Picture_Main.py.
#              It will receive one input argument (Unique ID) from the main process, and based on the argument,
#              it will first take a picture of the person and later save it into Dataset directory with
#              the help of Unique ID. This program should save the picture into the following directory :
#              ~/Face_Recognition_Code/Dataset/XX_UniqueID/XX_UniqueID_Y.jpg (XX - Person Name, Y - Instance)
#
# NOTE: This program can be run separately or as a stand-alone program as follow:
# >> python3 Capture_Picture_Save.py

import os
import cv2
import sys
import time
import subprocess
from pathlib import Path
from imutils.video import FPS
from datetime import date, datetime
from subprocess import check_output


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Capture_Picture_Save.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def get_details():
    details = None
    args_get_details = "zenity --forms --width=500 --height=200 --title='Save picture with a valid name' \
                        --text='Type only the First Name' \
                        --add-entry='First Name' 2>/dev/null"
    try:
        details = check_output(args_get_details, shell=True)
        details = details.decode().split('|')
        details = details[0].strip()
        details = details.upper()
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside get_details function.")
        exit_program()

    return details


def save_picture(details, img, fps, unique_id):
    details = details + '_' + unique_id
    dataset_path = 'Dataset'
    path = Path(dataset_path)
    if path.exists() is False:
        print("ERROR : path.exits() is false - Directory : Dataset is not present - inside save_picture function.")
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
            fps.update()
            fps.stop()
            exit_program()


def picture_taking(unique_id):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(-1)
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
                details = get_details()
                save_picture(details, img, fps, unique_id)

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
            print("ERROR : cv2.error - for taking photo - inside picture_taking function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=We cannot take your picture "
                                                                              "currently. \n\nPlease contact "
                                                                              "Admin"])
            exit_program()

    fps.stop()
    cap.release()


def main():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Capture_Picture_Save.py - at : ' + current_time + ' on : ' + current_date)

    try:
        print('Processing Capture_Picture_Save.py from main process.')
        print('Inside Capture_Picture_Save.py - Unique ID is : ', sys.argv[1])
        unique_id = sys.argv[1]
        picture_taking(unique_id)
        exit_program()
    except IndexError:
        print("Processing Capture_Picture_Save.py stand alone")
        unique_id = "0"
        picture_taking(unique_id)
        exit_program()

    exit_program()


if __name__ == "__main__":
    main()
