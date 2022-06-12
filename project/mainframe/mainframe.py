from email.mime import application
from flask import Blueprint, render_template, request, flash, send_from_directory
from flask.helpers import url_for
from flask.wrappers import Request
from werkzeug.utils import redirect 
from flask_login import login_required, current_user
from datetime import date, datetime
from ..models import User, OAuth
from .. import db 
import re

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

def stage():
    stage = int(current_user.stage)
    return stage

def get_integer(i):
    i = int(re.search(r'\d+', i).group())
    return i

@mainframe.route('/',  methods=['POST','GET'])
def index():

      
    return render_template('index.html', 
    disable=disable,
    empty=empty,
    convert_date=convert_date,
    nav_index = True
    )

@mainframe.route('/pocus0',  methods=['POST','GET'])
@login_required
def pocus0():

    return render_template('usg.html', 
    nav_pocus0 = True,
    index = get_integer(request.path),
    previous ='mainframe.pocus0',
    user_stage = stage()
    )

@mainframe.route('/pocus1',  methods=['POST','GET'])
@login_required
def pocus1():

    video_path="https://drive.google.com/file/d/1hk1K_OnLr4mSGYrgRuKNYjcS__hlu9LR/preview"
    
        

    if stage() < 1:
        return redirect(request.referrer)
    else:
        return render_template('usg.html', 
        video_path=video_path,
        nav_pocus1 = True,
        index = get_integer(request.path),
        previous ='mainframe.pocus1',
        user_stage= stage()
        )

@mainframe.route('/pocus2',  methods=['POST','GET'])
@login_required
def pocus2():

    video_path="https://drive.google.com/file/d/1CguzD5uMVL6Os5_3w5MHA5j8CrgIj9LH/preview"
      
    if stage() < 2:
        return redirect(request.referrer)
    else:
        return render_template('usg.html', 
        video_path=video_path,
        nav_pocus2 = True,
        index = get_integer(request.path),
        previous ='mainframe.pocus2',
        user_stage=stage()
        )

@mainframe.route('/pocus3',  methods=['POST','GET'])
@login_required
def pocus3():

    video_path="https://drive.google.com/file/d/1GPFgGVuT-x2BJuV4Smqwsaj-sUkClAxA/preview"

    if stage() < 3:
        return redirect(request.referrer)
    else:
        return render_template('usg.html', 
        video_path=video_path,
        nav_pocus3 = True,
        index = get_integer(request.path),
        previous ='mainframe.pocus3',
        user_stage=stage()
        )

@mainframe.route('/pocus4',  methods=['POST','GET'])
@login_required
def pocus4():

    video_path="https://drive.google.com/file/d/13fygHJs4EslJmIs3CRO5FDuMWRCw7U6J/preview"

    if stage() < 4:
        return redirect(request.referrer)
    else:
        return render_template('usg.html', 
        video_path=video_path,
        nav_pocus4 = True,
        index = get_integer(request.path),
        previous ='mainframe.pocus4',
        user_stage=stage()
        )

@mainframe.route('/pocus5',  methods=['POST','GET'])
@login_required
def pocus5():

    video_path="https://drive.google.com/file/d/1ihLOrvXo-TA5edFILDBo3co6eoPGl1Ri/preview"

    if stage() < 5:
        return redirect(request.referrer)
    else:
        return render_template('usg.html', 
        video_path=video_path,
        nav_pocus5 = True,
        index = get_integer(request.path),
        previous ='mainframe.pocus4',
        user_stage=stage()
        )

@mainframe.route('/complete',  methods=['POST','GET'])
@login_required
def complete():

    return render_template('complete.html', 
    )





###############FORM ROUTES#########################

@mainframe.route('/next_stage',  methods=['POST'])
def next_stage():

    index = int(request.form['current_index'])

    if request.method == 'POST':
        current = User.query.get(current_user.id)
        
        if index < stage():
            return redirect(url_for('mainframe.pocus' + str(index+1)))
        else:
            current.stage = stage() + 1
            db.session.commit()
            return redirect(url_for('mainframe.pocus' + str(index+1)))
            


@mainframe.route('/test0',  methods=['POST','GET'])
@login_required
def test0():

    string1 = request.path
 
    return str(get_integer(string1))