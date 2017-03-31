from liveyoursport import app
from flask import render_template, redirect, url_for, session, request
from user.decorator import login_required
from dashboard.models import Orders

@app.route('/')
@login_required
def index():
    return "This is index Page"
