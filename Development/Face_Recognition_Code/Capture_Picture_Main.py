#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Capture_Picture_Main.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Capture_Picture_Main.py program will be called from Main_Process.py (~/Main_Process/Main_Process.py)
#               It will receive one input argument (Unique ID) from the main process and based on the input argument,
#               it will call to ~/Face_Recognition_Code/Capture_Picture_Save.py for taking and saving the picture.
#               This process is a looping process that asks the user if he want to take multiple pictures and save it.
#
# NOTE:         This program can be run separately or as a stand-alone program as follow:
#               >> python3 Capture_Picture_Main.py

import sys
import subprocess
from datetime import date, datetime
from subprocess import check_output


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Capture_Picture_Main.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def ask_question(flag):
    response = None
    if flag == 1:
        args = "zenity --question --width=500 --height=250 --text='Do you want us to take your picture?' 2>/dev/null"
    else:
        args = "zenity --question --width=500 --height=250 --text='Do you want to take another picture?' 2>/dev/null"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside ask_question function.")
        exit_program()

    return response


def process_calling(passing_arg):
    flag = 1
    response = ask_question(flag)
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
                    print("ERROR : We cannot take your picture currently - inside process_calling function.")
                    check_output(
                        ["zenity", "--info", "--width=400", "--height=200", "--text=We cannot take your "
                                                                            "picture currently !!!!"])
                    exit_program()
            except IndexError:
                print("ERROR : IndexError - We cannot take your picture currently - inside process_calling function.")
                check_output(["zenity", "--error", "--width=400", "--height=200", "--text=We cannot take your picture "
                                                                                  "currently !!!!"])
                exit_program()

        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside  process_calling function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=We cannot take your picture "
                                                                              "currently. \n\nPlease contact "
                                                                              "Admin !!!!"])
            exit_program()

    while status == 0:
        response = ask_question(flag)
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
                        print("ERROR : We cannot take your picture currently - inside process_calling function.")
                        check_output(
                            ["zenity", "--info", "--width=400", "--height=200", "--text=We cannot take your "
                                                                                "picture currently !!!!"])
                        exit_program()

                except IndexError:
                    print("ERROR : IndexError - We cannot take your picture currently - "
                          "inside process_calling function.")
                    check_output(
                        ["zenity", "--error", "--width=400", "--height=200", "--text=We cannot take your picture "
                                                                             "currently !!!!"])
                    exit_program()

            except subprocess.CalledProcessError:
                print("ERROR : subprocess.CalledProcessError - inside process_calling function.")
                check_output(["zenity", "--error", "--width=400", "--height=200", "--text=We cannot take your picture "
                                                                                  "currently. \n\nPlease contact "
                                                                                  "Admin !!!!"])
                exit_program()

        else:
            status = 1

    exit_program()


def main():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Capture_Picture_Main.py - at : ' + current_time + ' on : ' + current_date)
    try:
        print('Processing Capture_Picture_Main.py from main process.')
        print('Inside Capture_Picture_Main.py - Unique ID is : ', sys.argv[1])
        passing_arg = sys.argv[1]
        process_calling(passing_arg)
    except IndexError:
        print('Processing Capture_Picture_Main.py stand alone')
        passing_arg = "0"
        process_calling(passing_arg)

    exit_program()


if __name__ == "__main__":
    main()
