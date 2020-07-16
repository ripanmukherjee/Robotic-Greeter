#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Search_Main.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Customer_Search_Main.py is used to search the user's data, and it will be called from Main_Process.py.
#               If the user wants to explore the data, this process will ask the user wants to search by ID or Name,
#               and as per the selection, this program will call the below two programs:
#               1. Customer_Search_ID.py
#               2. Customer_Search_Name.py
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Customer_Search_Main.py
# **********************************************************************************************************************
"""

import sys
import subprocess
from datetime import date, datetime
from subprocess import check_output, call


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
    print('Starting program : Customer_Search_Main.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Customer_Search_Main.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_ask_question(flag):
    """
    ************************************ Inside process_ask_question function ******************************************
    Function to prompt pop-up questions for the user.

    This function will ask if the user wants to update their details or not by prompting a pop-up message, and later
    it will return the user response. This function will prompt the question based on the value of the flag. If the
    function cannot run the pop-up process, then it will print an error message and will return response as None.
    ************************************ Inside process_ask_question function ******************************************
    """

    response = None
    if flag == 1:
        args = "zenity --info --width=500 --height=250 --text='You can search by ID or Name'"
    else:
        args = "zenity --question --width=500 --height=250 --text='Do you want to search another people?'"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_ask_question function.")

    return response


def process_get_details():
    """
    ************************************ Inside process_get_details function *******************************************
    Function to get search option from the user.

    This function will prompt a pop-up message for the user to select ID or Name (First Name or Last Name) they want to
    search with. User can choose or click ID or Name checkbox one at a time.
    ************************************ Inside process_get_details function *******************************************
    """

    details = None
    args = "zenity --list --width=500 --height=250 --title='List of search -Select only one option' --checklist \
    --column='Option' --column='Search' --column='Description' \
    1 'ID' 'Search by ID' \
    2 'Name' 'Search by First Name or Last Name'"

    try:
        details = check_output(args, shell=True)
        details = details.decode().split('|')
        details = details[0].strip()
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details function.")

    return details


def process_call_program(details):
    """
    ************************************ Inside process_call_program function ******************************************
    Function to get call search program.

    Based on the search option selected by user, this function will call the Customer_Search_ID.py or
    Customer_Search_Name.py.
    ************************************ Inside process_call_program function ******************************************
    """

    try:
        if details == "ID":
            print("Selected option : ID")
            print("Calling program : Customer_Search_ID.py......")
            args_call = "python3 Customer_Search_ID.py"
            try:
                call(args_call, shell=True)
            except subprocess.CalledProcessError:
                print("ERROR : subprocess.CalledProcessError - inside process_call_program function.")
        else:
            if details == "Name":
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
    """
    ************************************ Inside process_response function **********************************************
    Function to validate the user response.

    This function will call other functions based on the response chosen by the user. If the response is None or at the
    end of all steps, this function will set the flag as 2. Which means the first iteration is finish and will enter
    into the second iteration.
    ************************************ Inside process_response function **********************************************
    """

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
    """
    ************************************ Inside process_ask_multiple function ******************************************
    This function is a loop function that will run until the user chose not to update anymore.
    ************************************ Inside process_ask_multiple function ******************************************
    """

    while status == 0:
        response = process_ask_question(flag)
        process_response(response)


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    response = process_ask_question(flag=1)
    flag = process_response(response)
    process_ask_multiple(flag, status=0)
    exit_program()


if __name__ == "__main__":
    main()
