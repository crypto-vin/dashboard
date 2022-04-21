from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


# init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# access the existing database
accounts = db.Table("Accounts", db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
def index():
    return 'Basic RESTful API with Flask'

@app.route('/api/v1/users', methods=["GET"])
def get_users():
    return jsonify({"Users":db.session.query(accounts).all()})

@app.route('/api/v1/users/<string:phone>', methods=["GET"])
def get_users_by_phone(phone):
    account_exists = db.session.query(accounts).filter_by(phone=phone).first()
    print(account_exists)
    if account_exists:
        return jsonify({"Users":db.session.query(accounts).filter_by(phone=phone).first()})
    else:
        return 'null'
    


if __name__ == '__main__':
    app.run(port=5001, debug=True)