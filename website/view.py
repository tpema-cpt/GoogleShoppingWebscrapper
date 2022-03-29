from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .setup import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')


    return render_template("home.html", user=current_user)

