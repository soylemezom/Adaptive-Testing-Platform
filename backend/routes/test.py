from flask import Blueprint, render_template
from flask_login import login_required

test_bp = Blueprint('test', __name__)

@test_bp.route('/')
def index():
    return render_template('index.html')

@test_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@test_bp.route('/take-test')
@login_required
def take_test():
    return render_template('test.html')
