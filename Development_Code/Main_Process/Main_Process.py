#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Main_Process.py
# Author:       Somak Mukherjee
# Date:         Friday 24 May, 2020
# Version:      1
# **********************************************************************************************************************
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
# **********************************************************************************************************************
# NOTE 1 :      Please make sure to change the region value as per region wise before putting to server :
#               Development region : "DEV"
#               Test region : "TEST"
#               Production region : "PROD"
#
#               Check in the following function :
#               process_parameter_set():
#                    region = "DEV"
# **********************************************************************************************************************
# NOTE 2 :      In the program there are one main directory in process_parameter_set():
#               main_directory = "/home/somak/Robotic-Greeter/Development/"
#               Please make sure to change or validate before putting ii into Production.
# **********************************************************************************************************************
# NOTE 3 :      This program can be run separately or as a stand alone program as follow :
#               $ python3 Main_Process.py
# **********************************************************************************************************************
"""
import os
import sys
import glob
import psycopg2
import subprocess
from pathlib import Path
from datetime import date, datetime
from subprocess import check_output


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
    print('Starting program : Main_Process.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Main_Process.py - At: ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. Region = "DEV" signifies that we are running the code in the development region. And as per the region value,
    this program will choose the table. So, it is essential to set region value correctly.
    2. main_directory = "/home/somak/Robotic-Greeter/Development_Code" signifies that we are assigning this directory
    as main_directory, because Development_Code folder has all the other codes to run this process.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    region = "DEV"
    main_directory = "/home/somak/Robotic-Greeter/Development_Code"

    return region, main_directory


def process_checking_region_table(region):
    """
    ************************************ Inside process_checking_region_table function *********************************
    Function to get the table details.

    This function will be called to get main_table and sequence_table as per region value. If the region value is not
    set correctly, then this function will print error message and will exit from the program.
    ************************************ Inside process_checking_region_table function *********************************
    """

    main_table = None
    sequence_table = None
    if region == "DEV":
        main_table = "carego_customer_dev"
        sequence_table = "carego_customer_dev_ID_seq"
    elif region == "TEST":
        main_table = "carego_customer_test"
        sequence_table = "carego_customer_dev_ID_seq"
    elif region == "PROD":
        main_table = "carego_customer_prod"
        sequence_table = "carego_customer_dev_ID_seq"
    else:
        print("ERROR : REGION VALUE NOT FOUND. Please check the REGION value inside the program - "
              "inside process_checking_region_table function.")
        exit_program()

    return main_table, sequence_table


def process_checking_directory():
    """
    ************************************ Inside process_checking_directory function ************************************
    Function to validate all directory.

    This function will be called to check if codes related folder such as Database_Code, Face_Recognition_Code,
    and Speech_Recognition_Code is present inside of Main_Directory or not. If the directory is not present, then this
    function will give error and will exit from the program.
    ************************************ Inside process_checking_directory function ************************************
    """

    database_code_directory = Path("Database_Code")
    face_recognition_code_directory = Path("Face_Recognition_Code")
    speech_recognition_code_directory = Path("Speech_Recognition_Code")

    if database_code_directory.exists() is False:
        print("ERROR : Directory : Database_Code is not present - inside process_checking_directory function.")
        exit_program()
    elif face_recognition_code_directory.exists() is False:
        print("ERROR : Directory : Face_Recognition_Code is not present - inside process_checking_directory function.")
        exit_program()
    elif speech_recognition_code_directory.exists() is False:
        print("ERROR : Directory : Speech_Recognition_Code is not present - inside process_checking_directory "
              "function.")
        exit_program()
    else:
        pass

    return database_code_directory, face_recognition_code_directory, speech_recognition_code_directory


def process_speech_normal(text):
    """
    ************************************ Inside process_speech_normal function *****************************************
    Function to call Speech_Normal.py.

    This function will receive a text as input and will pass this input as passing argument to Speech_Normal.py. Which
    will convert text to speech with the gTTS. Speech_Normal.py will only speak from the text message. This function
    will only call Speech_Normal.py and will not receive any output from Speech_Normal.py. If it is not able to call
    Speech_Normal.py, it will print an error message and will continue.
    ************************************ Inside process_speech_normal function *****************************************
    """

    passing_arg = text
    program_name = "Speech_Normal.py"
    args_call = "python3 " + program_name + ' ' + passing_arg
    try:
        check_output(args_call, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_speech_normal function.")


def process_speech_question(text):
    """
    ************************************ Inside process_speech_question function ***************************************
    Function to call Speech_Question.py.

    This function will receive a text as input and will pass this input as passing argument to Speech_Question.py.
    Which will convert text to speech with gTTS. Text has to be question format since Speech_Question.py will first
    ask the user and receive a response from the user. If it is not able to call Speech_Normal.py, it will print an
    error message and will continue. This function will then check if Speech_Question_Output.txt is present and will
    read from it for the response and return it. If the output file does not exist, then it will return the response
    as None.
    ************************************ Inside process_speech_question function ***************************************
    """

    passing_arg = text
    program_name = "Speech_Question.py"
    args_call = "python3 " + program_name + ' ' + passing_arg
    try:
        check_output(args_call, shell=True)
        try:
            with open("Speech_Question_Output.txt", "r") as file:
                response = file.readline()
        except EOFError:
            print("ERROR : EOFError - Speech_Question_Output.txt,  has no data")
            response = None
        except FileNotFoundError:
            print("ERROR : FileNotFoundError - Speech_Question_Output.txt, is not present")
            response = None
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_speech_question function.")
        response = None

    return response


def process_speech_name_organization():
    """
    ************************************ Inside process_speech_name_organization function ******************************
    Function to call Speech_Name_Organization.py.

    Which will first ask your name, company, and then will ask if you want to save details or not. If it is not able
    to call Speech_Normal.py, it will print an error message and will continue.
    Based on your response, this function will check Speech_Name_Organization_Output.txt present or not and read the
    file for the response. Then it will return the response, and if the output file is not present, then it will return
    the response as None.
    ************************************ Inside process_speech_name_organization function ******************************
    """

    program_name = "Speech_Name_Organization.py"
    passing_arg = 0
    args_call = "python3 " + program_name + ' ' + str(passing_arg)
    try:
        output = check_output(args_call, shell=True)
        output = output.decode().split('\n')
        print("Output of the Speech_Name_Organization Program : ", output)
        try:
            with open("Speech_Name_Organization_Output.txt", "r") as file:
                response = file.readline()
        except EOFError:
            print("ERROR : EOFError - Speech_Name_Organization_Output.txt,  has no data")
            response = None
        except FileNotFoundError:
            print("ERROR : FileNotFoundError - Speech_Name_Organization_Output.txt, is not present")
            response = None
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_speech_name_organization function.")
        response = None

    return response


def process_prompt_question(text):
    """
    ************************************ Inside process_prompt_question function ***************************************
    Function to prompt a pop-up question.

    It will receive a text as input and will prompt the same text pop-up message to the user. Later, it will store
    the user response into output variable and will return the same. If this function cannot able to run the pop-up,
    then it will return output as None.
    ************************************ Inside process_prompt_question function ***************************************
    """

    try:
        output = check_output(["zenity", "--question", "--width=400", "--height=200", "--text=" + text])
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_ask_question function.")
        output = None

    return output


def process_inserting_data():
    """
    ************************************ Inside process_inserting_data function ****************************************
    Function to call Customer_Insert.py.

    Which will insert the data into the database. This process will receive an output from Customer_Insert.py to get
    Unique ID and later return the Unique ID. If it is not able to call or have an issue with extracting Unique ID,
    then it will print an error message and will return the Unique ID as None.
    ************************************ Inside process_inserting_data function ****************************************
    """

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
                print("ERROR : IndexError - You did not enter your details dor database - "
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
    """
    ************************************ Inside process_picture function ***********************************************
    Function to call Capture_Picture_Main.py

    This function will call Capture_Picture_Main with Unique ID as input, which is used to take and save your picture.
    This process will also receive an output from Capture_Picture_Main.py to check if there are any errors or not. If
    there are errors, then it will print an error message and will return None or else will return the original output
    value.
    ************************************ Inside process_picture function ***********************************************
    """

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
    """
    ************************************ Inside process_search_details function ****************************************
    Function to call Customer_Search_Main.py..

    Which will search the data from table. If it is not able to call, then it will print an error message and will
    continue.
    ************************************ Inside process_search_details function ****************************************
    """

    try:
        program_name = "Customer_Search_Main.py"
        args_call = "python3 " + program_name
        output = check_output(args_call, shell=True)
        print("Output of the Customer_Search_Main.py program : ", output)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_search_details function.")


def process_ask_search(detect_name):
    """
    ************************************ Inside process_ask_search function ********************************************
    Function to call process_prompt_question() function with text as input.

    First, this function will call process_prompt_question() function to get the response from the user and based on
    the response this function will call process_search_details() function.
    ************************************ Inside process_ask_search function ********************************************
    """

    text = "Would you like to proceed?"
    response = process_prompt_question(text)
    if response is not None:
        process_search_details()
        print("INFO - {} customer searched someone.".format(detect_name))
    else:
        print("INFO - {} customer does not want to search someone.".format(detect_name))


def process_search(text, database_code_directory, main_directory, detect_name, search_flag,
                   speech_recognition_code_directory):
    """
    ************************************ Inside process_search function ************************************************
    Main search function.

    This function will call process_speech_question() function with an input text and based on the response it will call
    process_speech_normal(text) function and process_ask_search(detect_name) function. If the customer says "Yes" then
    it will set search_flag as Yes and will return it, if not then will return as None.
    ************************************ Inside process_search function ************************************************
    """

    os.chdir(speech_recognition_code_directory)
    response = process_speech_question(text)
    os.chdir(main_directory)

    if response == "YES":
        print("INFO - {} customer wants to search someone.".format(detect_name))

        os.chdir(speech_recognition_code_directory)
        text = "There will be some pop up message will appear. Please follow it."
        process_speech_normal(text)
        os.chdir(main_directory)

        os.chdir(database_code_directory)
        process_ask_search(detect_name)
        search_flag = "YES"
        os.chdir(main_directory)

    else:
        print("INFO - {} customer does not want search someone.".format(detect_name))

    return search_flag


def process_update_detail():
    """
    ************************************ Inside process_update_detail function *****************************************
    Function to call Customer_Update.py

    Which will update the data in the table. If it is not able to call, then it will print an error message and will
    continue.
    ************************************ Inside process_update_detail function *****************************************
    """

    try:
        program_name = "Customer_Update.py"
        args_call = "python3 " + program_name
        output = check_output(args_call, shell=True)
        print("Output of the Customer_Update.py program : ", output)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_update_detail function.")


def process_ask_update(detect_name):
    """
    ************************************ Inside process_ask_update function ********************************************
    Function to call process_prompt_question() function with text as input.

    First, this function will call process_prompt_question() function to get the response from the user and based on
    the response this function will call process_update_detail() function.
    ************************************ Inside process_ask_update function ********************************************
    """

    text = "Would you like to update your details?"
    response = process_prompt_question(text)
    if response is not None:
        process_update_detail()
        print("INFO - {} customer updated detail.".format(detect_name))
    else:
        print("INFO - {} customer does not want to update detail.".format(detect_name))


def process_update(text, database_code_directory, main_directory, detect_name, speech_recognition_code_directory):
    """
    ************************************ Inside process_search function ************************************************
    Main update function.

    This function will call process_speech_question() function with text as input and based on the response it will call
    process_speech_normal(text) function and process_ask_update(detect_name) function.
    ************************************ Inside process_search function ************************************************
    """

    os.chdir(speech_recognition_code_directory)
    response = process_speech_question(text)
    os.chdir(main_directory)

    if response == "YES":
        print("INFO - {} customer wants to update details.".format(detect_name))

        os.chdir(speech_recognition_code_directory)
        text = "There will be some pop up message will appear. Please follow it."
        process_speech_normal(text)
        os.chdir(main_directory)

        os.chdir(database_code_directory)
        process_ask_update(detect_name)
        os.chdir(main_directory)

    else:
        print("INFO - {} customer does not want to update details.".format(detect_name))


def process_search_all_details(check_main_table, detect_id):
    """
    ************************************ Inside process_search function ************************************************
    Function to search ID from the table.

    This function will search the details of a known person with the ID. After the face detection function, if the
    face is known, with face ID, this function will check if the ID is present in the table. If details exist, then it
    will return the table details, if not, then it will return an empty list.
    ************************************ Inside process_search function ************************************************
    """

    cur = None
    conn = None
    table_list = []
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT * from """ + check_main_table + """ where "ID" = '{}'; """.format(detect_id)
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


