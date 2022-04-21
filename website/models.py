from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    user_accounts = db.relationship('Accounts')

class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(100))
    phone = db.Column(db.String(20), unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def authenticate(username):
        accounts = db.Table("Accounts", db.metadata, autoload=True, autoload_with=db.engine)
        account_exists = list(db.session.query(accounts).filter_by(username=username).first())
        if account_exists:
            print('The account is valid')
            return 'exists'
        else:
            print('Invalid account!')
            return 'null'

    def __repr__(self):
        return f'<User: {self.username}>'

if __name__ == '__main__':
    Accounts.authenticate('Vin')
