#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Customer_Update.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Customer_Update.py is used to update the data of the user into the table mentioned above. This program
#               will be called from Main_Process.py if the user wants to update their details. To update the details,
#               the user should know their unique ID, as this program will ask to confirm the ID before updating.
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
#               $ python3 Customer_Update.py
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
    print('Starting program : Customer_Update.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Customer_Update.py - at : ' + current_time + ' on : ' + current_date)
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


def process_ask_question(flag):
    """
    ************************************ Inside process_ask_question function ******************************************
    Function to prompt pop-up questions for the user.

    This function will ask if the user wants to update their details or not by prompting a pop-up message, and later
    it will return the user response. This function will prompt the question based on the value of the flag. If the
    function cannot run the pop-up process, then it will print an error and will exit from the program.
    ************************************ Inside process_ask_question function ******************************************
    """

    response = None
    if flag == 1:
        args = "zenity --question --width=500 --height=250 --text='Make sure you have your Unique ID. \n\n" \
               "Do you want to proceed?'"
    else:
        args = "zenity --question --width=500 --height=250 --text='Do you want to update another details?'"

    try:
        response = check_output(args, shell=True)
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_ask_question function.")
        exit_program()

    return response


def process_get_details_initial_option():
    """
    ************************************ Inside process_get_details_initial_option function ****************************
    Function to get the update option.

    This function will ask the user to select the option they want to update. User can choose one option at a
    time. If the user chooses "First Name," it will return the value of the option, which is 1 for the First Name.
    Later, it will return the option's value. If the function cannot run the pop-up process, then it will print an
    error message and will return option's value as None.
    ************************************ Inside process_get_details_initial_option function ****************************
    """

    args = "zenity --list --width=500 --height=300 --title='Modify the data - Select only one of the following' " \
           "--checklist --column='Option' --column='Number' --column='Description' \
            1 1 'Modify First Name' \
            2 2 'Modify Last Name' \
            3 3 'Modify Email ID' \
            4 4 'Modify Phone Number' \
            5 5 'Modify Employer' \
            6 6 'Modify Role'"

    try:
        details = check_output(args, shell=True)
        details = details.decode().split('|')
        details[0] = details[0].strip()
        details = details[0]
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_details_initial_option function.")
        details = None

    return details


def process_assign_update_option(details):
    """
    ************************************ Inside process_assign_update_option function **********************************
    Function to validate the update option.

    This function is to validate the update option and later return it for the update. If the option value is wrong
    then this function will print error message and will return option value as None.
    ************************************ Inside process_assign_update_option function **********************************
    """

    try:
        if details == "1":
            print("Selected option : Modify First Name")
            option = 1
        else:
            if details == "2":
                print("Selected option : Modify Last Name")
                option = 2
            else:
                if details == "3":
                    print("Selected option : Modify Email ID")
                    option = 3
                else:
                    if details == "4":
                        print("Selected option : Modify Phone Number")
                        option = 4
                    else:
                        if details == "5":
                            print("Selected option : Modify Employer")
                            option = 5
                        else:
                            if details == "6":
                                print("Selected option : Modify Role")
                                option = 6
                            else:
                                print("ERROR : Not a valid option - inside process_assign_update_option function.")
                                check_output(["zenity", "--error", "--width=400", "--height=200",
                                              "--text=ALERT!!!\n\nYou did not select a valid option. "
                                              "\nPlease try again!!!!"])
                                option = None
    except IndexError:
        print("ERROR : IndexError - Not a valid option - inside process_assign_update_option function.")
        option = None

    return option