def process_unknown(main_directory, database_code_directory, face_recognition_code_directory,
                    speech_recognition_code_directory, detect_name):
    """
    ************************************ Inside process_unknown function ***********************************************
    Main function for unknown user.

    This function is the primary process for an unknown person. This function will first greet the unknown person and
    later will ask if the person needs any help or not. Based on the response (Yes/No), this process will do as below:
    1. If Yes, it will ask if the customer wants to save their details in the database and save their picture.
    Also, it will ask if they want to search anyone or update their details.
    2. If No, then it will exit from this function and continue with the rest of the process.
    ************************************ Inside process_unknown function ***********************************************
    """

    search_flag = None
    help_flag = None

    os.chdir(speech_recognition_code_directory)
    text = "Hello, Welcome to Care Go, my name is TELIA. I am Care Go’s virtual greeter. I am going to ask few " \
           "question to you. You can answer with Yes or No. If I do not get an input from you within 5 second then I " \
           "will prompt a pop up message to you."
    process_speech_normal(text)
    os.chdir(main_directory)

    os.chdir(speech_recognition_code_directory)
    text = "Do you need any help?"
    response = process_speech_question(text)
    os.chdir(main_directory)

    if response == "YES":
        print("INFO - {} customer wants help.".format(detect_name))
        help_flag = "YES"

        os.chdir(speech_recognition_code_directory)
        response = process_speech_name_organization()
        os.chdir(main_directory)

        if response == "YES":
            print("INFO - {} customer wants to save detail.".format(detect_name))

            os.chdir(speech_recognition_code_directory)
            text = "There will be some pop up message will appear. Please follow it."
            process_speech_normal(text)
            os.chdir(main_directory)

            text = "Would you like to proceed to save your details?"
            response = process_prompt_question(text)

            if response is not None:
                print("INFO - {} customer wants to save detail.".format(detect_name))

                os.chdir(database_code_directory)
                unique_id = process_inserting_data()
                os.chdir(main_directory)

                if unique_id is not None:
                    print("INFO - {} customer saved detail with unique ID.".format(detect_name))

                    os.chdir(speech_recognition_code_directory)
                    text = "Okay. I hope you have noted your unique ID. Now we are going to take your picture, " \
                           "so that we can recognize you from next time."
                    process_speech_normal(text)
                    os.chdir(main_directory)

                    os.chdir(face_recognition_code_directory)
                    output_process_picture = process_picture(unique_id)
                    os.chdir(main_directory)

                    if output_process_picture is not None:
                        print("INFO - {} customer saved Picture.".format(detect_name))

                        text = "Okay. Thank you for saving your picture. Are you looking for someone here?"
                        search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                     search_flag, speech_recognition_code_directory)

                        text = "Do you like to update or modify your details?"
                        process_update(text, database_code_directory, main_directory, detect_name,
                                       speech_recognition_code_directory)

                    else:
                        print("INFO - {} customer does not want to save picture.".format(detect_name))

                        text = "Okay. Since you do not want to save picture, are you looking for someone here?"
                        search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                     search_flag, speech_recognition_code_directory)

                else:
                    print("INFO - {} customer wants to save detail but Unique ID was not created.".format(detect_name))

                    text = "We could not save your details. Are you looking for someone here?"
                    search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                 search_flag, speech_recognition_code_directory)

            else:
                print("INFO - {} customer wants help but does not want to save detail.".format(detect_name))

                text = "Okay. Since you do not want to save your details, are you looking for someone here?"
                search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                             search_flag, speech_recognition_code_directory)

        else:
            print("INFO - {} customer wants help but does not want to save detail.".format(detect_name))

            text = "Okay. Since you do not want to save your details, are you looking for someone here?"
            search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                         search_flag, speech_recognition_code_directory)

    else:
        print('INFO - {} Customer does not want any help'.format(detect_name))

    return search_flag, help_flag


