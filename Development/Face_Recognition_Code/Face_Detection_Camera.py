#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Capture_Picture_Main.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Capture_Picture_Main.py program will be called from Main_Process.py (~/Main_Process/Main_Process.py)
#               It is the main process of face detection program from real-time video. This process will first
#               capture video from camera and check if the real-time face's coordinate is present
#               in encoding.pickle file (~/Face_Recognition_Code/encoding.pickle). If the same coordinate
#               picture details are present in the file, then this program will show the known person's name on
#               the video frame. If not, then it will show as Unknown.
#
# NOTE:         This program can be run separately or as a stand-alone program as follow:
#               >> python3 Face_Detection_Camera.py

import cv2
import sys
import time
import pickle
import face_recognition
from imutils.video import FPS
from datetime import date, datetime


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Face_Detection_Camera.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def face_detection():
    try:
        with open("encodings.pickle", "rb") as file:
            unpickler = pickle.Unpickler(file)
            data = unpickler.load()

        face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(-1)
        time.sleep(2.0)
        capture_duration = 3
        start_time = time.time()
        end_time = 0
        name = ""
        fps = FPS().start()

        while cap.isOpened():
            _, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faces = face_casecade.detectMultiScale(rgb, 1.1, 4)

            boxes = [(y, x + w, y + h, x) for (x, y, w, h) in faces]
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            if int(end_time) - int(start_time) > capture_duration:
                print(name)
                fps.update()
                fps.stop()
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

    except EOFError:
        print("ERROR : EOFError - Pickle File : encodings.pickle,  has no data - inside face_detection function.")
        exit_program()
    except FileNotFoundError:
        print("ERROR : FileNotFoundError - Pickle File : encodings.pickle,  not present - "
              "inside face_detection function.")
        exit_program()


def main():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Face_Detection_Camera.py - at : ' + current_time + ' on : ' + current_date)

    face_detection()
    exit_program()


if __name__ == "__main__":
    main()