def process_get_details_validation(option):
    """
    ************************************ Inside process_get_details_validation function ********************************
    Function to get the new update details from the user.

    This function will prompt a pop-up message for the users to enter the new details based on the option chosen
    by the users. Later, this will validate the details entered by the users.

    Validation as follow:

    1. First_Name   : Cannot be less than 2 characters or numbers
    2. Last_name    : Cannot be less than 2 characters or numbers
    3. Email_ID     : Cannot be less than 7 characters and has to include @ and dot
    4. Phone_No     : Cannot be less than 7 Numbers and has to be numeric
    5. Employer     : Cannot be less than 2 characters or numbers
    6. Role         : Cannot be less than 2 characters or numbers

    If the validation passed then it will return the details or else will print error message, prompt the same error
    message for the user and then will return details as None.
    ************************************ Inside process_get_details_validation function ********************************
    """

    details = None
    if option == 1:
        args_get_details = "zenity --forms --width=500 --height=200 --title='Modify user' \
                    --text='Please enter the new details in the following' \
                    --add-entry='First Name'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            details = details[0].strip()
            details = details.upper()
            if len(details) < 2:
                print("ERROR : First Name cannot be blank or less than 2 characters. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nFirst Name cannot be blank or less than 2 characters. "
                              "\nPlease try again!!!!"])
                details = None
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_get_details_validation function.")
            details = None

    if option == 2:
        args_get_details = "zenity --forms --width=500 --height=200 --title='Modify user' \
                    --text='Please enter the new details in the following' \
                    --add-entry='Last Name'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            details = details[0].strip()
            details = details.upper()
            if len(details) < 2:
                print("ERROR : Last Name cannot be blank or less than 2 characters. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nLast Name cannot be blank or less than 2 characters. "
                              "\nPlease try again!!!!"])
                details = None
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_get_details_validation function.")
            details = None

    if option == 3:
        args_get_details = "zenity --forms --width=500 --height=200 --title='Modify user' \
                    --text='Please enter the new details in the following' \
                    --add-entry='Email ID'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            details = details[0].strip()
            if len(details) < 7:
                print("ERROR : Email Id should be more than 7 characters long. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nEmail Id should be more than 7 characters long. "
                              "\nPlease try again!!!!"])
                details = None
            elif re.match("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*$", details) == None:
                print("ERROR : Email Id should contain - @ and dot(.). "
                      "Also, it should be a valid Email ID. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nEmail Id should contain - @ and dot(.). "
                              "Also, it should be a valid Email ID. \nPlease try again!!!!"])
                details = None
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_get_details_validation function.")
            details = None

    if option == 4:
        args_get_details = "zenity --forms --width=500 --height=200 --title='Modify user' \
                    --text='Please enter the new details in the following' \
                    --add-entry='Phone No'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            details = details[0].strip()
            if len(details) < 7:
                print("ERROR : Phone number should be more than 7 digits long. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nPhone number should be more than 7 digits long. "
                              "\nPlease try again!!!!"])
                details = None
            elif re.match("[0-9]", details) is None:
                print("ERROR : Phone number should be numeric. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nPhone number should be numeric. \nPlease try again!!!!"])
                details = None
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_get_details_validation function.")
            details = None

    if option == 5:
        args_get_details = "zenity --forms --width=500 --height=200 --title='Modify user' \
                    --text='Please enter the new details in the following' \
                    --add-entry='Employer'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            details = details[0].strip()
            if len(details) < 2:
                print("ERROR : Employer details cannot be blank or less than 2 characters. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nEmployer details cannot be blank or less than 2 characters. "
                              "\nPlease try again!!!!"])
                details = None
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_get_details_validation function.")
            details = None

    if option == 6:
        args_get_details = "zenity --forms --width=500 --height=200 --title='Modify user' \
                    --text='Please enter the new details in the following' \
                    --add-entry='Role'"
        try:
            details = check_output(args_get_details, shell=True)
            details = details.decode().split('|')
            details = details[0].strip()
            if len(details) < 2:
                print("ERROR : Role details cannot be blank or less than 2 characters. Details entered : ", details)
                check_output(["zenity", "--error", "--width=400", "--height=200",
                              "--text=ALERT!!!\n\nRole details cannot be blank or less than 2 characters. "
                              "\nPlease try again!!!!"])
                details = None
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside process_get_details_validation function.")
            details = None

    if option == 0:
        print("ERROR : Not a valid entry - inside process_get_details_validation function.")
        details = None

    return details, option


