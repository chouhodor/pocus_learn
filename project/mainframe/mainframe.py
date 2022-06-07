from email.mime import application
from flask import Blueprint, render_template, request, flash, send_from_directory
from flask.helpers import url_for
from flask.wrappers import Request
from werkzeug.utils import redirect 
from flask_login import login_required, current_user
from datetime import date, datetime
from ..models import User, OAuth
from .. import db 

mainframe = Blueprint('mainframe', __name__, template_folder='templates', static_folder='static')


def convert_date(date):
    if date != None:
        date = date.strftime("%d-%m-%y")
        return date

def disable(x):
    y = 'disabled'
    z = ''
    if x == 1:
        return y
    else:
        return z

def empty(d):
    x = ' '
    if d == None:
        return x
    else:
        return d


@mainframe.route('/',  methods=['POST','GET'])
def index():
      
    return render_template('index.html', 
    disable=disable,
    empty=empty,
    convert_date=convert_date,
    nav_index = True
    )

@mainframe.route('/usg',  methods=['POST','GET'])
def usg():
      
    return render_template('usg.html', 
    disable=disable,
    empty=empty,
    convert_date=convert_date,
    nav_index = True
    )