#!/usr/bin/env python3

# Project : Robotic Greeter - CareGo Tek
# Program Name : Main_Process.py
# Author : Somak Mukherjee
# Date : Friday 24 April, 2020
# Version : 1
# Description : This program is the main program which will perform face_detection, speech_recognition & database_code.
#               It will first detect the person face in the real time video camera.
#
#               If the Robot detect the face then will do some steps as follow :
#               1. Greet by saying the name of the person,
#               2. Ask the person if they want to meet or search somebody, if they want to modify their old data,
#               3. etc.
#
#               If the Robot cannot detect the face then will do some steps as follow :
#               1. Ask the person name and organization,
#               2. Ask the person if they want to save their details and photos,
#               2. Ask the person if they want to meet or search somebody, if they want to modify their old data
#               3. etc.
#
# NOTE : In the program there are one main directory :
#           main_directory = "/home/somak/Final-Project-Robotic-Greeter/carego_project/development/"
#           Please make sure to change or validate before putting ii into Production.
#
# NOTE : This program can be run separately or as a stand alone program as follow :
# >> python3 Main_Process.py

import os
import sys
import psycopg2
import subprocess
from pathlib import Path
from datetime import date, datetime
from subprocess import check_output


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Main_Process.py - At: ' + current_time + ' on : ' + current_date)
    sys.exit()


def checking_directory():
    database_code_directory = Path("Database_Code")
    face_recognition_code_directory = Path("Face_Recognition_Code")
    speech_recognition_code_directory = Path("Speech_Recognition_Code")

    if database_code_directory.exists() is False:
        print("ERROR : Directory : Database_Code is not present - inside checking_directory function.")
        exit_program()
    elif face_recognition_code_directory.exists() is False:
        print("ERROR : Directory : Face_Recognition_Code is not present - inside checking_directory function.")
        exit_program()
    elif speech_recognition_code_directory.exists() is False:
        print("ERROR : Directory : Speech_Recognition_Code is not present - inside checking_directory function.")
        exit_program()
    else:
        pass

    return database_code_directory, face_recognition_code_directory, speech_recognition_code_directory


def ask_question(text):
    try:
        output = check_output(["zenity", "--question", "--width=400", "--height=200", "--text=" + text])
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside ask_question function.")
        output = None

    return output


def ask_search(database_code_directory, main_directory, detect_name):
    text = "Would you like to search someone here?"
    response = ask_question(text)
    if response is not None:
        os.chdir(database_code_directory)
        process_search_details()
        os.chdir(main_directory)
        print("INFO - {} customer searched someone.".format(detect_name))
    else:
        print("INFO - {} customer didn't want to search someone.".format(detect_name))


def ask_update(database_code_directory, main_directory, detect_name):
    text = "Would you like to update your details?"
    response = ask_question(text)
    if response is not None:
        os.chdir(database_code_directory)
        process_update_detail()
        os.chdir(main_directory)
        print("INFO - {} customer updated detail.".format(detect_name))
    else:
        print("INFO - {} customer didn't want to updated detail.".format(detect_name))


def process_speak_start_end(passing_arg):
    program_name = "Speech_Start_End.py"
    args_call = "python3 " + program_name + ' ' + passing_arg
    try:
        output = check_output(args_call, shell=True)
        output = output.decode().split('\n')
        print("Output of the Speech_Start_End.py Program : ", output)

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_speak_start_end function.")


def process_face_detection():
    program_name = "Face_Detection_Camera.py"
    args_call = "python3 " + program_name
    detect_id = None
    try:
        output = check_output(args_call, shell=True)
        output = output.decode().split('\n')
        print("Output of the Face_Detection_Camera.py program : ", output)
        detect_name = output[1]
        if detect_name[:5] == "ERROR":
            detect_name = "UNKNOWN"
            detect_id = None

        if detect_name == "UNKNOWN":
            print("Hello Unknown")
        else:
            under_position = detect_name.find("_")
            detect_id = detect_name[under_position+1:]
            detect_name = detect_name[:under_position]

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_face_detection function.")
        detect_name = "UNKNOWN"
        detect_id = None

    return detect_name, detect_id


def process_inserting_data():
    try:
        program_name = "Customer_Insert.py"
        args_call = "python3 " + program_name
        output = check_output(args_call, shell=True)
        try:
            output = output.decode().split('\n')
            print("Output of the Customer_Insert.py program : ", output)
            try:
                match = [element for element in output if "Unique_ID" in element]
                unique_id = match[0]
                colon_position = unique_id.find(":")
                unique_id = unique_id[colon_position + 3:]

            except IndexError:
                print("ERROR : IndexError - You didn't enter your details dor database - "
                      "inside process_inserting_data function.")
                check_output(
                    ["zenity", "--info", "--width=400", "--height=200", "--text=We cannot save your details"])
                unique_id = None

        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_inserting_data function.")
            unique_id = None

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_inserting_data function.")
        unique_id = None

    return unique_id


def process_picture(unique_id):
    program_name = "Capture_Picture_Main.py"
    passing_arg = str(unique_id)
    args_call = "python3 " + program_name + ' ' + passing_arg
    try:
        output = check_output(args_call, shell=True)
        output = output.decode().split('\n')
        print("Output of the Capture_Picture_Main.py program : ", output)
        output = output[5]
        if output[:5] == "ERROR":
            output = None

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_picture function.")
        output = None

    return output


def process_search_details():
    try:
        program_name = "Customer_Search_Main.py"
        args_call = "python3 " + program_name
        output = check_output(args_call, shell=True)
        print("Output of the Customer_Search_Main.py program : ", output)

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_search_details function.")


