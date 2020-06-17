#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Search_Name.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# ----------------------------------------------------------------------------------------------------------------------
# Description:  Customer_Search_Name.py is use to search the data of the customer from the following table
#               by using Name :
#               Development (DEV) : carego_customer_dev
#               Test (TEST) : carego_customer_test
#               Production (PROD) : carego_customer_prod
#
#               This program will be called from ~/Database_Code/Customer_Search_Main.py based on search criteria. If
#               the customer select Name option in Customer_Search_Main.py, then it will call Customer_Search_Name.py.
#               And this program will ask the Name and search the data.
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 1:       Please make sure to change the region value as per region wise before putting to server :
#               Development region: "DEV"
#               Test region: "TEST"
#               Production region: "PROD"
#
#               Check in the following function :
#               def process_parameter_set():
#                   region = "DEV"
#
#               This program also use conn as follow :
#               conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
#               port="5432")
#               Please make sure that everything is correct.
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               >> python3 Customer_Search_Name.py
# ----------------------------------------------------------------------------------------------------------------------

import sys
import psycopg2
import subprocess
from datetime import date, datetime
from subprocess import check_output


def start_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting Program : Customer_Search_Name.py - at : ' + current_time + ' on : ' + current_date)


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Customer_Search_Name.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    region = "DEV"

    return region


def process_checking_region_table(region):
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
    details = None
    args_get_details = "zenity --forms --width=500 --height=200 --title='Search user' \
                --text='Search with either First or Last Name or both of the following' \
                --add-entry='First Name' \
                --add-entry='Last Name'"
    try:
        details = check_output(args_get_details, shell=True)
        details = details.decode().split('|')
        print(details)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details function.")
        exit_program()

    return details


def process_format_details(details):
    first_name = None
    last_name = None
    details[1] = details[1].strip()
    try:
        if len(details[0]) < 2 and len(details[1]) < 2:
            print("ERROR : First Name or Last Name cannot be blank or less than 2 characters. "
                  "Details entered : ", details[0])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nFirst Name or "
                                                                              "Last Name cannot be blank or "
                                                                              "less than 2 characters. "
                                                                              "\nPlease try again!!!!"])
            exit_program()
        elif len(details[0]) >= 2 and len(details[1]) < 2:
            first_name = details[0].upper()
            last_name = ""
        elif len(details[0]) < 2 and len(details[1]) >= 2:
            first_name = ""
            last_name = details[1].upper()
        else:
            first_name = details[0].upper()
            last_name = details[1].upper()
    except IndexError:
        print("ERROR : IndexError - You did not enter any details - inside process_format_details function.")
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou did not "
                                                                          "enter any details!!!!"])
        exit_program()

    return first_name, last_name


def process_search_first_name(check_main_table, first_name):
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT "First_Name", "Last_Name", "Email_ID", "Phone_No"
        from """ + check_main_table + """ where "First_Name" LIKE '%{}%'; """.format(first_name)
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside process_search_first_name function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=There are no data "
                                                                              "as per your search!!!!"])
            exit_program()
        else:
            print("Data searched successfully!!!!")

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_search_first_name function : " + str(error))
        row = None

    return row


def process_search_last_name(check_main_table, last_name):
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT "First_Name", "Last_Name", "Email_ID", "Phone_No"
        from """ + check_main_table + """ where "Last_Name" LIKE '%{}%'; """.format(last_name)
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside process_search_last_name function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=There are no data "
                                                                              "as per your search!!!!"])
            exit_program()
        else:
            print("Data searched successfully!!!!")

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_search_last_name function : " + str(error))
        row = None

    return row


def process_search_first_last_name(check_main_table, first_name, last_name):
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT "First_Name", "Last_Name", "Email_ID", "Phone_No"
        from """ + check_main_table + """ where "First_Name" LIKE '%{}%' and
        "Last_Name" LIKE '%{}%'; """.format(first_name, last_name)
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside process_search_first_last_name function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=There are no data "
                                                                              "as per your search!!!!"])
            exit_program()
        else:
            print("Data searched successfully!!!!")

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_search_first_last_name function : " + str(error))
        row = None

    return row


def process_display_details(search_details):
    display_row = ""
    counter = 0
    for list_details in search_details:
        details_tuple = list_details
        for tuple_details in details_tuple:
            if counter == 0:
                display_row = str(tuple_details)
                counter += 1
            else:
                display_row = display_row + " " + str(tuple_details)
                counter += 1

    print(display_row)
    args_display = "zenity --list --width=800 --height=600 --title='List of people as per your search' \
    --column='First Name' --column='Last Name' --column='Email ID' --column='Phone Number' " \
    + display_row
    search_output = check_output(args_display, shell=True)
    print(search_output)


def process_search_display(check_main_table, first_name, last_name):
    if first_name != "" and last_name == "":
        search_details = process_search_first_name(check_main_table, first_name)
    elif first_name == "" and last_name != "":
        search_details = process_search_last_name(check_main_table, last_name)
    elif first_name != "" and last_name != "":
        search_details = process_search_first_last_name(check_main_table, first_name, last_name)
    else:
        search_details = None

    if search_details is not None:
        process_display_details(search_details)


def main():
    start_program()
    region = process_parameter_set()
    check_main_table, check_sequence_table = process_checking_region_table(region)
    details = process_get_details()
    first_name, last_name = process_format_details(details)
    process_search_display(check_main_table, first_name, last_name)
    exit_program()


if __name__ == "__main__":
    main()
