from flask import Blueprint, render_template, redirect, url_for, flash
from backend.forms import LoginForm, RegisterForm
from backend.models import User, db
from flask_login import login_user, logout_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('test.dashboard'))
        flash("Invalid credentials")
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
