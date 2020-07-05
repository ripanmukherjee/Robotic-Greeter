
import os
import sys
import subprocess
from pathlib import Path
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
    print('Starting program : Web_Application_Backend.py - at : ' + current_time + ' on : ' + current_date)


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
    print('Ending program : Web_Application_Backend.py - At: ' + current_time + ' on : ' + current_date)
    sys.exit()


def process_parameter_set():
    """
    ************************************ Inside process_parameter_set function *****************************************
    This function will be called to set the essential parameter needed for this program as below:

    1. Region = "DEV" signifies that we are running the code in the development region. And as per the region value,
    this program will choose the table. So, it is essential to set region value correctly.
    2. main_directory = "/home/somak/Robotic-Greeter/Development_Code" signifies that we are assigning this directory
    as main_directory, because Development_Code folder has all the other codes to run this process.

    All the above values will be returning from this function, and other functions will use these parameters. So, it
    is essential to verify the parameter before running this process.
    ************************************ Inside process_parameter_set function *****************************************
    """

    region = "DEV"
    main_directory = "/home/somak/Robotic-Greeter/Development_Code"

    return region, main_directory


def process_checking_directory():
    """
    ************************************ Inside process_checking_directory function ************************************
    Function to validate all directory.

    This function will be called to check if codes related folder such as Database_Code, Face_Recognition_Code,
    and Speech_Recognition_Code is present inside of Main_Directory or not. If the directory is not present, then this
    function will give error and will exit from the program.
    ************************************ Inside process_checking_directory function ************************************
    """

    database_code_directory = Path("Database_Code")
    speech_recognition_code_directory = Path("Speech_Recognition_Code")
    main_process_directory = Path("Main_Process")

    if database_code_directory.exists() is False:
        print("ERROR : Directory : Database_Code is not present - inside process_checking_directory function.")
        exit_program()
    elif speech_recognition_code_directory.exists() is False:
        print("ERROR : Directory : Speech_Recognition_Code is not present - inside process_checking_directory "
              "function.")
        exit_program()
    elif main_process_directory.exists() is False:
        print("ERROR : Directory : Main_Process is not present - inside process_checking_directory "
              "function.")
        exit_program()
    else:
        pass

    return database_code_directory, speech_recognition_code_directory, main_process_directory


def process_check_input_argument():
    """
    ************************************ Inside process_check_input_argument function **********************************
    This function will decide if this program will run as stand-alone or not.

    It will receive an input argument from the Web_Application_Frontend.py and it will set the passing_arg to the input
    argument. If this function does not receive any argument, it will pass "0" as an argument.
    ************************************ Inside process_check_input_argument function **********************************
    """

    try:
        print('Inside Web_Application_Backend.py - Input Argument is : ', sys.argv[1])
        passing_arg = sys.argv[1]
    except IndexError:
        print('Processing Web_Application_Backend.py stand alone')
        passing_arg = "0"

    return passing_arg


def validation_call(passing_arg, main_directory, database_code_directory, speech_recognition_code_directory,
                    main_process_directory):
    """
    ************************************ Inside validation_call function ***********************************************
    This function will validate the input argument and will call the respective program.
    ************************************ Inside validation_call function ***********************************************
    """

    if passing_arg == "emergency_evacuation_procedure":
        os.chdir(speech_recognition_code_directory)
        try:
            program_name = "Speech_Emergency_Evacuation_Procedures.py"
            args_call = "python3 " + program_name
            check_output(args_call, shell=True)
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside emergency_evacuation_procedure argument")

        os.chdir(main_directory)

    elif passing_arg == "customer_insert":
        os.chdir(database_code_directory)
        try:
            program_name = "Customer_Insert.py"
            args_call = "python3 " + program_name
            check_output(args_call, shell=True)
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside customer_insert argument.")

        os.chdir(main_directory)

    elif passing_arg == "customer_update":
        os.chdir(database_code_directory)
        try:
            program_name = "Customer_Update.py"
            args_call = "python3 " + program_name
            check_output(args_call, shell=True)
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside customer_update argument.")

        os.chdir(main_directory)

    elif passing_arg == "customer_search":
        os.chdir(database_code_directory)
        try:
            program_name = "Customer_Search_Main.py"
            args_call = "python3 " + program_name
            check_output(args_call, shell=True)
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside customer_update argument.")

        os.chdir(main_directory)

    elif passing_arg == "main_process":
        os.chdir(main_process_directory)
        try:
            program_name = "Main_Process.py"
            args_call = "python3 " + program_name
            check_output(args_call, shell=True)
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside main_process argument.")

        os.chdir(main_directory)

    elif passing_arg == "view_report":
        os.chdir(main_process_directory)
        try:
            program_name = "Carego_Customer_Reports.py"
            args_call = "python3 " + program_name
            check_output(args_call, shell=True)
        except subprocess.CalledProcessError:
            print("ERROR : subprocess.CalledProcessError - inside view_report argument.")

        os.chdir(main_directory)

    else:
        print('Not a valid input argument : ', str(passing_arg))


def main():
    """
    ************************************ Inside main function **********************************************************
    This is the main process which will call at the very beginning and will call the other functions.
    ************************************ Inside main function **********************************************************
    """

    start_program()
    region, main_directory = process_parameter_set()
    os.chdir(main_directory)
    database_code_directory, speech_recognition_code_directory, main_process_directory = process_checking_directory()
    passing_arg = process_check_input_argument()
    validation_call(passing_arg, main_directory, database_code_directory, speech_recognition_code_directory,
                    main_process_directory)
    exit_program()


if __name__ == "__main__":
    main()