#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Insert.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  All the python code in Database Code folder deals with the following table:
#
#               * Development (DEV) : carego_customer_dev
#               * Test (TEST) : carego_customer_test
#               * Production (PROD) : carego_customer_prod
#
#               Customer_Insert.py is use for inserting the data of the customer into the table mentioned above. This
#               program will be called from Main_Process.py. If the customer wants to save their details in the
#               database, then Main_Process.py will call this program, and this process will insert the data into
#               the table mentioned above.
# **********************************************************************************************************************
# NOTE 1:       Please make sure to change the region's value as per region wise before putting it to server :
#               Development region: "DEV"
#               Test region: "TEST"
#               Production region: "PROD"
#
#               Check in the following function :
#               def process_parameter_set():
#               region = "DEV"
#
#               Also, this program use "carego_customer_dev_ID_seq" as follow :
#               seq_query = '''SELECT CURRVAL('"carego_customer_dev_ID_seq"'::regclass);'''
#               Please, make sure if you are creating new table then change the sequence value.
#
#               This program also use conn as follow :
#               conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
#               port="5432")
#               Please make sure that everything is correct.
# **********************************************************************************************************************
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               $ python3 Customer_Insert.py
# **********************************************************************************************************************
"""

import re
import sys
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
    print('Starting program : Customer_Insert.py - at : ' + current_time + ' on : ' + current_date)


def exit_program():
    """
    ************************************ Inside exit_program function **************************************************
    This function will be called at the end to print today's date and end time.
    ************************************ Inside exit_program function **************************************************
    """

    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    print('Ending program : Customer_Insert.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    region = "DEV"
    today = date.today()
    creation_date = today.strftime("%d/%m/%Y")

    return region, creation_date


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


def process_ask_question(flag):
    response = None
    if flag == 1:
        args = "zenity --question --width=500 --height=250 --text='You need to create your details. \n\n" \
               "Do you want to proceed?'"
    else:
        args = "zenity --question --width=500 --height=250 --text='You need to create your details. \n\n" \
               "Do you want to proceed?'"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_ask_question function.")

    return response


def process_get_details():
    args_get_details = "zenity --forms --width=500 --height=200 --title='Create user' \
                    --text='Add new user' \
                    --add-entry='First Name' \
                    --add-entry='Last Name' \
                    --add-entry='Email ID' \
                    --add-entry='Phone No' \
                    --add-entry='Employer' \
                    --add-entry='Role'"

    try:
        details = check_output(args_get_details, shell=True)
        details = details.strip()
        details = details.decode().split('|')
        print(details)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details function.")
        details = None

    return details


def process_format_details(details):
    first_name = None
    last_name = None
    email_id = None
    phone_no = None
    employer = None
    role = None
    try:
        if len(details[0]) < 2:
            print("ERROR : First Name cannot be blank or less than 2 characters. Details entered : ", details[0])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nFirst Name cannot "
                                                                              "be blank or less than 2 characters. \n"
                                                                              "Please try again!!!!"])
            error_flag = 1
        elif len(details[1]) < 2:
            print("ERROR : Last Name cannot be blank or less than 2 characters. Details entered : ", details[1])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nLast Name cannot "
                                                                              "be blank or less than 2 characters. \n"
                                                                              "Please try again!!!!"])
            error_flag = 1
        elif len(details[2]) < 7:
            print("ERROR : Email Id should be more than 7 characters long. Details entered : ", details[2])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nEmail Id should be "
                                                                              "more than 7 characters long. \n"
                                                                              "Please try again!!!!"])
            error_flag = 1
        elif re.match("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*$", details[2]) is None:
            print("ERROR : Email Id should contain - @ & dot(.). Also, it should be a valid Email ID. "
                  "Details entered : ", details[2])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nEmail Id should "
                                                                              "contain - @ and  dot(.). "
                                                                              "Also, it should be a valid Email ID. \n"
                                                                              "Please try again!!!!"])
            error_flag = 1
        elif len(details[3]) < 7:
            print("ERROR : Phone number should be more than 7 digits long. Details entered : ", details[3])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nPhone number should "
                                                                              "be more than 7 digits long. \n"
                                                                              "Please try again!!!!"])
            error_flag = 1
        elif re.match("[0-9]", details[3]) is None:
            print("ERROR : Phone number should be numeric. Details entered : ", details[3])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nPhone number should "
                                                                              "be numeric. \nPlease try again!!!!"])
            error_flag = 1
        else:
            first_name = details[0].upper()
            last_name = details[1].upper()
            email_id = details[2]
            phone_no = details[3]
            employer = details[4]
            role = details[5].strip()
            error_flag = 0
    except IndexError:
        print("ERROR : IndexError - You did not enter any details - inside process_format_details function.")
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou did not enter "
                                                                          "any details!!!!"])
        error_flag = 1

    return first_name, last_name, email_id, phone_no, employer, role, error_flag


def process_insert(check_main_table, check_sequence_table, first_name, last_name, email_id, phone_no, employer,
                   role, creation_date):
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")

        query = '''INSERT INTO ''' + check_main_table + ''' ("First_Name", "Last_Name", "Email_ID", "Phone_No",
        "Employer", "Role", "Creation_Date")
        VALUES (%s, %s, %s, %s, %s, %s, %s);'''
        cur.execute(query, (first_name, last_name, email_id, phone_no, employer, role, creation_date))

        seq_query = '''SELECT CURRVAL('"''' + check_sequence_table + '''"'::regclass);'''
        cur.execute(seq_query)
        seq = cur.fetchone()

        print("Data inserted successfully - Query & Seq. : ", query, seq_query)
        check_output(["zenity", "--info", "--width=400", "--height=200", "--text=Data inserted successfully.\n\n"
                                                                         "Please note your UNIQUE ID : "
                                                                         "" + str(seq[0])])
        print("Unique_ID : ", str(seq[0]))
        error_flag = 0
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_insert function : " + str(error))
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nSomething "
                                                                          "went wrong!!!! \nPlease try again!!!"])
        error_flag = 1
    except psycopg2.IntegrityError as error:
        print("ERROR : psycopg2.IntegrityError - inside process_insert function : " + str(error))
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nDetails "
                                                                          "already present!!!! \nPlease try again!!!"])
        error_flag = 1

    return error_flag


def process_response(response, check_main_table, check_sequence_table, creation_date):
    if response is not None:
        details = process_get_details()
        if details is not None:
            first_name, last_name, email_id, phone_no, employer, role, error_flag = process_format_details(details)
            if error_flag == 0:
                error_flag = process_insert(check_main_table, check_sequence_table, first_name, last_name, email_id,
                                            phone_no, employer, role, creation_date)
                if error_flag == 0:
                    exit_program()

        flag = 2

    else:
        flag = None
        exit_program()

    return flag


def process_ask_multiple(flag, check_main_table, check_sequence_table, creation_date, status):
    while status == 0:
        response = process_ask_question(flag)
        process_response(response, check_main_table, check_sequence_table, creation_date)


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    region, creation_date = process_parameter_set()
    check_main_table, check_sequence_table = process_checking_region_table(region)
    response = process_ask_question(flag=1)
    flag = process_response(response, check_main_table, check_sequence_table, creation_date)
    process_ask_multiple(flag, check_main_table, check_sequence_table, creation_date, status=0)
    exit_program()


if __name__ == "__main__":
    main()
