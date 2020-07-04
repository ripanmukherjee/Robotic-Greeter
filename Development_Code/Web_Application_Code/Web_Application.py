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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
