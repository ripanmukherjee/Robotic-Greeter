#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Question.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Speech_Question.py is to ask YES or NO related questions to the customer. If this program does not
#               get input from customers within a given time, it will prompt a pop-up message to click ok or cancel.
#               It will be called from Main_Process.py and Main_Process.py will pass the question as an argument in
#               this program. Depending on the person's response, this program will give an output (inside of a text
#               file: Speech_Question_Output.txt) as YES or NO or NONE. And with that response, Main_Process.py will
#               perform different tasks.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose:
#               $ python3 Speech_Question.py
# **********************************************************************************************************************
"""

import os
import sys
import gtts
import glob
import subprocess
from gtts import gTTS
import speech_recognition
import speech_recognition as sr
from playsound import playsound
from nltk.corpus import stopwords
from datetime import date, datetime
from subprocess import check_output
from nltk.tokenize import word_tokenize


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
    print('Starting program : Speech_Question.py - At : ' + current_time + ' On : ' + current_date)


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
    print('Ending program : Speech_Question.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. yes_syn_words signifies all the synonym word of Yes.
    2. stop_words means all the unwanted noisy word.
    3. record signifies the setting of the recorder.
    4. mp3_filename is the mp3 file from where gtts will play the sound.
    5. text will be the initial text message.
    6. device_index will be automatically set as the available input device on the computer.
    So it is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    yes_syn_words = ['all right', 'alright', 'very well', 'of course', 'by all means', 'sure', 'certainly',
                     'absolutely', 'indeed', 'affirmative', 'in the affirmative', 'agreed', 'roger', 'aye',
                     'aye aye', 'yeah', 'yah', 'yep', 'yup', 'uh-huh', 'okay', 'ok', 'right', 'surely',
                     'yea', 'well', 'course', 'yes', 'please']
    stop_words = set(stopwords.words("english"))
    record = sr.Recognizer()
    mp3_filename = "Speech_Question"
    text = "I am going to ask few question to you. You can answer with Yes or No. If I do not get an input from you " \
           "within 5 second, then, I will prompt a pop up message to you."
    device_list = sr.Microphone.list_microphone_names()
    if 'pulse' in device_list:
        device_index = device_list.index('pulse')
    else:
        device_index = 0

    return yes_syn_words, stop_words, record, mp3_filename, text, device_index


def process_check_input_argument():
    """
    ************************************ Inside process_check_input_argument function **********************************
    This function will be called to check the input argument based on stand_alone_flag. If this process received an
    input from Main_Process.py then it will pass that argument into text and if not then it will set stand_alone_flag
    as 1, and this process will run as stand-alone.
    ************************************ Inside process_check_input_argument function **********************************
    """

    stand_alone_flag = None
    try:
        input_argv = sys.argv
        if len(input_argv) < 2:
            stand_alone_flag = 1
            text = "Hello, this is for testing. Do you want to continue?"
        else:
            text_list = []
            for i in input_argv[1:]:
                text_list.append(i)

            text = " ".join(text_list)
    except IndexError:
        stand_alone_flag = 1
        text = "Hello, this is for testing. Do you want to continue?"

    return text, stand_alone_flag


def process_speak_listen(device_index, mp3_filename, text, record, flag):
    """
    ************************************ Inside process_speak_listen function ******************************************
    This function will be called to play the sound or save the text message to an mp3 file and later play the mp3
    file, and after the play is done, this function will remove the mp3 file.
    Later it will record the response from the user, there is a timeout of 5 second. If the recorder does not get an
    input for 5 second or during any lookup error or Unknown Value Error then it will prompt a pop-up message. Based
    on the input response given by the customer this function will return it.
    ************************************ Inside process_speak_listen function ******************************************
    """

    record_text = None
    mp3_filename = mp3_filename + ".mp3"
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(mp3_filename)
        playsound(mp3_filename)
        os.remove(mp3_filename)

        if flag != 1:
            with sr.Microphone(device_index=device_index) as source:
                record.adjust_for_ambient_noise(source)
                print("Speak:")
                os.system("zenity --progress --width=400 --height=200 --title='Speak Now' "
                          "--text='Speak Now......No need to click Ok button' --no-cancel &")
                try:
                    audio = record.listen(source, timeout=5)
                    record_text = record.recognize_google(audio)
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print(record_text)
                except LookupError:
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print("ERROR : LookupError - Could not able to understand")
                    try:
                        record_text = check_output(["zenity", "--question", "--width=400", "--height=200",
                                                    "--text=I could not able to understand.\n\n" + text])
                        record_text = "Yes"
                    except subprocess.CalledProcessError:
                        print("ERROR : subprocess.CalledProcessError - inside process_speak_listen function.")
                        record_text = None

                    print(record_text)
                except speech_recognition.WaitTimeoutError:
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print("ERROR : WaitTimeoutError - Could not able to listen anything for 5 seconds")
                    try:
                        record_text = check_output(["zenity", "--question", "--width=400", "--height=200",
                                                    "--text=I could not able to listen anything for 5 seconds.\n\n"
                                                    + text])
                        record_text = "Yes"
                    except subprocess.CalledProcessError:
                        print("ERROR : subprocess.CalledProcessError - inside process_speak_listen function.")
                        record_text = None

                    print(record_text)
                except speech_recognition.UnknownValueError:
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print("ERROR : UnknownValueError - Could not able to listen anything for 5 seconds")
                    try:
                        record_text = check_output(["zenity", "--question", "--width=400", "--height=200",
                                                    "--text=I could not able to listen anything for 5 seconds.\n\n"
                                                    + text])
                        record_text = "Yes"
                    except subprocess.CalledProcessError:
                        print("ERROR : subprocess.CalledProcessError - inside process_speak_listen function.")
                        record_text = None

                    print(record_text)
    except gtts.tts.gTTSError:
        print("Connection Error : No internet connection.")
        exit_program()

    return record_text


def process_input_details(device_index, input_details, mp3_filename, record, yes_syn_words, stop_words):
    """
    ************************************ Inside process_input_details function *****************************************
    This function will tokenize and filter the words based on the response given by User. First, it will tokenize
    the sentence into word and later remove all the stop words. Then from the filtered_sent, it will search if any word
    is present in yes_syn_words or not. If yes, then this function will be treated as Yes, and if not, then it will be
    treated as No. Later that response will be return to write into an output file.
    ************************************ Inside process_input_details function *****************************************
    """

    response = "NO"
    if input_details is None:
        text = "Sorry, I did not get an input from you."
        flag = 1
        process_speak_listen(device_index, mp3_filename, text, record, flag)
        response = "NO"
    else:
        tokenized_word = word_tokenize(input_details)
        filtered_sent = []
        for word in tokenized_word:
            if word not in stop_words:
                filtered_sent.append(word.lower())

        print(filtered_sent)
        for word in filtered_sent:
            if word in yes_syn_words:
                response = "YES"
                print("Yes!! Person wants to continue")
                break
            else:
                response = "NO"
                print("No!! Do not want to continue")

    return response


def process_output_file_write(response):
    """
    ************************************ Inside process_output_file_write function *************************************
    This function will be called to write the response into a output file.
    ************************************ Inside process_output_file_write function *************************************
    """

    with open("Speech_Question_Output.txt", "w") as output_file:
        output_file.write(response)


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
    yes_syn_words, stop_words, record, mp3_filename, text, device_index = process_parameter_set()
    # process_speak_listen(mp3_filename, text, record, flag=1)
    text, stand_alone_flag = process_check_input_argument()
    input_details = process_speak_listen(device_index, mp3_filename, text, record, flag=0)
    response = process_input_details(device_index, input_details, mp3_filename, record, yes_syn_words, stop_words)
    process_output_file_write(response)
    process_delete_mp3_output_files(stand_alone_flag)
    exit_program()


if __name__ == "__main__":
    main()