def process_known(main_directory, database_code_directory, face_recognition_code_directory,
                  speech_recognition_code_directory, detect_name, detect_id, check_main_table):
    """
    ************************************ Inside process_known function *************************************************
    Main function for known user.

    This function is the primary process for a known person. This function will first greet the unknown person and
    later will ask if the person needs any help or not. Based on the response (Yes/No), this process will do as below:
    1. If Yes, it will ask if the customer wants to search anyone or update their details.
    2. If No, then it will exit from this function and continue with the rest of the process.
    ************************************ Inside process_known function *************************************************
    """

    help_flag = None
    search_flag = None

    os.chdir(speech_recognition_code_directory)
    text = "Hello " + detect_name.lower() + ". Welcome to Care Go, do you remember me, TELIA, Care Go’s virtual " \
                                            "greeter?"
    process_speech_normal(text)
    os.chdir(main_directory)

    os.chdir(speech_recognition_code_directory)
    text = detect_name.lower() + " Do you need any help?"
    response = process_speech_question(text)
    os.chdir(main_directory)

    if response == "YES":
        print("INFO - {} customer wants help.".format(detect_name))
        help_flag = "YES"

        os.chdir(database_code_directory)
        table_details = process_search_all_details(check_main_table, detect_id)
        os.chdir(main_directory)

        if table_details is not None:
            print("INFO - {} needs help and customer details present in the table.".format(detect_name))

            text = "Okay " + detect_name.lower() + ". Are you looking for someone here?"
            search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                         search_flag, speech_recognition_code_directory)

            text = "Okay " + detect_name.lower() + ". Do you like to update or modify your details?"
            process_update(text, database_code_directory, main_directory, detect_name,
                           speech_recognition_code_directory)

        else:
            print("INFO - {} needs help but customer details are not present in the table.".format(detect_name))

            os.chdir(speech_recognition_code_directory)
            text = "Currently we do not have your correct details. would you like to save your details?"
            response = process_speech_question(text)
            os.chdir(main_directory)

            if response == "YES":
                text = "Do you want to proceed?"
                response = process_prompt_question(text)

                if response is not None:
                    print("INFO - {} customer wants to save details in the database")

                    os.chdir(database_code_directory)
                    unique_id = process_inserting_data()
                    os.chdir(main_directory)

                    if unique_id is not None:
                        print("INFO - {} customer creates new unique ID in the database")

                        text = "Your old ID was : " + detect_id + "\n\nYour new ID is : " + unique_id
                        try:
                            print("Renaming the old ID dataset directory with new ID dataset")

                            check_output(["zenity", "--info", "--width=400", "--height=200", "--text=" + text])

                            os.chdir(face_recognition_code_directory)
                            image_path = 'Dataset'
                            os.chdir(image_path)

                            old_folder = detect_name + '_' + detect_id
                            new_folder = detect_name + '_' + unique_id
                            fix_pic_path = Path(old_folder)

                            if fix_pic_path.exists() is False:
                                print("ERROR : " + old_folder + " is not present - inside process_known function. "
                                                                "Could not able to save the image data with new ID : ",
                                      str(unique_id))

                            else:
                                os.rename(old_folder, new_folder)
                                print(old_folder + " is present and saving the image data with new ID : ",
                                      str(unique_id))

                                os.chdir(main_directory)

                                text = "Okay " + detect_name.lower() + ". Are you looking for someone here?"
                                search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                             search_flag, speech_recognition_code_directory)

                                process_update(text, database_code_directory, main_directory, detect_name,
                                               speech_recognition_code_directory)

                        except subprocess.CalledProcessError:
                            print("ERROR : subprocess.CalledProcessError - inside process_known function. "
                                  "could not able to save the image data with new ID : ", str(unique_id))

                            text = "Okay " + detect_name.lower() + ". Are you looking for someone here?"
                            search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                         search_flag, speech_recognition_code_directory)

                            text = "Okay " + detect_name.lower() + ". Do you like to update or modify your details?"
                            process_update(text, database_code_directory, main_directory, detect_name,
                                           speech_recognition_code_directory)

                    else:
                        print("INFO - {} customer does not want to save detail.".format(detect_name))

                        text = "Okay " + detect_name.lower() + ". Are you looking for someone here?"
                        search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                     search_flag, speech_recognition_code_directory)

                else:
                    print("INFO - {} customer does not want to save detail.".format(detect_name))

                    text = "Okay " + detect_name.lower() + ". Are you looking for someone here?"
                    search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                                 search_flag, speech_recognition_code_directory)
            else:
                print("INFO - {} customer does not want to save detail.".format(detect_name))

                text = "Okay " + detect_name.lower() + ". Are you looking for someone here?"
                search_flag = process_search(text, database_code_directory, main_directory, detect_name,
                                             search_flag, speech_recognition_code_directory)

    else:
        print("INFO - {} customer does not want help.".format(detect_name))

    return search_flag, help_flag


