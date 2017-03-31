from liveyoursport import app
from user.form import ResgisterForm, LoginForm
from flask import render_template, redirect, url_for, session, request
from user.models import User
from user.forms import LoginForm, ResgisterForm

@app.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    error = None

    # if request.method == 'GET' and request.args.get('next'):
    #     session['next'] = request.args.get('next')
    #
    # if form.validate_on_submit():
    #     user = User.query.filter_by(
    #         username = form.username.data,
    #     ).first()
    #     if user:
    #         if bcrypt.hashpw(form.password.data, user.password) == user.password:
    #             session['username'] = form.username.data
    #             session['is_author'] = user.is_author
    #             if 'next' in session:
    #                 next = session.get('next')
    #                 session.pop('next')
    #                 return redirect(next)
    #             return redirect(url_for('index'))
    #     else:
    #         error = 'Incorrect Username and Password'
    return render_template('user/login.html', form=form, error=error)


@app.route('/signup')
def signup():
    form = ResgisterForm()
    error = None
    return render_template('user/signup.html', form=form,error=error)
