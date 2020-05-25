#!/usr/bin/env python3

# Project : Robotic Greeter - CareGo Tek
# Program Name : Speech_Normal.py
# Author : Somak Mukherjee
# Date : Monday 18 May, 2020
# Version : 1
# Description : Speech_Normal.py is a normal speech related program. It will be called from the following program
#               ~/Main_Process/Main_Process.py with text message that robot need to speak. This process will not gonna
#               ask anything. It will just speak whatever text message this program will receive.
#
# NOTE 1 : This program can be run separately or as a stand alone program as follow for testing purpose :
# >> python3 Speech_Normal.py

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
    print('Starting program : Speech_Normal.py - at : ' + current_time + ' on : ' + current_date)

    mp3_filename = "Speech_Normal"
    try:
        input_argv = sys.argv
        if len(input_argv) < 2:
            text = "Hello, this is for testing. "
        else:
            text_list = []
            for i in input_argv[1:]:
                text_list.append(i)

            text = " ".join(text_list)
    except IndexError:
        text = "Hello, this is for testing. "

    process(mp3_filename, text)
    exit_program()


if __name__ == "__main__":
    main()
