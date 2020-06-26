#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Normal.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Speech_Normal.py is a standard speech-related program. It will be called from the Main_Process.py with
#               a text message that robots need to speak. This process will not be going to ask anything. It will
#               talk just whatever text message this program will receive.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose :
#               $ python3 Speech_Normal.py
# **********************************************************************************************************************
"""

import os
import sys
import glob
from gtts import gTTS
from playsound import playsound
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
    print('Starting program : Speech_Normal.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Speech_Start_End.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. stand_alone_flag signifies if the program is running from Main_Process.py or not.
    2. mp3_filename signifies the mp3 filename that will be used by gTTS.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """
    stand_alone_flag = None
    mp3_filename = "Speech_Normal"

    return stand_alone_flag, mp3_filename


def process_check_input_argument(stand_alone_flag):
    """
    ************************************ Inside process_check_input_argument function **********************************
    This function will be called to set the value of stand_alone_flag and text message.

    If this process received an input from Main_Process.py then it will pass that argument into text, and the value
    of the stand_alone_flag will be None. If this process gets input argument less than two characters of length or
    does not get any input argument, it will set stand_alone_flag as 1 (To run the program as stand-alone), and set
    the text as a sample text message. Later, this function will pass these parameters for other tasks.
    ************************************ Inside process_check_input_argument function **********************************
    """

    try:
        input_argv = sys.argv
        if len(input_argv) < 2:
            stand_alone_flag = 1
            text = "Hello, this is for testing. Sound is working."
        else:
            text_list = []
            for i in input_argv[1:]:
                text_list.append(i)

            text = " ".join(text_list)
    except IndexError:
        stand_alone_flag = 1
        text = "Hello, this is for testing. Sound is working."

    return text, stand_alone_flag


def process_gtts_playsound(mp3_filename, text):
    """
    ************************************ Inside process_gtts_playsound function ****************************************
    This function will be called to play the sound or save the text message to an mp3 file, play the mp3 file, and
    after the sound play, this function will remove the mp3 file.
    ************************************ Inside process_gtts_playsound function ****************************************
    """

    mp3_filename = mp3_filename + ".mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(mp3_filename)
    playsound(mp3_filename)
    os.remove(mp3_filename)


def process_delete_mp3_output_files(stand_alone_flag):
    """
    ************************************ Inside process_delete_mp3_output_files function *******************************
    This function will be called to delete all mp3 and output files before to end of the program.
    ************************************ Inside process_delete_mp3_output_files function *******************************
    """

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
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    stand_alone_flag, mp3_filename = process_parameter_set()
    text, stand_alone_flag = process_check_input_argument(stand_alone_flag)
    process_gtts_playsound(mp3_filename, text)
    process_delete_mp3_output_files(stand_alone_flag)
    exit_program()


if __name__ == "__main__":
    main()
