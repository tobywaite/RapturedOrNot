import simplejson as json

from rapturedornot import app
from models import *

from flask import render_template, flash, url_for, redirect
from flaskext import wtf
from flaskext.wtf import validators

from google.appengine.ext import db

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/loginplz')
def loginplz():
    return render_template('loginplz.html')

@app.route('/create', methods=['POST'])
def create():
    session['username'] = session.get('fb_id')
    new_voter = db.get(session.get('fb_id'))
    if new_voter is None:
        new_voter = Voter(fb_id = session.get('fb_id'),
                          friends = json.loads(session.get('friends')),
                          votes = [])
        db.put(new_voter)
    return redirect(url_for('show', fb_id, 0))

@app.route('/show/<fb_id>/<int:which_friend>')
def show(fb_id, which_friend):
    return render_template('base.html')
    
