#!/usr/bin/env python3

# Project : Robotic Greeter - CareGo Tek
# Program Name : Speech_Start_End.py
# Author : Somak Mukherjee
# Date : Monday 18 May, 2020
# Version : 1
# Description : Speech_Start_End.py is to greet Known and Unknown person. It will be called from
#               ~/Main_Process/Main_Process.py with special argument as follow:
#               1. Argument when 0 (For Unknown person) : It will greet to Unknown Person
#               2. Argument when Specific Name (For Known person) : It will greet to known Person
#               3. Argument when 1 (For Known & Unknown) : It will say Bye
#
# NOTE 1 : This program can be run separately or as a stand alone program as follow for testing purpose :
# >> python3 Speech_Start_End.py

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
    print('Starting program : Speech_Start_End.py - at : ' + current_time + ' on : ' + current_date)
    stand_alone_flag = None
    try:
        input_argv = sys.argv[1]
        if input_argv == "0":
            mp3_filename = "Speech_Start_End"
            text = "Hello, Welcome to Care Go, my name is TELIA, I am Care Go’s virtual greeter."
        elif input_argv == "1":
            mp3_filename = "Speech_Start_End"
            text = "Thank you for visiting Care Go. Bye. See you later."
        else:
            mp3_filename = "Speech_Start_End"
            text = "Hello " + input_argv + ". Welcome to Care Go, do you remember me, TELIA, Care Go’s " \
                                           "virtual greeter? "
    except IndexError:
        stand_alone_flag = 1
        mp3_filename = "Speech_Start_End"
        text = "Hello, Welcome to Care Go, my name is TELIA, I am Care Go’s virtual greeter."

    process(mp3_filename, text)
    if stand_alone_flag == 1:
        print("Deleting mp3 and output file. Value of stand_alone_flag : ", str(stand_alone_flag))
        delete_mp3_output_files()

    exit_program()


if __name__ == "__main__":
    main()
