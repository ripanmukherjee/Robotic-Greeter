#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Search_Main.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# ----------------------------------------------------------------------------------------------------------------------
# Description:  Customer_Search_Main.py is used to search the customer's data, and it will be called from
#               ~/Main_Process/Main_Process.py. If the customer wants to explore the data, then this process will ask
#               to the customer wants to search by ID or Name, and as per the selection this program will call the
#               below two program:
#               1. Customer_Search_ID.py
#               2. Customer_Search_Name.py
# ---------------------------------------------------------------------------------------------------------------------
# NOTE 1:         This program can be run separately or as a stand-alone program as follow:
#               >> python3 Customer_Search_Main.py
# ----------------------------------------------------------------------------------------------------------------------

import sys
import subprocess
from datetime import date, datetime
from subprocess import check_output, call


def start_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Customer_Search_Main.py - at : ' + current_time + ' on : ' + current_date)


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Customer_Search_Main.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_ask_question(flag):
    response = None
    if flag == 1:
        args = "zenity --info --width=500 --height=250 --text='You can search by ID or Name. \n\n" \
               "Do you want to proceed?'"
    else:
        args = "zenity --question --width=500 --height=250 --text='Do you want to search another people?'"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_ask_question function.")

    return response


def process_get_details():
    details = None
    args = "zenity --list --width=500 --height=250 --title='List of search' \
    --column='Option' --column='Description' \
    1 'Search by ID' \
    2 'Search by First Name or Last Name'"

    try:
        details = check_output(args, shell=True)
        details = details.decode().split('|')
        details = details[0].strip()
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details function.")

    return details


def process_call_program(details):
    try:
        if details == "1":
            print("Selected option : ID")
            print("Calling program : Customer_Search_ID.py......")
            args_call = "python3 Customer_Search_ID.py"
            try:
                call(args_call, shell=True)
            except subprocess.CalledProcessError:
                print("ERROR : subprocess.CalledProcessError - inside process_call_program function.")
        else:
            if details == "2":
                print("Selected option : Name")
                print("Calling program : Customer_Search_Name.py......")
                args_call = "python3 Customer_Search_Name.py"
                try:
                    call(args_call, shell=True)
                except subprocess.CalledProcessError:
                    print("ERROR : subprocess.CalledProcessError - inside process_call_program function.")
            else:
                print("ERROR : Not a valid option - inside process_call_program function.")
                check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou did not "
                                                                                  "select a valid option. "
                                                                                  "\nPlease try again!!!!"])
    except IndexError:
        print("ERROR : IndexError - Not a valid option - inside process_call_program function.")
        exit_program()


def process_response(response):
    if response is not None:
        details = process_get_details()
        if details is not None:
            process_call_program(details)

        flag = 2
    else:
        flag = None
        exit_program()

    return flag


def process_ask_multiple(flag, status):
    while status == 0:
        response = process_ask_question(flag)
        process_response(response)


def main():
    response = process_ask_question(flag=1)
    flag = process_response(response)
    process_ask_multiple(flag, status=0)
    exit_program()


if __name__ == "__main__":
    main()