def process_search_all_details(check_region_table, detect_id):
    cur = None
    conn = None
    table_list = []
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT * from """ + check_region_table + """ where "ID" = '{}'; """.format(detect_id)
        cur.execute(query)
        row = cur.fetchall()
        if len(row) == 0:
            print("There are no data!!!!")
            table_list = None
        else:
            print("Data searched successfully!!!!")
            for list_details in row:
                total_tuple = list_details
                for tuple_details in total_tuple:
                    table_list.append(tuple_details)

        conn.commit()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_search_all_details function : " + str(error))
        conn = None
        cur = None
    finally:
        cur.close()
        conn.close()

    return table_list


def process_update_detail():
    try:
        program_name = "Customer_Update.py"
        args_call = "python3 " + program_name
        output = check_output(args_call, shell=True)
        print("Output of the Customer_Update.py program : ", output)

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_update_detail function.")


def process_unknown(main_directory, database_code_directory, face_recognition_code_directory,
                    speech_recognition_code_directory, detect_name, detect_id):
    passing_arg = "0"
    os.chdir(speech_recognition_code_directory)
    process_speak_start_end(passing_arg)
    os.chdir(main_directory)
    text = "Currently we don't have your details\n\nWould you like to save your details?"
    response = ask_question(text)
    if response is not None:
        os.chdir(database_code_directory)
        unique_id = process_inserting_data()
        os.chdir(main_directory)
        if unique_id is not None:
            os.chdir(face_recognition_code_directory)
            output_process_picture = process_picture(unique_id)
            os.chdir(main_directory)
            if output_process_picture is not None:
                ask_search(database_code_directory, main_directory, detect_name)
                ask_update(database_code_directory, main_directory, detect_name)
            else:
                ##detete code -- Here Code should delete the data from database and inform the customer.
                print("ERROR : UNKNOWN customer don't want to save picture. But details saved in dataBase.")
                ask_search(database_code_directory, main_directory, detect_name)
        else:
            print("INFO - {} customer don't want to save detail.".format(detect_name))
            ask_search(database_code_directory, main_directory, detect_name)
    else:
        print("INFO - {} customer don't want to save detail.".format(detect_name))
        ask_search(database_code_directory, main_directory, detect_name)


def process_known(main_directory, database_code_directory, face_recognition_code_directory,
                  speech_recognition_code_directory, detect_name, detect_id):
    print('Hello, {} {}'.format(detect_name, detect_id))
    passing_arg = detect_name.lower()
    os.chdir(speech_recognition_code_directory)
    process_speak_start_end(passing_arg)
    os.chdir(main_directory)
    os.chdir(database_code_directory)
    check_region_table = "carego_customer_dev"
    table_details = process_search_all_details(check_region_table, detect_id)
    os.chdir(main_directory)
    if table_details is not None:
        ask_search(database_code_directory, main_directory, detect_name)
        ask_update(database_code_directory, main_directory, detect_name)
    else:
        text = "Currently we don't have your correct details\n\nwould you like to save your details?"
        response = ask_question(text)
        if response is not None:
            os.chdir(database_code_directory)
            unique_id = process_inserting_data()
            os.chdir(main_directory)
            if unique_id is not None:
                text = "Your old ID was : " + detect_id + "\n\nYour new ID is : " + unique_id
                try:
                    check_output(["zenity", "--info", "--width=400", "--height=200", "--text=" + text])
                    os.chdir(face_recognition_code_directory)
                    image_path = 'Dataset'
                    os.chdir(image_path)
                    old_folder = detect_name + '_' + detect_id
                    new_folder = detect_name + '_' + unique_id
                    fix_pic_path = Path(old_folder)
                    if fix_pic_path.exists() is False:
                        print("ERROR : fix_pic_path.exists() is False : " + old_folder +
                              " Not present - inside main_process function. Could not able to "
                              "save the image data with new ID : ", str(unique_id))
                    else:
                        os.rename(old_folder, new_folder)
                        ask_search(database_code_directory, main_directory, detect_name)
                        ask_update(database_code_directory, main_directory, detect_name)
                except subprocess.CalledProcessError:
                    print("ERROR : subprocess.CalledProcessError - inside main_process function. "
                          "could not able to save the image data with new ID : ", str(unique_id))
                    ask_search(database_code_directory, main_directory, detect_name)
                    ask_update(database_code_directory, main_directory, detect_name)
            else:
                print("INFO - {} customer don't want to save detail.".format(detect_name))
                ask_search(database_code_directory, main_directory, detect_name)
        else:
            print("INFO - {} customer don't want to save detail.".format(detect_name))
            ask_search(database_code_directory, main_directory, detect_name)


def main_process(main_directory, database_code_directory, face_recognition_code_directory,
                 speech_recognition_code_directory):
    os.chdir(face_recognition_code_directory)
    detect_name, detect_id = process_face_detection()
    os.chdir(main_directory)
    if detect_name == "UNKNOWN":
        process_unknown(main_directory, database_code_directory, face_recognition_code_directory,
                        speech_recognition_code_directory, detect_name, detect_id)

    else:
        process_known(main_directory, database_code_directory, face_recognition_code_directory,
                      speech_recognition_code_directory, detect_name, detect_id)

    passing_arg = "1"
    os.chdir(speech_recognition_code_directory)
    process_speak_start_end(passing_arg)
    os.chdir(main_directory)


def main():
    main_directory = "/home/somak/Final-Project-Robotic-Greeter/carego_project/development/"
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Main_Process.py - at : ' + current_time + ' on : ' + current_date)

    os.chdir(main_directory)
    database_code_directory, face_recognition_code_directory, speech_recognition_code_directory = checking_directory()

    main_process(main_directory, database_code_directory, face_recognition_code_directory,
                 speech_recognition_code_directory)
    os.chdir(main_directory)

    exit_program()


if __name__ == "__main__":
    main()
