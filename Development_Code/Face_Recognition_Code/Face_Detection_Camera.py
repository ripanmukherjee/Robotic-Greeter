#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Face_Detection_Camera.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Capture_Picture_Main.py program will be called from Main_Process.py.  It is the main process of the
#               face detection program from real-time video. This process will first capture video from the camera
#               and check if the real-time face's coordinate is present in the encoding.pickle file. If the same
#               coordinate picture details are present in the file, then this program will show the known person's
#               name on the video frame. If not, then it will show as Unknown.
# **********************************************************************************************************************
# NOTE 1:       Please check following line of code:
#               cap = cv2.VideoCapture(-1) - If with -1 video stream is not working then you can replace with 0 or 1.
# **********************************************************************************************************************
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Face_Detection_Camera.py
# **********************************************************************************************************************
"""

import cv2
import sys
import time
import pickle
import face_recognition
from imutils.video import FPS
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
    print('Starting program : Face_Detection_Camera.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Face_Detection_Camera.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. encoding_file signifies the encoding file from where this process extract the known faces co-ordinate.
    2. face_cascade signifies OpenCV cascade classifier from haarcascade_frontalface_default.xml file.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    encoding_file = 'encodings.pickle'
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    return encoding_file, face_cascade


def process_face_detection(encoding_file, face_cascade):
    """
    ************************************ Inside process_face_detection function ****************************************
    This is the main function which will detect the faces from a real time video.

    This function is the primary function that will first load all the data from the encoding file, and later this will
    open the camera and create co-ordinate of each faces in the camera. If any newly created co-ordinate matches
    with the co-ordinate present in the encoding file, then it will create a square box and name of the person over
    the faces on the camera. But if the function can not able to find the encoding file in the directory, then it will
    exit from the program.
    ************************************ Inside process_face_detection function ****************************************
    """

    try:
        with open(encoding_file, "rb") as file:
            unpickler = pickle.Unpickler(file)
            data = unpickler.load()

        # cap = cv2.VideoCapture(-1, cv2.CAP_DSHOW) - For Windows 10 system
        cap = cv2.VideoCapture(-1)
        time.sleep(2.0)
        capture_duration = 3
        start_time = time.time()
        end_time = 0
        name = ""
        fps = FPS().start()

        while cap.isOpened():
            _, img = cap.read()
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faces = face_cascade.detectMultiScale(rgb, 1.1, 4)

            boxes = [(y, x + w, y + h, x) for (x, y, w, h) in faces]
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            if int(end_time) - int(start_time) > capture_duration:
                print(name)
                fps.update()
                fps.stop()
                cap.release()
                cv2.destroyAllWindows()
                exit_program()

            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"], encoding)
                name = "UNKNOWN"
                if True in matches:
                    matched_id = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    for i in matched_id:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)

                names.append(name)

            for ((top, right, bottom, left), name) in zip(boxes, names):
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
                end_time = time.time()
            cv2.imshow("Image Frame", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            fps.update()

        fps.stop()
        cap.release()
        cv2.destroyAllWindows()

    except EOFError:
        print("ERROR : EOFError - Pickle File : encodings.pickle,  has no data - "
              "inside process_face_detection function.")
        exit_program()
    except FileNotFoundError:
        print("ERROR : FileNotFoundError - Pickle File : encodings.pickle,  not present - "
              "inside process_face_detection function.")
        exit_program()


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    encoding_file, face_cascade = process_parameter_set()
    process_face_detection(encoding_file, face_cascade)
    exit_program()


if __name__ == "__main__":
    main()
