#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Normal.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Speech_Normal.py is a standard speech-related program. It will be called from the following schedule.
#               ~/Main_Process/Main_Process.py with a text message that robots need to speak. This process will not
#               be going to ask anything. It will talk just whatever text message this program will receive.
#
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose :
#               >> python3 Speech_Normal.py

import os
import sys
import glob
import pygame
from gtts import gTTS
from datetime import date, datetime


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Speech_Start_End.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process(mp3_filename, text):
    mp3_filename = mp3_filename + ".mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(mp3_filename)
    pygame.mixer.init()
    audio = pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
        continue


def delete_mp3_output_files():
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
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Speech_Normal.py - at : ' + current_time + ' on : ' + current_date)
    stand_alone_flag = None
    mp3_filename = "Speech_Normal"
    try:
        input_argv = sys.argv
        if len(input_argv) < 2:
            stand_alone_flag = 1
            text = "Hello, this is for testing. "
        else:
            text_list = []
            for i in input_argv[1:]:
                text_list.append(i)

            text = " ".join(text_list)
    except IndexError:
        stand_alone_flag = 1
        text = "Hello, this is for testing. "

    process(mp3_filename, text)
    if stand_alone_flag == 1:
        print("Deleting mp3 and output file. Value of stand_alone_flag : ", str(stand_alone_flag))
        delete_mp3_output_files()

    exit_program()


if __name__ == "__main__":
    main()
