import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

import MySQLdb

# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="put your username here",         # your username
#                      passwd=" put your passwork here",  # your password
#                      db="bus_data")        # name of the data base

# cur = db.cursor()

# Use all the SQL you like

# cur.execute("SELECT stop_id, location FROM stopids WHERE route_number = '54A' ")

# print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row[0:2])

# db.close()

# @app.route('/postmethod', methods = ['POST'])
# def get_post_javascript_data():
#     jsdata = request.form['javascript_data']
#     return jsdata

from flask import Flask, render_template, request


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/tracker/')
def tracker_page():
    return render_template('tracker.html')

def post_route():    
     bus_route = request.form['route']
     return bus_route


if __name__ == '__main__':
    app.run()
    