#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Search_ID.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# ----------------------------------------------------------------------------------------------------------------------
# Description:  Customer_Search_ID.py is use to search the data of the customer from the following table by using ID :
#               Development (DEV) : carego_customer_dev
#               Test (TEST) : carego_customer_test
#               Production (PROD) : carego_customer_prod
#
#               This program will be called from ~/Database_Code/Customer_Search_Main.py based on search criteria. If
#               the customer select ID option in Customer_Search_Main.py, then it will call Customer_Search_ID.py. And
#               this program will ask the ID and search the data.
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 1:       Please make sure to change the region value as per region wise before putting to server :
#               Development region: "DEV"
#               Test region: "TEST"
#               Production region: "PROD"
#
#               Check in the following function :
#               def main():
#                   region = "DEV"
#
#               This program also use conn as follow :
#               conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
#               port="5432")
#               Please make sure that everything is correct.
# ----------------------------------------------------------------------------------------------------------------------
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               >> python3 Customer_Search_ID.py
# ----------------------------------------------------------------------------------------------------------------------

import re
import sys
import psycopg2
import subprocess
from datetime import date, datetime
from subprocess import check_output


def exit_program():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Ending program : Customer_Search_ID.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def checking_region_table(region):
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
              "inside checking_region_table function.")
        exit_program()

    return main_table, sequence_table


def get_details():
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
        print("ERROR : subprocess.CalledProcessError - inside get_details function.")
        exit_program()

    return details


def format_details(details):
    id_details = None
    try:
        if len(details) < 1:
            print("ERROR : ID cannot be blank or less than 1 number. Details entered : ", details)
            check_output(["zenity", "--error", "--width=400", "--height=200",
                          "--text=ALERT!!!\n\nID cannot be blank or less than 1 number. Please try again!!!!"])
            exit_program()
        elif re.match("[0-9]", details) is None:
            print("ERROR : Phone number must be numeric. Details entered : ", details)
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nID must be numeric. "
                                                                              "Please try again!!!!"])
            exit_program()
        else:
            id_details = details
    except IndexError:
        print("ERROR : IndexError - You did not enter any details - inside format_details function.")
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou did not enter "
                                                                          "any details!!!!"])
        exit_program()

    return id_details


def search_id(check_main_table, id_details):
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT "First_Name", "Last_Name", "Email_ID", "Phone_No"
        from """ + check_main_table + """ where "ID" = '{}'; """.format(id_details)
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside search_id function.")
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=There are no data as per "
                                                                              "your search!!!!"])
            exit_program()
        else:
            print("Data searched successfully!!!!")

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside search_id function : " + str(error))
        row = None

    return row


def display_details(search_details):
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
    args_display = "zenity --list --width=800 --height=400 --title='List of people as per your search' \
    --column='ID' --column='First Name' --column='Last Name' --column='Email ID' --column='Phone Number' " \
    + display_row
    search_output = check_output(args_display, shell=True)
    print(search_output)


def main():
    region = "DEV"
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Customer_Search_ID.py - at : ' + current_time + ' on : ' + current_date)

    check_main_table,  check_sequence_table = checking_region_table(region)
    details = get_details()
    id_value = format_details(details)
    if id_value != "":
        search_details = search_id(check_main_table, id_value)
    else:
        search_details = None

    if len(search_details) > 0:
        display_details(search_details)

    exit_program()


if __name__ == "__main__":
    main()
