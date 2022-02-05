from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from models import *
from . import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class AccountModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(100))
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'Account(username = {username}, password = {password}, status = {status})' 

#db.create_all() 

acc_put_args =  reqparse.RequestParser()
acc_put_args.add_argument("username", type=str, help="Account Username", required=True)
acc_put_args.add_argument("password", type=str, help="Account Password", required=True)
acc_put_args.add_argument("status", type=str, help="Account Status")



resource_fields = {
    'id' : fields.Integer,
    'username' : fields.String,
    'password' : fields.String,
    'status' : fields.String
}


class Acc(Resource):
    @marshal_with(resource_fields)
    def get(self, acc_id):
        result = Accounts.query.filter_by(id=acc_id).first()
        if not result:
            abort(404, message="Too bad the account doesnt exist")
        return result


 
api.add_resource(Acc, "/accounts/<int:acc_id>")

if __name__ == "__main__":
    app.run(debug=True)