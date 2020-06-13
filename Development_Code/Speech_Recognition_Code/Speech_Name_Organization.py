#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Name_Organization.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Speech_Name_Organization.py is to ask the Name & Organization to Unknown Person. Later it will ask to
#               the person if they want to save their details or not. It will be called from
#               ~/Main_Process/Main_Process.py and depending on the person's response this program will give an output
#               (inside of a text file as follow: Speech_Name_Organization_Output.text) as YES or NO or NONE.
#               And with that response Main_Process.py will perform different task.
#
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose:
#               >> python3 Speech_Name_Organization.py


import os
import sys
import gtts
import glob
import nltk
from gtts import gTTS
import speech_recognition
import speech_recognition as sr
from playsound import playsound
from nltk.corpus import stopwords
from datetime import date, datetime
from nltk.tokenize import word_tokenize


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Speech_Name_Organization.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def token_sentence(text):
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    return sentences


def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names


def process_speak_listen(mp3_filename, text, record, flag):
    mp3_filename = mp3_filename + ".mp3"
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(mp3_filename)
        playsound(mp3_filename)
        os.remove(mp3_filename)

        if flag != 1:
            with sr.Microphone(device_index=4) as source:
                record.pause_threshold = 1
                record.adjust_for_ambient_noise(source, duration=1)
                print("Speak:")
                try:
                    audio = record.listen(source, timeout=3)
                    text = record.recognize_google(audio)
                    print(text)
                except LookupError:
                    print("ERROR : LookupError - Couldn't able to understand")
                    text = None
                except speech_recognition.WaitTimeoutError:
                    print("ERROR : WaitTimeoutError - Couldn't able to listen anything for 3 seconds")
                    text = None
                except speech_recognition.UnknownValueError:
                    print("ERROR : UnknownValueError - Couldn't able to listen anything for 3 seconds")
                    text = None
    except gtts.tts.gTTSError:
        print("Connection Error : No internet connection.")
        exit_program()
    except PermissionError:
        print("No Permission")

    return text


def process_details(mp3_filename, text, record):
    flag = 0
    text = process_speak_listen(mp3_filename, text, record, flag)
    if text is None:
        details = None
    else:
        sentences = token_sentence(text)
        entity_names = []

        for tree in sentences:
            entity_names.extend(extract_entity_names(tree))

        print(set(entity_names))
        try:
            details = entity_names[0]
        except IndexError:
            details = None

    return details


def delete_mp3_output_files():
    mp3_files = glob.glob('*.mp3')
    output_files = glob.glob('*_Output.txt')
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
    record = sr.Recognizer()
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Speech_Name_Organization.py - At : ' + current_time + ' On : ' + current_date)

    yes_syn_words = ['all right', 'alright', 'very well', 'of course', 'by all means', 'sure', 'certainly',
                     'absolutely', 'indeed', 'affirmative', 'in the affirmative', 'agreed', 'roger', 'aye',
                     'aye aye', 'yeah', 'yah', 'yep', 'yup', 'uh-huh', 'okay', 'Ok', 'okey-dokey', 'okey-doke',
                     'achcha', 'right', 'righty-ho', 'surely', 'yea', 'well', 'course', 'yes', 'please']
    stop_words = set(stopwords.words("english"))
    stand_alone_flag = None

    try:
        input_argv = sys.argv[1]
        if input_argv == "0":
            stand_alone_flag = 0
    except IndexError:
        stand_alone_flag = 1

    mp3_filename = "Speech_Name_Organization"
    text = "May I please ask your name?"
    name = process_details(mp3_filename, text, record)

    if name is None:
        text = "Sorry, we couldn't get your name. Actually, we Don't Have Your Details. " \
               "Would you like to save your details for future?"
    else:
        text = "Okay. And what company are you with?"
        process_details(mp3_filename, text, record)
        text = "Okay. " + name + ". I hope, that I am guessing your name correctly. Actually, " \
                                 "we Don't Have Your Details. Would you like to save your details for future?"

    flag = 0
    input_details = process_speak_listen(mp3_filename, text, record, flag)
    response = "NONE"

    if input_details is None:
        text = "Sorry, we didn't get any input."
        flag = 1
        process_speak_listen(mp3_filename, text, record, flag)
        response = "NONE"
    else:
        tokenized_word = word_tokenize(input_details)
        filtered_sent = []
        for word in tokenized_word:
            if word not in stop_words:
                filtered_sent.append(word)

        for word in filtered_sent:
            if word in yes_syn_words:
                response = "YES"
                break
            else:
                response = "NO"

    with open("Speech_Name_Organization_Output.txt", "w") as output_file:
        output_file.write(response)

    if stand_alone_flag == 1:
        print("Deleting mp3 and output file. Value of stand_alone_flag : ", str(stand_alone_flag))
        delete_mp3_output_files()

    exit_program()


if __name__ == "__main__":
    main()
