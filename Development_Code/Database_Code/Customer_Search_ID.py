#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Search_ID.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Customer_Search_ID.py is used to search the user's data from the table mentioned above by using an ID.
#               This program will be called from Customer_Search_Main.py based on search criteria. If the user selects
#               the ID option in Customer_Search_Main.py, then it will call Customer_Search_ID.py. And this program
#               will ask the ID and search the data.
# **********************************************************************************************************************
# NOTE 1:       Please make sure to change the region value as per region wise before putting to server :
#               Development region: "DEV"
#               Test region: "TEST"
#               Production region: "PROD"
#
#               Check in the following function :
#               def main():
#                   region = "DEV"
#
#               This program also use database connection from python as follow :
#               conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
#               port="5432")
#               Please make sure that everything is correct.
# **********************************************************************************************************************
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Customer_Search_ID.py
# **********************************************************************************************************************
"""

import re
import sys
import pickle
import psycopg2
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
    print('Starting program : Customer_Search_ID.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Customer_Search_ID.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. Region = "DEV" signifies that we are running the code in the development region. And as per the region value,
    this program will choose the table.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    region = "DEV"

    return region


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


def process_get_details():
    """
    ************************************ Inside process_get_details function *******************************************
    Function to get the ID details from the user.

    This function will ask the user to enter the details of ID and later will return the details. If the function
    cannot able to call the pop-up function, then it will exit from the program.
    ************************************ Inside process_get_details function *******************************************
    """

    details = None
    args_get_details = "zenity --forms --width=500 --height=200 --title='Search user' \
                --text='Search with ID' \
                --add-entry='ID'"
    try:
        details = check_output(args_get_details, shell=True)
        details = details.decode().split('|')
        details = details[0].strip()
        print(details)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details function.")
        exit_program()

    return details


def process_format_details(details):
    """
    ************************************ Inside process_format_details function ****************************************
    Function to validate the ID.

    This function will validate the details entered by the users. The ID cannot be blank or less than 1 number. If the
    validation is successful then this function will return the ID or else will return as None.
    ************************************ Inside process_format_details function ****************************************
    """

    id_details = None
    try:
        if len(details) < 1:
            print("ERROR : ID cannot be blank or less than 1 number. Details entered : ", details)
            check_output(["zenity", "--error", "--width=400", "--height=200",
                          "--text=ALERT!!!\n\nID cannot be blank or less than 1 number. \nPlease try again!!!!"])
            exit_program()
        elif re.match("[0-9]", details) is None:
            print("ERROR : ID should be numeric. Details entered : ", details)
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nID should be numeric."
                                                                              "\nPlease try again!!!!"])
            exit_program()
        else:
            id_details = details
    except IndexError:
        print("ERROR : IndexError - You did not enter any details - inside process_format_details function.")
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou did not enter "
                                                                          "any details!!!!"])
        exit_program()

    return id_details


def process_search_id(check_main_table, id_value):
    """
    ************************************ Inside process_search_first_name function *************************************
    Function to search the details.

    This function will search the details from the table by ID and later will return the row. If there are no details
    in the table, it will prompt as "There are no data as per your search!!!!" and will return row as None.
    ************************************ Inside process_search_first_name function *************************************
    """

    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT "ID", "First_Name", "Last_Name", "Email_ID", "Phone_No"
        from """ + check_main_table + """ where "ID" = '{}'; """.format(id_value)
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside process_search_id function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=There are no data as per "
                                                                              "your search!!!!"])
            exit_program()
        else:
            print("Data searched successfully!!!!")

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_search_id function : " + str(error))
        row = None

    return row


def process_display_details(search_details):
    """
    ************************************ Inside process_display_details function ***************************************
    Function to display the table details.

    This function will receive the searched details and display it as a pop-up list.
    ************************************ Inside process_display_details function ***************************************
    """

    display_row = ""
    counter = 0
    for list_details in search_details:
        total_tuple = list_details
        for tuple_details in total_tuple:
            if counter == 0:
                display_row = str(tuple_details)
                counter += 1
            else:
                display_row = display_row + " " + str(tuple_details)
                counter += 1

    print(display_row)
    args_display = "zenity --list --width=800 --height=600 --title='List of people - Select only one option' " \
                   "--checklist --column='Option' --column='First Name' --column='Last Name' --column='Email ID' " \
                   "--column='Phone Number' --print-column=ALL " + display_row
    try:
        search_output = check_output(args_display, shell=True)
        search_output = search_output.strip()
        search_output = search_output.decode().split('|')
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_display_details function")
        search_output = None

    return search_output


def process_id_search_display(check_main_table, id_value):
    """
    ************************************ Inside process_search_display function ****************************************
    Function to validate the ID details.

    This function will call the search function based on the value of ID entered by user.
    ************************************ Inside process_search_display function ****************************************
    """

    if id_value is not None:
        search_details = process_search_id(check_main_table, id_value)
    else:
        search_details = None

    first_name = None
    last_name = None
    email_id = None
    phone_no = None
    if search_details is not None:
        if len(search_details) > 0:
            search_output = process_display_details(search_details)
            if search_output is not None:
                print('Searched Details : ' + str(search_output))
                try:
                    first_name = search_output[0]
                    last_name = search_output[1]
                    email_id = search_output[2]
                    phone_no = search_output[3]
                except IndexError:
                    exit_program()
            else:
                exit_program()
        else:
            exit_program()
    else:
        exit_program()

    return first_name, last_name, email_id, phone_no


def process_show_details(first_name, last_name, email_id, phone_no):
    """
    ************************************ Inside process_show_details function ******************************************
    This function will show the Name, Email ID and Phone Number of the person as a pop-up message after the user
    selected the search person from the result list.
    ************************************ Inside process_show_details function ******************************************
    """

    try:
        check_output(["zenity", "--info", "--width=400", "--height=200", "--text=You have searched : "
                      + first_name + " " + last_name + "\n\nEmail ID is : " + email_id +
                      "\nPhone Number is : " + phone_no])

    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_display_details function")


def process_write_pickle_file(first_name, last_name, email_id, phone_no):
    """
    ************************************ Inside process_write_pickle_file function *************************************
    This function will write the details of the searched person into a pickle file
    ************************************ Inside process_write_pickle_file function *************************************
    """

    new_data = {"First_Name": first_name, "Last_Name": last_name, "Email_ID": email_id, "Phone_No": phone_no}
    with open("Search_Output.pickle", "wb+") as pickle_file:
        pickle_file.write(pickle.dumps(new_data))

    with open("Search_Output.pickle", "rb") as file:
        unpickler = pickle.Unpickler(file)
        data = unpickler.load()
        print(data['Email_ID'])


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    region = process_parameter_set()
    check_main_table,  check_sequence_table = process_checking_region_table(region)
    details = process_get_details()
    id_value = process_format_details(details)
    first_name, last_name, email_id, phone_no = process_id_search_display(check_main_table, id_value)
    process_show_details(first_name, last_name, email_id, phone_no)
    # process_write_pickle_file(first_name, last_name, email_id, phone_no)
    exit_program()


if __name__ == "__main__":
    main()
