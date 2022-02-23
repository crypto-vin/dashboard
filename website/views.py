from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Accounts
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    if request.method == 'POST':
        id = request.form.get('id')
        username = request.form.get('userName')
        password = request.form.get('password')
        phone = request.form.get('phone')

        account = Accounts.query.filter_by(username=username).first()
        phone_exists = Accounts.query.filter_by(phone=phone).first()
        if account:
            flash('User already Exists!', category='error')
        elif phone_exists:
            flash('Phone number already taken!', category='error')
        else:
            new_account = Accounts(id=id, username=username, password=password, phone=phone, user_id=current_user.id)
            db.session.add(new_account)
            db.session.commit()
            flash('New Account added!', category='success')


    return render_template("add_user.html", user=current_user)

@views.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_profiles():
    
    return render_template("user_profile.html", user=current_user)

    
@views.route('/delete-account', methods=['GET', 'POST'])
@login_required
def delete_account():
    account_id = request.form.get("delete")
    account = db.session.query(Accounts).filter(Accounts.id==account_id).first()
    if account:
        db.session.delete(account)
        db.session.commit()
        flash('Account deleted!', category='success')
    else:
        flash(f'Account { account_id } not found!', category='error')

    return render_template("user_profile.html", user=current_user)


@views.route('/api', methods=['GET', 'POST'])
@login_required
def api():
    return render_template("api.html", user=current_user)

# API endpoint
@views.route('/api/v1/users/<string:phone>', methods=['GET', 'POST'])
def get_users_by_phone(phone):
    accounts = db.Table("Accounts", db.metadata, autoload=True, autoload_with=db.engine)
    try:
        account_exists = list(db.session.query(accounts).filter_by(phone=phone).first())
        print(account_exists)
        status = 'exists'
        user_data = jsonify({"Users":db.session.query(accounts).filter_by(phone=phone).first()})
        return user_data
    except:
        print('Account doesn\'t exist')
        status = 'null'
        return status
    
        