def process_get_id_confirmation():
    """
    ************************************ Inside process_get_id_confirmation function ***********************************
    Function to get ID for the confirmation.

    This function will prompt a pop-up message for the users to enter the Unique ID for the confirmation. Correct
    ID is required since this function will validate the ID, which has to be at least 1 number long and numeric. Also,
    it will return the ID to check if the ID is present in the table or not. If the ID is not correct then this
    function will print error message, prompt the same error message to the user and will return ID as None.
    ************************************ Inside process_get_id_confirmation function ***********************************
    """

    args_get_details = "zenity --forms --width=500 --height=200 --title='Confirmation' \
                --text='Confirm Your ID' \
                --add-entry='ID'"
    try:
        id_details = check_output(args_get_details, shell=True)
        id_details = id_details.decode().split('|')
        id_details = id_details[0].strip()
        if len(id_details) < 1:
            print("ERROR : ID cannot be blank or less than 1 number. Details entered : ", id_details)
            check_output(["zenity", "--error", "--width=400", "--height=200",
                          "--text=ALERT!!!\n\nID cannot be blank or less than 1 number. Please try again!!!!"])
            main_id = None
        elif re.match("[0-9]", id_details) is None:
            print("ERROR : ID should be numeric. Details entered : ", id_details)
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=ALERT!!!\n\nID should be numeric."
                                                                              "\nPlease try again!!!!"])
            main_id = None
        else:
            main_id = id_details
    except subprocess.CalledProcessError:
        print("ERROR : subprocess.CalledProcessError - inside process_get_id_confirmation function.")
        main_id = None

    return main_id


def process_search_id(check_main_table, confirm_id):
    """
    ************************************ Inside process_search_id function *********************************************
    Function to confirm the ID from the table.

    This function will check if the ID is present in the table or not. If the ID does not exits, then this function
    will return count as 0 or else return the table's count.
    ************************************ Inside process_search_id function *********************************************
    """

    try:
        count = 0
        conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        print("Connection success")
        query = """SELECT count(1) from """ + check_main_table + """ where "ID" = '{}'; """.format(confirm_id)
        cur.execute(query)
        row = cur.fetchall()

        if len(row) == 0:
            print("ERROR : There are no data as per your search - inside process_search_id function.")
            count = 0
        else:
            for total_tuple in row:
                for tuple_details in total_tuple:
                    count = tuple_details

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as error:
        print("ERROR : psycopg2.OperationalError - inside process_search_id function : " + str(error))
        count = 0

    return count


def process_update_table(check_main_table, update_details, update_option, confirm_id):
    """
    ************************************ Inside process_update_table function ******************************************
    Function to update the details in the table.

    This function will update the details in the table based on the option chosen by the user. If this function
    cannot able to update due to any psycopg2 error then it will prompt "Please contact admin!!!!"
    ************************************ Inside process_update_table function ******************************************
    """

    if update_option == 1:
        try:
            conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
                                    port="5432")
            cur = conn.cursor()
            print("Connection Success")

            query = '''UPDATE ''' + check_main_table + ''' SET "First_Name" = '{}'
            WHERE "ID" = '{}';'''.format(update_details, confirm_id)
            cur.execute(query)

            print("First Name updated successfully")
            check_output(["zenity", "--info", "--width=400", "--height=200",
                          "--text=First Name updated successfully!!!!"])
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as error:
            print("ERROR : psycopg2.OperationalError - inside process_update_table function : " + str(error))
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=Please contact admin!!!!"])

    if update_option == 2:
        try:
            conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
                                    port="5432")
            cur = conn.cursor()
            print("Connection success")

            query = '''UPDATE ''' + check_main_table + ''' SET "Last_Name" = '{}'
            WHERE "ID" = '{}';'''.format(update_details, confirm_id)
            cur.execute(query)

            print("Last Name updated successfully")
            check_output(["zenity", "--info", "--width=400", "--height=200",
                          "--text=Last Name updated successfully!!!!"])
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as error:
            print("ERROR : psycopg2.OperationalError - inside process_update_table function : " + str(error))
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=Please contact admin!!!!"])

    if update_option == 3:
        try:
            conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
                                    port="5432")
            cur = conn.cursor()
            print("Connection success")

            query = '''UPDATE ''' + check_main_table + ''' SET "Email_ID" = '{}'
            WHERE "ID" = '{}';'''.format(update_details, confirm_id)
            cur.execute(query)

            print("Email ID updated successfully")
            check_output(["zenity", "--info", "--width=400", "--height=200",
                          "--text=Email ID updated successfully!!!!"])
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as error:
            print("ERROR : psycopg2.OperationalError - inside process_update_table function : " + str(error))
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=Please contact admin!!!!"])

    if update_option == 4:
        try:
            conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
                                    port="5432")
            cur = conn.cursor()
            print("Connection success")

            query = '''UPDATE ''' + check_main_table + ''' SET "Phone_No" = '{}'
            WHERE "ID" = '{}';'''.format(update_details, confirm_id)
            cur.execute(query)

            print("Phone no updated successfully")
            check_output(["zenity", "--info", "--width=400", "--height=200",
                          "--text=Phone no updated successfully!!!!"])
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as error:
            print("ERROR : psycopg2.OperationalError - inside process_update_table function : " + str(error))
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=Please contact admin!!!!"])

    if update_option == 5:
        try:
            conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
                                    port="5432")
            cur = conn.cursor()
            print("Connection success")

            query = '''UPDATE ''' + check_main_table + ''' SET "Employer" = '{}'
            WHERE "ID" = '{}';'''.format(update_details, confirm_id)
            cur.execute(query)

            print("Employer details updated successfully")
            check_output(["zenity", "--info", "--width=400", "--height=200",
                          "--text=Employer details updated successfully!!!!"])
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as error:
            print("ERROR : psycopg2.OperationalError - inside process_update_table function : " + str(error))
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=Please contact admin!!!!"])

    if update_option == 6:
        try:
            conn = psycopg2.connect(dbname="caregodb", user="postgres", password="postgres", host="127.0.0.1",
                                    port="5432")
            cur = conn.cursor()
            print("Connection success")

            query = '''UPDATE ''' + check_main_table + ''' SET "Role" = '{}'
            WHERE "ID" = '{}';'''.format(update_details, confirm_id)
            cur.execute(query)

            print("Role details updated successfully")
            check_output(["zenity", "--info", "--width=400", "--height=200",
                          "--text=Role details updated successfully!!!!"])
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as error:
            print("ERROR : psycopg2.OperationalError - inside process_update_table function : " + str(error))
            check_output(["zenity", "--error", "--width=400", "--height=200", "--text=Please contact admin!!!!"])


