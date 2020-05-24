#!/usr/bin/env python3

# Project : Robotic Greeter - CareGo Tek
# Program Name : Speech_Start_End.py
# Author : Somak Mukherjee
# Date : Monday 18 May, 2020
# Version : 1
# Description : This program is to greet Known and Unknown person. It will be call from
#               ~/Main_Process/Main_Process.py with special argument as follow:
#               1. Argument when 0 (For Unknown person) : It will greet to Unknown Person
#               2. Argument when Specific Name (For Known person) : It will greet to known Person
#               3. Argument when 1 (For Known & Unknown) : It will say Bye
#
# NOTE : This program can be run separately or as a stand alone program as follow for testing purpose :
# >> python3 Speech_Start_End.py

import sys
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


def main():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Speech_Start_End.py - at : ' + current_time + ' on : ' + current_date)

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
                                           "virtual greeter? Who are you here to see today? "
    except IndexError:
        mp3_filename = "Speech_Start_End"
        text = "Hello, Welcome to Care Go, my name is TELIA, I am Care Go’s virtual greeter."

    process(mp3_filename, text)
    exit_program()


if __name__ == "__main__":
    main()
