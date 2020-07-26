#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Capture_Picture_Main.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Capture_Picture_Main.py program will be called from Main_Process.py. It will receive one input argument
#               (Unique ID) from the main process, and based on the input argument, it will call to
#               Capture_Picture_Save.py for taking and saving the picture. This process is a looping process that asks
#               the user if he want to take multiple pictures and save it.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Capture_Picture_Main.py
# **********************************************************************************************************************
"""

import sys
import subprocess
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
    print('Starting program : Capture_Picture_Main.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Capture_Picture_Main.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_ask_question(flag):
    """
    ************************************ Inside process_ask_question function ******************************************
    This function is the initial step to ask the user if they want to take photos or not.

    It will ask by prompting a pop-up message, and in the pop-up message, users can click on YES or NO button.
    Based on the response, it will return it for the next function. This function receives an input flag, for the
    first time, the value of the flag will be 1, and after all the process flag sets as two, and this function will
    get called again. This time will ask if they want to take another photo or not. If this function cannot prompt
    the pop-up message, it will exit from the program.
    ************************************ Inside process_ask_question function ******************************************
    """

    response = None
    if flag == 1:
        args = "zenity --question --width=500 --height=250 --text='Do you want me to take your picture?'"
    else:
        args = "zenity --question --width=500 --height=250 --text='Do you want me to take your another picture?'"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_ask_question function.")
        exit_program()

    return response


def process_calling(passing_arg):
    """
    ************************************ Inside process_calling function ***********************************************
    This function is to call Capture_Picture_Save.py based on user response.

    It will first call process_ask_question function, and based on the user response; this will call one python process
    Capture_Picture_Save.py, to save the picture. This function is written inside a loop until the user decides not to
    take any more pictures.
    ************************************ Inside process_calling function ***********************************************
    """

    flag = 1
    response = process_ask_question(flag)
    status = 0
    if len(response) == 0:
        print("Calling program : Capture_Picture_Save.py......")
        args_call = "python3 Capture_Picture_Save.py" + ' ' + passing_arg
        output = check_output(args_call, shell=True)
        try:
            output = output.decode().split('\n')
            try:
                match = [element for element in output if ".jpg" in element]
                if len(match) > 0:
                    flag = 2
                else:
                    print("ERROR : I cannot take your picture currently - inside process_calling function.")
                    check_output(
                        ["zenity", "--info", "--width=400", "--height=200", "--text=I cannot take your "
                                                                            "picture currently !!!!"])
            except IndexError:
                print("ERROR : IndexError - I cannot take your picture currently - inside process_calling function.")
                check_output(["zenity", "--error", "--width=400", "--height=200", "--text=I cannot take your picture "
                                                                                  "currently !!!!"])
                exit_program()

        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside  process_calling function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=I cannot take your picture "
                                                                              "currently. \n\nPlease contact "
                                                                              "Admin !!!!"])
            exit_program()

    while status == 0:
        response = process_ask_question(flag)
        if len(response) == 0:
            print("Calling program : Capture_Picture_Save.py......")
            args_call = "python3 Capture_Picture_Save.py" + ' ' + passing_arg
            output = check_output(args_call, shell=True)
            try:
                output = output.decode().split('\n')
                try:
                    match = [element for element in output if ".jpg" in element]
                    if len(match) > 1:
                        flag = 2
                    else:
                        print("ERROR : I cannot take your picture currently - inside process_calling function.")
                        check_output(
                            ["zenity", "--info", "--width=400", "--height=200", "--text=I cannot take your "
                                                                                "picture currently !!!!"])
                        exit_program()

                except IndexError:
                    print("ERROR : IndexError - I cannot take your picture currently - "
                          "inside process_calling function.")
                    check_output(
                        ["zenity", "--error", "--width=400", "--height=200", "--text=I cannot take your picture "
                                                                             "currently !!!!"])
                    exit_program()

            except subprocess.CalledProcessError:
                print("ERROR : subprocess.CalledProcessError - inside process_calling function.")
                check_output(["zenity", "--error", "--width=400", "--height=200", "--text=I cannot take your picture "
                                                                                  "currently. \n\nPlease contact "
                                                                                  "Admin !!!!"])
                exit_program()

        else:
            status = 1

    exit_program()


def process_check_input_argument():
    """
    ************************************ Inside process_check_input_argument function **********************************
    This function will decide if this program will run as stand-alone or not.

    It will receive an input argument (Unique ID) from the Main_Process and pass the Unique ID to the main
    process_calling function. If this function does not receive any argument, it will pass "0" as an argument.
    ************************************ Inside process_check_input_argument function **********************************
    """

    try:
        print('Processing Capture_Picture_Main.py from main process.')
        print('Inside Capture_Picture_Main.py - Unique ID is : ', sys.argv[1])
        passing_arg = sys.argv[1]
        process_calling(passing_arg)
    except IndexError:
        print('Processing Capture_Picture_Main.py stand alone')
        passing_arg = "0"
        process_calling(passing_arg)


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    process_check_input_argument()
    exit_program()


if __name__ == "__main__":
    main()
