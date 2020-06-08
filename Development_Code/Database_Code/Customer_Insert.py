#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Insert.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Customer_Insert.py is use for inserting the data of the customer into the following table :
#               Development (DEV) : carego_customer_dev
#               Test (TEST) : carego_customer_test
#               Production (PROD) : carego_customer_prod
#
#               This program will be called from ~/Main_Process/Main_Process.py. If the customer wants to save their
#               details in the database then Main_Process.py will call this program, and this process will insert the
#               data into the table mentioned above.
#
# NOTE 1:       Please make sure to change the region's value as per region wise before putting it to server :
#               Development region: "DEV"
#               Test region: "TEST"
#               Production region: "PROD"
#
#               Check in the following function :
#               def main():
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
#
# NOTE 2:       This program can be run separately or as a stand-alone program as follow:
#               >> python3 Customer_Insert.py


import re
import sys
import psycopg2
import subprocess
from datetime import date, datetime
from subprocess import check_output


def exit_program():
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    print('Ending program : Customer_Insert.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def checking_region_table(region):
    table = None
    if region == "DEV":
        table = "carego_customer_dev"
    elif region == "TEST":
        table = "carego_customer_test"
    elif region == "PROD":
        table = "carego_customer_prod"
    else:
        print("ERROR : REGION VALUE NOT FOUND. Please check the REGION value inside the program - "
              "inside checking_region_table function.")
        exit_program()

    return table


def get_details():
    details = None
    args_get_details = "zenity --forms --width=500 --height=200 --title='Create user' --text='Add new user' \
                    --add-entry='First Name' \
                    --add-entry='Last Name' \
                    --add-entry='Email ID' \
                    --add-entry='Phone No' \
                    --add-entry='Employer' \
                    --add-entry='Role'"
    try:
        details = check_output(args_get_details, shell=True)
        details = details.decode().split('|')
        print(details)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside get_details function.")
        exit_program()

    return details


def format_details(details):
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
                                                                              "be blank or less than 2 characters. "
                                                                              "Please try again!!!!"])
            exit_program()
        elif len(details[1]) < 2:
            print("ERROR : Last Name cannot be blank or less than 2 characters. Details entered : ", details[1])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nLast Name cannot "
                                                                              "be blank or less than 2 characters. "
                                                                              "Please try again!!!!"])
            exit_program()
        elif len(details[2]) < 7:
            print("ERROR : Eamil Id must be more than 7 characters long. Details entered : ", details[2])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nEamil Id must be "
                                                                              "more than 7 characters long."
                                                                              "Please try again!!!!"])
            exit_program()
        elif re.match("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*$", details[2]) is None:
            print("ERROR : Email Id must contain @ & dot(.). Also, it should be valid Email ID. "
                  "Details entered : ", details[2])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nEmail Id must "
                                                                              "contain @ & dot(.). ""Also, it should "
                                                                              "be valid Email ID. "
                                                                              "Please try again!!!!"])
            exit_program()
        elif len(details[3]) < 7:
            print("ERROR : Phone number must be more than 7 digits long. Details entered : ", details[3])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nPhone number must "
                                                                              "be more than 7 digits long. "
                                                                              "Please try again!!!!"])
            exit_program()
        elif re.match("[0-9]", details[3]) is None:
            print("ERROR : Phone number must be numeric. Details entered : ", details[3])
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nPhone number must "
                                                                              "be numeric. Please try again!!!!"])
            exit_program()
        else:
            first_name = details[0].upper()
            last_name = details[1].upper()
            email_id = details[2]
            phone_no = details[3]
            employer = details[4]
            role = details[5].strip()
    except IndexError:
        print("ERROR : IndexError - You didn't enter any details - inside format_details function.")
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nYou didn't enter "
                                                                          "any details!!!!"])
        exit_program()

    return first_name, last_name, email_id, phone_no, employer, role


def insert(check_region_table, first_name, last_name, email_id, phone_no, employer, role, creation_date):
    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")

        query = '''INSERT INTO ''' + check_region_table + ''' ("First_Name", "Last_Name", "Email_ID", "Phone_No",
        "Employer", "Role", "Creation_Date")
        VALUES (%s, %s, %s, %s, %s, %s, %s);'''
        cur.execute(query, (first_name, last_name, email_id, phone_no, employer, role, creation_date))

        seq_query = '''SELECT CURRVAL('"carego_customer_dev_ID_seq"'::regclass);'''
        cur.execute(seq_query)
        seq = cur.fetchone()

        print("Data inserted successfully - Query & Seq. : ", query, seq_query)
        check_output(["zenity", "--info", "--width=400", "--height=200", "--text=Data inserted successfully.\n\n"
                                                                         "Please note your UNIQUE ID : "
                                                                         "" + str(seq[0])])
        print("Unique_ID : ", str(seq[0]))
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside insert function : " + str(error))
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nSomething "
                                                                          "went wrong!!!! Please try again!!!"])
    except psycopg2.IntegrityError as error:
        print("ERROR : psycopg2.IntegrityError - inside insert function : " + str(error))
        check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nDetails "
                                                                          "already present!!!! Please try again!!!"])


def main():
    region = "DEV"
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Starting program : Customer_Insert.py - at : ' + current_time + ' on : ' + current_date)

    check_region_table = checking_region_table(region)
    details = get_details()
    first_name, last_name, email_id, phone_no, employer, role = format_details(details)
    today = date.today()
    creation_date = today.strftime("%d/%m/%Y")
    insert(check_region_table, first_name, last_name, email_id, phone_no, employer, role, creation_date)

    exit_program()


if __name__ == "__main__":
    main()
