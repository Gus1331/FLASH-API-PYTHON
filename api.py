from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqParse, fields, marshal_with, abort


"""App and Api properties"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


"""Database Models"""
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
    

"""Args Configuration"""
user_args = reqParse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="You have to define a name for an user")
user_args.add_argument('email', type=str, required=True, help="You have to define an unique email for an user")


"""Exit JSON Data Definition"""
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
    }


"""Query"""
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()

        if not users:
            return [], 204
        
        return users, 200

    # reforce this concept later
    def post(self):
        args = user_args.parse_args() # validade args for data manipulation
        user = UserModel(name=args["name"], email=args["email"]) # converts args to data
        db.session.add(user) # change
        db.session.commit() # apply
        return user, 201

class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found! :(")
        return user
    
    @marshal_with(userFields)
    def put(self, id):
        user = UserModel.query.filter_by(id=id).first()

        if not user:
            abort(404, "User not found! :(")

        args = user_args.parse_args()
        updated_user = UserModel(name=args["name"], email=args["email"])

        user.name = updated_user.name
        user.email = updated_user.email

        db.session.commit()
        return user
    
    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()

        if not user:
            abort(404, "User not found! :(")

        db.session.delete(user)
        db.session.commit()
        return user, 204

"""Routes"""
@app.route('/')
def home():
    return '<h1>GUS Flask Rest API</h1>' 


"""Endpoints"""
api.add_resource(Users, '/users/') # function <- endpoint
api.add_resource(User, '/users/<int:id>')


"""Aplication initializer"""
if __name__ == '__main__':
    app.run(debug=True)