from liveyoursport import app, db
from user.form import ResgisterForm, LoginForm
from flask import render_template, redirect, url_for, session, request
from user.models import User
from user.forms import LoginForm, ResgisterForm
import bcrypt

@app.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next')

    if form.validate_on_submit():
        user = User.query.filter_by(
            username = form.username.data.lower(),
        ).first()
        if user:
            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['username'] = form.username.data
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                return redirect(url_for('index'))
        else:
            error = 'Incorrect Username and Password'
    return render_template('user/login.html', form=form, error=error)

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect( url_for('login'))


@app.route('/signup', methods=('GET','POST'))
def signup():
    form = ResgisterForm()
    error = None
    # import pdb; pdb.set_trace()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        full_name = form.first_name.data + ' ' + form.last_name.data
        user = User(
            full_name,
            form.first_name.data,
            form.last_name.data,
            form.email.data,
            form.username.data.lower(),
            hashed_password,
            )
        db.session.add(user)
        try:
            db.session.commit()
            session['username'] = form.username.data
        except:
            error = "Username or Email Already exist"
            return render_template('user/signup.html', form=form,error=error)
        return redirect( url_for('index'))
    return render_template('user/signup.html', form=form,error=error)
