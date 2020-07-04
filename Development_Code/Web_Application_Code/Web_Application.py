#!/usr/bin/env python3
from flask import Flask, render_template
from subprocess import check_output

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'


@app.route('/')
def home():
    return render_template('/Home.html')


@app.route('/company/about-carego')
def about_carego():
    return render_template('/About_Carego.html')


@app.route('/company/about-TELIA')
def about_telia():
    return render_template('/About_TELIA.html')


@app.route('/company/emergency-evacuation-procedure')
def emergency_evacuation_procedure():
    return render_template('/Emergency-Evacuation-Procedure.html')


@app.route('/company/register-new-user')
def register_new_user():
    return render_template('/Register_New_User.html')


@app.route('/company/modify-user')
def modify_user():
    return render_template('/Modify_User.html')


@app.route('/company/search')
def search():
    return render_template('/Search.html')


@app.route('/company/contact-us')
def contact_us():
    return render_template('/Contact_US.html')


@app.route('/company/admin-login')
def admin_login():
    return render_template('/Admin_Login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
