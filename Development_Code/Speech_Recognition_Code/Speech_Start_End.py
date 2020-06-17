#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Start_End.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# ----------------------------------------------------------------------------------------------------------------------
# Description:  Speech_Start_End.py is to greet the Known and Unknown person. It will be called from
#               ~/Main_Process/Main_Process.py with first argument as follow:
#               1. Case when 0 (For Unknown person): It will greet to Unknown Person
#               2. Case when Specific Name (For Known person): It will welcome to known Person
#               3. Case when 1 (For Known & Unknown): It will say Bye
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose :
#               >> python3 Speech_Start_End.py
# ----------------------------------------------------------------------------------------------------------------------

import os
import sys
import glob
from gtts import gTTS
from playsound import playsound
from datetime import date, datetime


def start_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Speech_Start_End.py - at : ' + current_time + ' on : ' + current_date)


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Speech_Start_End.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    stand_alone_flag = None
    mp3_filename = "Speech_Start_End"

    return stand_alone_flag, mp3_filename


def check_input_argument(stand_alone_flag):
    try:
        input_argv = sys.argv[1]
        if input_argv == "0":
            text = "Hello, Welcome to Care Go, my name is TELIA. I am Care Go’s virtual greeter."
        elif input_argv == "1":
            text = "Thank you for visiting Care Go. Bye. See you later."
        else:
            text = "Hello " + input_argv + ". Welcome to Care Go, do you remember me, TELIA, Care Go’s " \
                                           "virtual greeter? "
    except IndexError:
        stand_alone_flag = 1
        text = "Hello, Welcome to Care Go, my name is TELIA. I am Care Go’s virtual greeter."

    return text, stand_alone_flag


def process(mp3_filename, text):
    mp3_filename = mp3_filename + ".mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(mp3_filename)
    playsound(mp3_filename)
    os.remove(mp3_filename)


def delete_mp3_output_files(stand_alone_flag):
    if stand_alone_flag == 1:
        print("Deleting mp3 and output file. Value of stand_alone_flag : ", str(stand_alone_flag))
        mp3_files = glob.glob('*.mp3', recursive=True)
        output_files = glob.glob('*_Output.txt', recursive=True)
        for files in mp3_files:
            try:
                os.remove(files)
            except OSError:
                print("Cannot delete the old mp3 files.")

        for files in output_files:
            try:
                os.remove(files)
            except OSError:
                print("Cannot delete the old output text files.")


def main():
    start_program()
    stand_alone_flag, mp3_filename = process_parameter_set()
    text, stand_alone_flag = check_input_argument(stand_alone_flag)
    process(mp3_filename, text)
    delete_mp3_output_files(stand_alone_flag)
    exit_program()


if __name__ == "__main__":
    main()
