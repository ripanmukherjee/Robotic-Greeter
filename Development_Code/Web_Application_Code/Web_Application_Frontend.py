#!/usr/bin/env python3
"""
# **********************************************************************************************************************
# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Web_Application_Frontend.py
# Author:       Somak Mukherjee
# Date:         Friday 24 June, 2020
# Version:      1
# **********************************************************************************************************************
# Description:  Web_Application_Frontend.py is the main python program which needs to run to access web application.
#               This program will first call home.html to show to home page in the web application. On the home page
#               in web application, based on customer selection, this program will call other html program. Also, this
#               program will call Web_Application_Backend.py process if user wants to do certain process.
# **********************************************************************************************************************
# NOTE 1:       This program can be run separately or as a stand-alone program as follow for testing purpose:
#               $ python3 Web_Application_Frontend.py
# **********************************************************************************************************************
"""

import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'


@app.route('/robotic-greeter')
def main_process_html():
    passing_arg = "main_process"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Main_Process.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        print("Checking if Main_Process.py is already running or not.")
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        print("Calling Web_Application_Backend.py for Main_Process.py")
        os.system("python3 " + program_name + " " + passing_arg + " &")
    else:
        print("Main_Process.py is already running.")

    return render_template('/Main_Process.html')


@app.route('/')
def home_html():
    return render_template('/Home.html')


@app.route('/company/about-carego')
def about_carego_html():
    return render_template('/About_Carego.html')


@app.route('/company/about-TELIA')
def about_telia_html():
    return render_template('/About_TELIA.html')


@app.route('/robotic-greeter-emergency-evacuation-procedure')
def speech_emergency_evacuation_procedure_html():
    passing_arg = "emergency_evacuation_procedure"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Speech_Emergency_Evacuation_Procedures.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        print("Checking if Speech_Emergency_Evacuation_Procedures.py is already running or not.")
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        print("Calling Web_Application_Backend.py for Speech_Emergency_Evacuation_Procedures.py")
        os.system("python3 " + program_name + " " + passing_arg + " &")
    else:
        print("Speech_Emergency_Evacuation_Procedures.py is already running.")

    return render_template('/Speech_Emergency_Evacuation_Procedure.html')


@app.route('/company/emergency-evacuation-procedure')
def emergency_evacuation_procedure_html():
    return render_template('/Emergency_Evacuation_Procedure.html')


@app.route('/robotic-greeter-register-new-user')
def database_customer_insert_html():
    passing_arg = "customer_insert"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Customer_Insert.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        print("Checking if Customer_Insert.py is already running or not.")
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        print("Calling Web_Application_Backend.py for Customer_Insert.py")
        os.system("python3 " + program_name + " " + passing_arg + " &")
    else:
        print("Customer_Insert.py is already running.")

    return render_template('/Database_Customer_Insert.html')


@app.route('/register-new-user')
def register_new_user_html():
    return render_template('/Register_New_User.html')


@app.route('/robotic-greeter-modify-user')
def database_customer_update_html():
    passing_arg = "customer_update"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Customer_Update.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        print("Checking if Customer_Update.py is already running or not.")
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        print("Calling Web_Application_Backend.py for Customer_Update.py")
        os.system("python3 " + program_name + " " + passing_arg + " &")
    else:
        print("Customer_Update.py is already running.")

    return render_template('/Database_Customer_Update.html')


@app.route('/modify-user')
def modify_user_html():
    return render_template('/Modify_User.html')


@app.route('/robotic-greeter-search-user')
def database_customer_search_html():
    passing_arg = "customer_search"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Customer_Search_Main.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        print("Checking if Customer_Search_Main.py is already running or not.")
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        print("Calling Web_Application_Backend.py for Customer_Search_Main.py")
        os.system("python3 " + program_name + " " + passing_arg + " &")
    else:
        print("Customer_Search_Main.py is already running.")

    return render_template('/Database_Customer_Search.html')


@app.route('/search')
def search_html():
    return render_template('/Search.html')


@app.route('/contact-us')
def contact_us_html():
    return render_template('/Contact_US.html')


@app.route('/robotic-greeter-view-report')
def view_report():
    passing_arg = "view_report"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Carego_Customer_Reports.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        print("Checking if Carego_Customer_Reports.py is already running or not.")
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        print("Calling Web_Application_Backend.py for Carego_Customer_Reports.py")
        os.system("python3 " + program_name + " " + passing_arg + " &")
    else:
        print("Carego_Customer_Reports.py is already running.")

    return render_template('/View_Report.html')


@app.route('/admin-logged-in')
def admin_logged_in():
    return render_template('/Admin_Logged_In.html')


@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login_html():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return admin_logged_in()
    return render_template('Admin_Login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
