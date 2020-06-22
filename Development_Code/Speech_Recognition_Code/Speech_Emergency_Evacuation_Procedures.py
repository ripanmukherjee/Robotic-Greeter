#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Emergency_Evacuation_Procedures.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# ----------------------------------------------------------------------------------------------------------------------
# Description:  Speech_Emergency_Evacuation_Procedures.py program is to show the emergency and evacuation
#               procedure and while showing the image, this program will describe the image by gTTS. All the pictures
#               of emergency and evacuation procedures are present inside Emergency_Evacuation_Procedures folder.
#               Please check def process_parameter_set() function and check the path before executing this process.
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose:
#               $ python3 Speech_Emergency_Evacuation_Procedures.py
# ----------------------------------------------------------------------------------------------------------------------

import os
import sys
import cv2
import numpy as np
from gtts import gTTS
from pathlib import Path
from playsound import playsound
from datetime import date, datetime


def start_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Speech_Emergency_Evacuation_Procedures.py - at : ' + current_time + ' on : ' +
          current_date)


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Speech_Emergency_Evacuation_Procedures.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    emergency_evacuation_procedures_path = 'Emergency_Evacuation_Procedures'
    mp3_filename = "Speech_Emergency_Evacuation_Procedure"

    return emergency_evacuation_procedures_path, mp3_filename


def process_gtts_playsound(mp3_filename, text):
    mp3_filename = mp3_filename + ".mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(mp3_filename)
    playsound(mp3_filename)
    os.remove(mp3_filename)


def emergency_evacuation_process(emergency_evacuation_procedures_path, mp3_filename):
    path = Path(emergency_evacuation_procedures_path)
    if path.exists() is False:
        print("ERROR : path.exits() is false - Directory : emergency_evacuation_procedures_path is not present - "
              "inside emergency_evacuation_process function.")
        exit_program()
    else:
        os.chdir(path)

        text = "I want to point out with our Emergency Evacuation Procedures in front of you."
        process_gtts_playsound(mp3_filename, text)

        print("Showing Image - Emergency Evacuation Procedure")
        image_emergency_evacuation_procedures = cv2.imread('Emergency_Evacuation_Procedures.png', 0)
        cv2.imshow('Emergency Evacuation Procedures', image_emergency_evacuation_procedures)
        text = "Please read the Emergency Evacuation Procedure and close it, once you finish."
        process_gtts_playsound(mp3_filename, text)
        cv2.waitKey(0)

        print("Showing Image - Employee and Occupants Responsibilities")
        image_employee_and_occupants_responsibilities = cv2.imread('Employee_and_Occupants_Responsibilities.png', 0)
        cv2.imshow('Employee and Occupants Responsibilities', image_employee_and_occupants_responsibilities)
        text = "Please read the Employee and Occupants Responsibilities and close it, once you finish."
        process_gtts_playsound(mp3_filename, text)
        cv2.waitKey(0)

        print("Showing Image - Designated Meeting Area")
        image_meeting_area = cv2.imread('Designated_Meeting_Area.png', 0)
        cv2.imshow('Designated Meeting Area', image_meeting_area)
        text = "We want to take care of you, when you visit us and in the unlikely event of a fire or emergency, we " \
               "want you to be safe. If you are alerted of a fire or emergency, leave the building from the nearest " \
               "exit, close doors behind you and report to the designated meeting area. Remember to remain calm, and " \
               "do not re-enter the building until declared safe. Do not leave the site unless permission is given. " \
               "The designated meeting area is shown on this map between the west parking lot and the street."
        process_gtts_playsound(mp3_filename, text)
        cv2.waitKey(0)

        print("Showing Image - Main Floor and Second Floor Layout and Emergency Exits")
        image_main_floor = cv2.imread('Main_Floor_Layout_and_Emergency_Exits.png', 0)
        image_main_floor = cv2.resize(image_main_floor, (700, 800))
        image_second_floor = cv2.imread('Second_Floor_Layout_and_Emergency_Exits.png', 0)
        image_second_floor = cv2.resize(image_second_floor, (800, 800))
        emergency_exit_picture = np.concatenate((image_main_floor, image_second_floor), axis=1)
        cv2.imshow('Main Floor and Second Floor Layout and Emergency Exits', emergency_exit_picture)
        text = "This map shows  Main Floor and Second Floor Layout and emergency exits and it is posted throughout " \
               "the building. There is one in the lobby right over there."
        process_gtts_playsound(mp3_filename, text)
        cv2.waitKey(0)


def main():
    start_program()
    emergency_evacuation_procedures_path, mp3_filename = process_parameter_set()
    emergency_evacuation_process(emergency_evacuation_procedures_path, mp3_filename)
    exit_program()


if __name__ == "__main__":
    main()
