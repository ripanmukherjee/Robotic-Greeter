#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Speech_Name_Organization.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Speech_Name_Organization.py is to ask the Name & Organization to Unknown Person. Later it will ask the
#               person if they want to save their details or not. If this program does not get input from users
#               within a given time, then it will prompt a pop-up message to enter the details or to click ok or
#               cancel. It will be called from ~/Main_Process/Main_Process.py, and depending on the person's
#               response, this program will give an output into a file (Speech_Name_Organization_Output.text)
#               as YES or NO or NONE. And with that response, Main_Process.py will perform different task.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose:
#               $ python3 Speech_Name_Organization.py
# **********************************************************************************************************************
"""

import os
import sys
import gtts
import glob
import nltk
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
    print('Starting program : Speech_Name_Organization.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Speech_Name_Organization.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program:

    1. yes_syn_words signifies all the synonym word of Yes.
    2. stop_words means all the unwanted noisy word.
    3. record signifies the setting of the recorder.
    4. mp3_filename is the mp3 file from where gTTS will play the sound.
    5. text will be the initial text message which will be played by gTTS.
    6. device_index will be set automatically as the available microphone input device on the computer.
    7. output_file is the file where the final response will be written.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    yes_syn_words = ['all right', 'alright', 'very well', 'of course', 'by all means', 'sure', 'certainly',
                     'absolutely', 'indeed', 'affirmative', 'in the affirmative', 'agreed', 'roger', 'aye',
                     'aye aye', 'yeah', 'yah', 'yep', 'yup', 'uh-huh', 'okay', 'ok', 'right', 'surely',
                     'yea', 'well', 'course', 'yes', 'please']
    stop_words = set(stopwords.words("english"))
    record = sr.Recognizer()
    mp3_filename = "Speech_Name_Organization"
    text = "I am going to ask your name and organization. If I do not get an input from you within 5 second, then, " \
           "I will prompt a pop up message to you."
    device_list = sr.Microphone.list_microphone_names()
    if 'pulse' in device_list:
        device_index = device_list.index('pulse')
    else:
        device_index = 0

    output_file = "Speech_Name_Organization_Output.txt"

    return yes_syn_words, stop_words, record, mp3_filename, text, device_index, output_file


def process_check_input_argument():
    """
    ************************************ Inside process_check_input_argument function **********************************
    This function will be called to set the value of stand_alone_flag.

    If this process received an input from Main_Process.py then it will set stand_alone_flag as 0 and if not then will
    set as 1, and this process will run as stand-alone.
    ************************************ Inside process_check_input_argument function **********************************
    """

    try:
        input_argv = sys.argv[1]
        if input_argv == "0":
            stand_alone_flag = 0
        else:
            stand_alone_flag = 0
    except IndexError:
        stand_alone_flag = 1

    return stand_alone_flag


def process_speak_listen(device_index, mp3_filename, text, record, flag):
    """
    ************************************ Inside process_speak_listen function ******************************************
    This function will be called to play the sound or save the text message to an mp3 file, play the mp3 file, and
    after the sound play, this function will remove the mp3 file.

    This function will prompt a pop-up message as Speak Now to indicate the user that they need to speak now.
    Later, it will record the response from the user and will store into text. There is a timeout of 5 seconds; if the
    recorder does not get an input for 5 seconds or any lookup error or Unknown Value Error, it will set text as None.

    This function will only record the user's response when the flag is not "1". If the flag's value is "1", this
    function will only play the sound of the text and exit from this function.

    This function uses Google-Text-To-Speech (gtts) module that needs an internet connection. Without an internet
    connection, this function will give an ERROR and will exit from the program.
    ************************************ Inside process_speak_listen function ******************************************
    """

    mp3_filename = mp3_filename + ".mp3"
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(mp3_filename)
        playsound(mp3_filename)
        os.remove(mp3_filename)

        if flag != 1:
            with sr.Microphone(device_index=device_index) as source:
                record.adjust_for_ambient_noise(source, duration=1)
                print("Speak:")
                os.system("zenity --progress --width=400 --height=200 --title='Speak Now' "
                          "--text='Speak Now......No need to click Ok button' --no-cancel &")
                try:
                    audio = record.listen(source, timeout=5)
                    text = record.recognize_google(audio)
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print(text)
                except LookupError:
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print("ERROR : LookupError - Could not able to understand")
                    text = None
                except speech_recognition.WaitTimeoutError:
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print("ERROR : WaitTimeoutError - Could not able to listen anything for 5 seconds")
                    text = None
                except speech_recognition.UnknownValueError:
                    os.system("ps -ef|grep zenity|awk '{print $2}'|head -1|xargs kill -9")
                    print("ERROR : UnknownValueError - Could not able to listen anything for 5 seconds")
                    text = None
    except gtts.tts.gTTSError:
        print("ERROR : Connection Error : No internet connection.")
        exit_program()
    except PermissionError:
        print("ERROR : No permission")
        exit_program()

    return text


def process_token_sentence(text):
    """
    ************************************ Inside process_token_sentence function ****************************************
    This function will be called to tokenize the sentence from the input text.
    ************************************ Inside process_token_sentence function ****************************************
    """

    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    return sentences


def process_extract_entity_names(t):
    """
    ************************************ Inside process_extract_entity_names function **********************************
    This function will be called to find the person's name and organization's name.

    This process will check each word in tree level is similar to NE or not. NE signifies if that word is Noun related
    name. If this function finds any word similar with NE then it will append into entity_names and later it will
    return this list.
    ************************************ Inside process_extract_entity_names function **********************************
    """

    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(process_extract_entity_names(child))

    return entity_names


def process_extract_name_organization_details(device_index, mp3_filename, text, record):
    """
    ************************************ Inside process_extract_name_organization_details function *********************
    This function will be called to return a person's name and organization's name as details.

    First, this function will receive a text and call process_speak_listen function with flag value as 0 to record the
    user's answer. That response will be store into the text variable. If the text value is None, then it will
    return the detail's value as None. If not, then it will call process_token_sentence function to get the tokenize
    sentence and later call to process_extract_entity_names to find the person's name or organization's name from the
    tokenize sentence.
    ************************************ Inside process_extract_name_organization_details function *********************
    """

    flag = 0
    text = process_speak_listen(device_index, mp3_filename, text, record, flag)
    if text is None:
        details = None
    else:
        sentences = process_token_sentence(text)
        entity_names = []

        for tree in sentences:
            entity_names.extend(process_extract_entity_names(tree))

        print(set(entity_names))
        try:
            details = entity_names[0]
        except IndexError:
            details = None

    return details


def process_organization(device_index, mp3_filename, record, text, name):
    """
    ************************************ Inside process_organization function ******************************************
    This function will ask the user to enter the Organization name in a pop-up message.

    First, it will prompt a pop-up message for the user to enter their Company's Name, only if the Company's Name
    value is None in the previous function. If the users enter their Company's Name, then this function will set
    the text as a different text message. But, If the user chooses not to enter the Company's Name, then this
    function will set the text as final speak text value.
    ************************************ Inside process_organization function ******************************************
    """

    organization = process_extract_name_organization_details(device_index, mp3_filename, text, record)
    speak_text = ". Actually, I do not have your details. Would you like to save your details for future?"
    if organization is None:
        try:
            check_output(["zenity", "--question", "--width=400", "--height=200",
                          "--text=Sorry, I could not get your organization.\n\n"
                          "Do you want to enter the name of your organization?"])
            args_get_details = "zenity --forms --width=500 --height=200 --title='Organization' \
                                            --text='Enter your organization Name' \
                                            --add-entry='Organization'"
            try:
                details = check_output(args_get_details, shell=True)
                details = details.decode().split('|')
                organization = details[0]
                text = "Okay. " + name + ". Say Hi to everyone at " + organization + speak_text

            except subprocess.CalledProcessError:
                text = "Okay. " + name + speak_text
        except subprocess.CalledProcessError:
            text = "Okay. " + name + speak_text
    else:
        text = "Okay. " + name + speak_text

    return text


def process_name_organization(device_index, mp3_filename, record):
    """
    ************************************ Inside process_name_organization function *************************************
    This function will ask the user to enter the Name in a pop-up message and later ask the company name.

    First, it will prompt a pop-up message for the user to enter their Name, only if the name value is None in the
    previous function. If the user enter their names, then this function will ask the Company's name to the
    user. If the user chooses not to enter the Company's Name then this function will set the text as final
    speak text value.
    ************************************ Inside process_name_organization function *************************************
    """

    speak_text = "Actually, I do not have your details. Would you like to save your details for future?"
    try:
        check_output(["zenity", "--question", "--width=400", "--height=200",
                      "--text=Sorry, I could not get your name.\n\n" "Do you want to enter your name?"])
        args_get_details = "zenity --forms --width=500 --height=200 --title='Name' \
                    --text='Enter your First Name' \
                    --add-entry='First Name'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            name = details[0]
            text = "All right " + name + ", and what company are you with?"
            text = process_organization(device_index, mp3_filename, record, text, name)
        except subprocess.CalledProcessError:
            text = speak_text
    except subprocess.CalledProcessError:
        text = speak_text

    return text


def process_name(device_index, mp3_filename, record):
    """
    ************************************ Inside process_name function **************************************************
    This function will ask the user's Name and Organization.

    First, it will ask the Name of the person; if the value of Name is None, it will call process_name_organization.
    If the Name is not None, then it will ask the company name by calling process_extract_name_organization_details.
    Later, based on users' input details, this function will set the final text message as if the user wants
    to save their details or not and return this text for the closing process.
    ************************************ Inside process_name function **************************************************
    """

    text = "May I please ask your name?"
    name = process_extract_name_organization_details(device_index, mp3_filename, text, record)

    if name is None:
        text = process_name_organization(device_index, mp3_filename, record)
    else:
        text = "All right, and what company are you with?"
        input_details = process_extract_name_organization_details(device_index, mp3_filename, text, record)
        if input_details is None:
            text = process_organization(device_index, mp3_filename, record, text, name)
        else:
            text = "Actually, I do not have your details. Would you like to save your details for future?"

    return text


def process_input_details(device_index, input_details, mp3_filename, record, yes_syn_words, stop_words):
    """
    ************************************ Inside process_input_details function *****************************************
    This function will set the final response as YES or NO by tokenizing.

    First, based on the last response receives from the users, this function will prompt a pop-up message if the
    user wants to save their details or not. In this pop-up message, users can click on YES or NO button. If
    the user clicks on the NO button, then this function will set input details and final response as None. But if
    the user clicks on the YES button, then this function will tokenize the sentence into word and later remove all
    the stop words. Then from the filtered_sent, it will search if any word is present in yes_syn_words or not. If yes,
    then this function will set the final response as YES, and if not, then it will set as NO. Later, it will return
    the value of the final response.
    ************************************ Inside process_input_details function *****************************************
    """

    if input_details is None:
        try:
            check_output(["zenity", "--question", "--width=400", "--height=200",
                          "--text=I could not able to understand.\n\n"
                          "Actually, I do not have your details. Would you like to save your details for future?"])
            input_details = "Yes"
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_input_details function.")
            input_details = None
    else:
        pass

    response = "NONE"

    if input_details is None:
        text = "Sorry, I did not get an input from you."
        flag = 1
        process_speak_listen(device_index, mp3_filename, text, record, flag)
        response = "NONE"
    else:
        tokenized_word = word_tokenize(input_details)
        filtered_sent = []
        for word in tokenized_word:
            if word not in stop_words:
                filtered_sent.append(word.lower())

        for word in filtered_sent:
            if word in yes_syn_words:
                response = "YES"
                print("Yes!! Person wants to continue")
                break
            else:
                response = "NO"
                print("No!! Do not want to continue")

    return response


def process_output_file_write(output_file, response):
    """
    ************************************ Inside process_output_file_write function *************************************
    This function will be called to write the final response into a output file.
    ************************************ Inside process_output_file_write function *************************************
    """

    with open(output_file, "w") as output_file:
        output_file.write(response)


def process_delete_mp3_output_files(stand_alone_flag):
    """
    ************************************ Inside process_delete_mp3_output_files function *******************************
    This function will be called to delete all mp3 and output files before to end of the program.
    ************************************ Inside process_delete_mp3_output_files function *******************************
    """

    if stand_alone_flag == 1:
        print("Deleting mp3 and output file. Value of stand_alone_flag : ", str(stand_alone_flag))
        mp3_files = glob.glob('*.mp3')
        output_files = glob.glob('*_Output.txt')
        for files in mp3_files:
            try:
                os.remove(files)
            except OSError:
                print("Cannot able delete the old mp3 files.")

        for files in output_files:
            try:
                os.remove(files)
            except OSError:
                print("Cannot able delete the old output text files.")


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    yes_syn_words, stop_words, record, mp3_filename, text, device_index, output_file = process_parameter_set()
    stand_alone_flag = process_check_input_argument()
    process_speak_listen(device_index, mp3_filename, text, record, flag=1)
    text = process_name(device_index, mp3_filename, record)
    input_details = process_speak_listen(device_index, mp3_filename, text, record, flag=0)
    response = process_input_details(device_index, input_details, mp3_filename, record, yes_syn_words, stop_words)
    process_output_file_write(output_file, response)
    process_delete_mp3_output_files(stand_alone_flag)
    exit_program()


if __name__ == "__main__":
    main()
