
from flask import Flask, render_template, request, flash, session, redirect, url_for
from forms import SignupForm, SigninForm
from intro_to_flask import app
from models import db, User



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'email' in session:
        return redirect(url_for('profile'))
    form = SignupForm()
        
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.username.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['email'] = newuser.email
            return redirect(url_for('profile'))
    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
    
    if 'email' not in session:
        return redirect(url_for('signin'))
        
    user = User.query.filter_by(email = session['email']).first()
            
    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html',username = user.username)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if 'email' in session:
        return redirect(url_for('profile'))
    form = SigninForm()
        
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signin.html', form=form)
        else:
            session['email'] = form.email.data
            return redirect(url_for('profile'))
                
    elif request.method == 'GET':
        return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
    
    if 'email' not in session:
        return redirect(url_for('signin'))
        
    session.pop('email', None)
    return redirect(url_for('home'))