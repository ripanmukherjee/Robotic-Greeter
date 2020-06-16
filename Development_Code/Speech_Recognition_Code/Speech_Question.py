#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Question.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Speech_Question.py is to ask YES or NO related questions to the customer. It will be called from
#               ~/Main_Process/Main_Process.py and Main_Process.py will pass the question as an argument in this
#               program. Depending on the person's response, this program will give an output (inside of a text file :
#               Speech_Question_Output.txt) as YES or NO or NONE. And with that response, Main_Process.py will perform
#               different tasks.
#
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose:
#               >> python3 Speech_Question.py


import os
import sys
import gtts
import nltk
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


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Speech_Question.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def token_sentence(text):
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    return sentences


def process_speak_listen(mp3_filename, text, record, flag):
    record_text = None
    mp3_filename = mp3_filename + ".mp3"
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(mp3_filename)
        playsound(mp3_filename)
        os.remove(mp3_filename)

        if flag != 1:
            with sr.Microphone(device_index=0) as source:
                record.adjust_for_ambient_noise(source)
                print("Speak:")
                try:
                    audio = record.listen(source, timeout=5)
                    record_text = record.recognize_google(audio)
                    print(record_text)
                except LookupError:
                    print("ERROR : LookupError - Couldn't able to understand")
                    try:
                        record_text = check_output(["zenity", "--question", "--width=400", "--height=200",
                                                    "--text=We couldn't able to understand.\n\n"
                                                    "Do you want to continue?"])
                        record_text = "Yes"
                    except subprocess.CalledProcessError:
                        print("ERROR : subprocess.CalledProcessError - inside process_speak_listen function.")
                        record_text = None

                    print(record_text)
                except speech_recognition.WaitTimeoutError:
                    print("ERROR : WaitTimeoutError - Couldn't able to listen anything for 5 seconds")
                    try:
                        record_text = check_output(["zenity", "--question", "--width=400", "--height=200",
                                                    "--text=We couldn't able to listen anything for 5 seconds.\n\n"
                                                    "Do you want to continue?"])
                        record_text = "Yes"
                    except subprocess.CalledProcessError:
                        print("ERROR : subprocess.CalledProcessError - inside process_speak_listen function.")
                        record_text = None

                    print(record_text)
                except speech_recognition.UnknownValueError:
                    print("ERROR : UnknownValueError - Couldn't able to listen anything for 5 seconds")
                    try:
                        record_text = check_output(["zenity", "--question", "--width=400", "--height=200",
                                                    "--text=We couldn't able to listen anything for 5 seconds.\n\n"
                                                    "Do you want to continue?"])
                        record_text = "Yes"
                    except subprocess.CalledProcessError:
                        print("ERROR : subprocess.CalledProcessError - inside process_speak_listen function.")
                        record_text = None

                    print(record_text)
    except gtts.tts.gTTSError:
        print("Connection Error : No internet connection.")
        exit_program()

    return record_text


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
    print('Starting program : Speech_Question.py - At : ' + current_time + ' On : ' + current_date)

    record = sr.Recognizer()
    yes_syn_words = ['all right', 'alright', 'very well', 'of course', 'by all means', 'sure', 'certainly',
                     'absolutely', 'indeed', 'affirmative', 'in the affirmative', 'agreed', 'roger', 'aye',
                     'aye aye', 'yeah', 'yah', 'yep', 'yup', 'uh-huh', 'okay', 'Ok', 'okey-dokey', 'okey-doke',
                     'achcha', 'right', 'righty-ho', 'surely', 'yea', 'well', 'course', 'yes', 'please', 'do']
    stop_words = set(stopwords.words("english"))
    mp3_filename = "Speech_Question"
    stand_alone_flag = None

    flag = 1
    text = "We are going to ask few question to you. You can answer with Yes or No. If we do not get any input for " \
           "5 second, then, we will prompt a pop up message to you. You can choose option from there."
    process_speak_listen(mp3_filename, text, record, flag)

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

    flag = 0
    input_details = process_speak_listen(mp3_filename, text, record, flag)
    response = "NO"

    if input_details is None:
        text = "Sorry, we didn't get any input."
        flag = 1
        process_speak_listen(mp3_filename, text, record, flag)
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
                print("No!! Don't want to continue")

    with open("Speech_Question_Output.txt", "w") as output_file:
        output_file.write(response)

    if stand_alone_flag == 1:
        print("Deleting mp3 and output file. Value of stand_alone_flag : ", str(stand_alone_flag))
        delete_mp3_output_files()

    exit_program()


if __name__ == "__main__":
    main()
