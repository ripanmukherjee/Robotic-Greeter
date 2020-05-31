#!/usr/bin/env python3

# Project : Robotic Greeter - CareGo Tek
# Program Name : Customer_Search_Main.py
# Author : Somak Mukherjee
# Date : Friday 24 April, 2020
# Version : 1
# Description: Customer_Search_Main.py is used to search the customer's data, and it will be called from
#               ~/Main_Process/Main_Process.py. If the customer wants to explore the data, then this process will ask
#               to the customer wants to search by ID or Name, and as per the selection this program will call the
#               below two program:
#               1. Customer_Search_ID.py
#               2. Customer_Search_Name.py
#
# NOTE: This program can be run separately or as a stand-alone program as follow:
# >> python3 Customer_Search_Main.py


import sys
import subprocess
from datetime import date, datetime
from subprocess import check_output, call


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Customer_Search_Main.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def ask_question(flag):
    response = None
    if flag == 1:
        args = "zenity --question --width=500 --height=250 --text='You can search by ID or Name. \n\n" \
               "Do you want to proceed?' 2>/dev/null"
    else:
        args = "zenity --question --width=500 --height=250 --text='Do you want to search another people?' 2>/dev/null"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside ask_question function.")

    return response


def get_details():
    details = None
    args = "zenity --list --width=500 --height=250 --title='List of search' \
    --column='Option' --column='Description' \
    1 'Search by ID' \
    2 'Search by First Name or Last Name' 2>/dev/null"

    try:
        details = check_output(args, shell=True)
        details = details.decode().split('|')
        details = details[0].strip()
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside get_details function.")
        exit_program()

    return details


def call_program(details):
    try:
        if details == "1":
            print("Selected option : ID")
            print("Calling program : Customer_Search_ID.py......")
            args_call = "python3 Customer_Search_ID.py"
            call(args_call, shell=True)
        else:
            if details == "2":
                print("Selected option : Name")
                print("Calling program : Customer_Search_Name.py......")
                args_call = "python3 Customer_Search_Name.py"
                call(args_call, shell=True)
            else:
                print("ERROR : Not valid option - inside call_program function.")
                check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou didn't "
                                                                                  "select valid option. "
                                                                                  "Please try again!!!!"])
                exit_program()
    except IndexError:
        print("ERROR : IndexError - Not valid option - inside call_program function.")
        exit_program()


def main():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Customer_Search_Main.py - at : ' + current_time + ' on : ' + current_date)

    flag = 1
    response = ask_question(flag)
    status = 0
    if response is not None:
        details = get_details()
        call_program(details)
        flag = 2
    else:
        exit_program()

    while status == 0:
        response = ask_question(flag)
        if response is not None:
            details = get_details()
            call_program(details)
        else:
            status = 1

    exit_program()


if __name__ == "__main__":
    main()