def process_face_detection():
    """
    ************************************ Inside process_face_detection function ****************************************
    Function to call Face_Detection_Camera.py

    Which will detect the faces with the detect_name and detect_id. detect_name and detect_id will be Unknown, and None
    if the faces are not known. If it is a known face, then will return the exact name and ID. If it is not able to
    call then it will print an error message and will continue.
    ************************************ Inside process_face_detection function ****************************************
    """

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
            print('Hello, {} {}'.format(detect_name, detect_id))
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_face_detection function.")
        detect_name = "UNKNOWN"
        detect_id = None

    return detect_name, detect_id


def process_speech_emergency_evacuation_procedures():
    """
    ************************************ Inside process_speech_emergency_evacuation_procedures function ****************
    Function to call Speech_Emergency_Evacuation_Procedures.py.

    Which will explain the emergency evacuation procedures to the user. For the unknown user it will be mandatory but
    for the known user, this function will ask if the user wants to see this procedures again or not. If the user says
    Yes then this function will call Speech_Emergency_Evacuation_Procedures.py or else not. If it is not able to call
    then it will print an error message and will continue.
    ************************************ Inside process_speech_emergency_evacuation_procedures function ****************
    """

    try:
        program_name = "Speech_Emergency_Evacuation_Procedures.py"
        args_call = "python3 " + program_name
        check_output(args_call, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_speech_emergency_evacuation_procedures function.")


def process_main(main_directory, database_code_directory, face_recognition_code_directory,
                 speech_recognition_code_directory, check_main_table):
    """
    ************************************ Inside process_main function **************************************************
    This the main function.

    This function is the main function and first, this will perform face_detection and based on the detect name this
    will call process_unknown or process_known function. Later, this process will do some extra feature.
    ************************************ Inside process_main function **************************************************
    """

    os.chdir(face_recognition_code_directory)
    detect_name, detect_id = process_face_detection()
    os.chdir(main_directory)
    if detect_name == "UNKNOWN":
        search_flag, help_flag = process_unknown(main_directory, database_code_directory,
                                                 face_recognition_code_directory, speech_recognition_code_directory,
                                                 detect_name)

    else:
        search_flag, help_flag = process_known(main_directory, database_code_directory,
                                               face_recognition_code_directory, speech_recognition_code_directory,
                                               detect_name, detect_id, check_main_table)

    os.chdir(speech_recognition_code_directory)
    if search_flag is not None:
        text = "Wonderful, I hope you got the information you were looking."
        process_speech_normal(text)

    if help_flag is not None:
        if detect_name == "UNKNOWN":
            print("Showing Emergency Evacuation Procedures to Unknown")
            process_speech_emergency_evacuation_procedures()
        else:
            text = detect_name.lower() + " Do you want to see Emergency Evacuation Procedures again?"
            response = process_speech_question(text)
            if response == "YES":
                print("Showing Emergency Evacuation Procedures to {}".format(detect_name))
                process_speech_emergency_evacuation_procedures()

        text = "Do you want to know more about me as TELIA?"
        response = process_speech_question(text)
        if response == "YES":
            text = "Did you know that I am named after TELIA, our forward thinking optimization and automation " \
                   "system that maximizes storage capacity, increases productivity, improves facility throughput " \
                   "all under the control of a safety critical environment."
            process_speech_normal(text)

            text = "And did you know we have installed TELIA as a system in 3 countries, it controls over 100 " \
                   "automated assets including more than 25 cranes, at 12 different sites for steel coil, long " \
                   "products and finished goods. We are always innovating as we have 13 patents or pending patents " \
                   "and more than 50 projects."
            process_speech_normal(text)

            text = "You are probably wondering why CareGo would create me to greet you? I am to remind you that we " \
                   "are a technology company which is obsessed with innovation, we try to improve everything from " \
                   "our team to our processes to our products and how we greet you at the door. We not only embrace " \
                   "innovation, we were born from it. Speaking of innovators."
            process_speech_normal(text)

    text = "Can I have you sign our visitor sheet on my notepad here? Thanks for doing that."
    process_speech_normal(text)

    text = "Thank you for visiting Care Go. Please check out our web-site newsletter. Bye. See you later."
    process_speech_normal(text)
    os.chdir(main_directory)


def process_delete_mp3_output_files(speech_recognition_code_directory):
    """
    ************************************ Inside process_delete_mp3_output_files function *******************************
    This function will be called to delete all mp3 and output files before to end of the program.
    ************************************ Inside process_delete_mp3_output_files function *******************************
    """

    os.chdir(speech_recognition_code_directory)
    mp3_files = glob.glob('*.mp3', recursive=True)
    output_files = glob.glob('*_Output.txt', recursive=True)
    for files in mp3_files:
        try:
            os.remove(files)
            print("Deleting mp3 files")
        except OSError:
            print("Cannot delete the old mp3 files.")

    for files in output_files:
        try:
            os.remove(files)
            print("Deleting output files")
        except OSError:
            print("Cannot delete the old output text files.")


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    region, main_directory = process_parameter_set()
    check_main_table, check_sequence_table = process_checking_region_table(region)

    os.chdir(main_directory)
    database_code_directory, face_recognition_code_directory, speech_recognition_code_directory = \
        process_checking_directory()

    process_main(main_directory, database_code_directory, face_recognition_code_directory,
                 speech_recognition_code_directory, check_main_table)

    os.chdir(main_directory)
    process_delete_mp3_output_files(speech_recognition_code_directory)
    os.chdir(main_directory)
    exit_program()


if __name__ == "__main__":
    main()
