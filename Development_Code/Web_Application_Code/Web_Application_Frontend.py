#!/usr/bin/env python3

import os
import subprocess
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'


@app.route('/robotic-greeter')
def main_process_html():
    passing_arg = "main_process"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Speech_Emergency_Evacuation_Procedures.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        os.system("python3 " + program_name + " " + passing_arg + " &")

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
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        os.system("python3 " + program_name + " " + passing_arg + " &")

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
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        os.system("python3 " + program_name + " " + passing_arg + " &")

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
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        os.system("python3 " + program_name + " " + passing_arg + " &")

    return render_template('/Database_Customer_Update.html')


@app.route('/modify-user')
def modify_user_html():
    return render_template('/Modify_User.html')


@app.route('/robotic-greeter-search-user')
def database_customer_search_html():
    passing_arg = "customer_search"
    program_name = "Web_Application_Backend.py"
    args_call = "ps -ef|grep 'python3 Customer_Update.py'|grep -v 'grep'|awk '{print $8}'"
    try:
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        os.system("python3 " + program_name + " " + passing_arg + " &")

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
        output = subprocess.check_output(args_call, shell=True)
        output = output.decode().split('\n')
    except subprocess.CalledProcessError:
        output = []

    print(len(output))
    if len(output) == 1:
        os.system("python3 " + program_name + " " + passing_arg + " &")

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
