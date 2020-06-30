#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Carego_Customer_Reports.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  This code deals with the following table:
#
#               * Development (DEV) : carego_customer_dev
#               * Test (TEST) : carego_customer_test
#               * Production (PROD) : carego_customer_prod
#
#               Carego_Customer_Reports.py program will fetch the records from the table and will create a CSV file.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow:
#           	$ python3 Carego_Customer_Reports.py
# **********************************************************************************************************************
"""

import os
import sys
import csv
import psycopg2
from datetime import date, datetime


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
    print('Starting Program : Carego_Customer_Reports.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Carego_Customer_Reports.py - at : ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. csv_file signifies the output report file.
    2. Region = "DEV" signifies that we are running the code in the development region. And as per the region value,
    this program will choose the table.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    csv_file = 'Carego_Customer_Reports.csv'
    region = "DEV"

    return csv_file, region


def process_checking_directory():
    main_directory = "/home/somak/Robotic-Greeter/Reports/"

    try:
        os.chdir(main_directory)
    except FileNotFoundError:
        os.mkdir(main_directory)
        os.chdir(main_directory)


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


def process_search(check_main_table):
    """
    ************************************ Inside process_search function ************************************************
    Function to get the table details.

    This function will get the table details and will return the row value.
    ************************************ Inside process_search function ************************************************
    """

    try:
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT * from """ + check_main_table + """ order by "ID";"""
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside process_search_first_last_name function.")
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


def process_table_data_write(csv_file, table_details):
    """
    ************************************ Inside process_search function ************************************************
    Function to write the table details into CSV file.
    ************************************ Inside process_search function ************************************************
    """

    header = ['ID', 'First Name', 'Last Name', 'Email ID', 'Phone No', 'Employer', 'Role', 'Creation Date']
    print('Generating CSV file')

    with open(csv_file, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)

    with open(csv_file, 'a+') as output_file:
        writer = csv.writer(output_file)
        for row in table_details:
            temp_list = []
            for item in row:
                try:
                    col = item.rstrip()
                except AttributeError:
                    col = item

                temp_list.append(col)

            writer.writerow(temp_list)


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    csv_file, region = process_parameter_set()
    process_checking_directory()
    check_main_table, check_sequence_table = process_checking_region_table(region)
    table_details = process_search(check_main_table)
    process_table_data_write(csv_file, table_details)
    exit_program()


if __name__ == "__main__":
    main()