def process_response(check_main_table, response, flag):
    """
    ************************************ Inside process_response function **********************************************
    Function to validate the user response.

    This function will call other functions based on the response chosen by the user. If the response is None or at the
    end of all steps, this function will set the flag as 2. Which means the first iteration is finish and will enter
    into the second iteration.
    ************************************ Inside process_response function **********************************************
    """

    if response is not None:
        details = process_get_details_initial_option()
        if details is not None:
            option = process_assign_update_option(details)
            if option is not None:
                update_details, update_option = process_get_details_validation(option)
                if update_details is not None:
                    confirm_id = process_get_id_confirmation()
                    if confirm_id is not None:
                        confirm_table_id = process_search_id(check_main_table, confirm_id)
                        print("ID present in table : ", confirm_table_id)
                        if confirm_table_id == 1:
                            process_update_table(check_main_table, update_details, update_option, confirm_id)
                        else:
                            if confirm_table_id == 0:
                                print("ERROR : There are no data as per your search - "
                                      "inside process_response function.")
                                check_output(["zenity", "--error", "--width=400", "--height=200",
                                              "--text=There are no data as per your search!!!!"])
                            else:
                                print("ERROR : ID searched in table has more than one data - "
                                      "inside process_response function : ", str(confirm_id))
                                check_output(["zenity", "--error", "--width=400", "--height=200",
                                              "--text=ALERT!!!\n\nPlease contact admin!!!!"])

        flag = 2

    return flag


def process_ask_multiple(check_main_table, flag, status):
    """
    ************************************ Inside process_ask_multiple function ******************************************
    This function is a loop function that will run until the user chose not to update anymore.
    ************************************ Inside process_ask_multiple function ******************************************
    """

    while status == 0:
        response = process_ask_question(flag)
        process_response(check_main_table, response, flag)


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    region = process_parameter_set()
    check_main_table, check_sequence_table = process_checking_region_table(region)
    response = process_ask_question(flag=1)
    flag = process_response(check_main_table, response, flag=0)
    process_ask_multiple(check_main_table, flag, status=0)
    exit_program()


if __name__ == "__main__":
    main()
