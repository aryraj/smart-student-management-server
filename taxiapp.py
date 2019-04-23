# Created by Aryan Raj on 27/03/2018

import os
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as hsh_pwd




                            #!-- Instruction for working with the code  --!#

### In terminal, cd into the directory this file is saved in and type 'python taxiapp.py runserver -d',
# without the quotes.
# Your server is now ready and listening on port 0.0.0.0:5000
# In a new terminal window type in the following command to add a new user

#               curl -u admin:root -i -X POST -H "Content-Type: application/json" -d '{"username":"username",
#                                              "password":"password","name":"name","email":"email","password":"password}

# Repeat the above step for however many number of users required.

# To view all the added users, fire up your browser and go to http://127.0.0.1:5000/view_users
# When prompted type in 'admin' as username and 'root' as password.

#  **This method is developed just for POC and is not scalable.**

                                    #!-- End of Instruction --!#



# initializing
app = Flask(__name__)

# Users will be stored in a Flask-SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# initializing database
db = SQLAlchemy(app)

# initializing authentication
auth = HTTPBasicAuth()

# object mapping
class User(db.Model):
    _tablename = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    _secure_password = db.Column(db.String(64))
    name = db.Column(db.String(32), index=True)
    email = db.Column(db.String(32), index=True)
    phone= db.Column(db.Integer, index=True)

    def __init__(self, username, name, email, phone):
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone


    # encrypting the password so that users' data is secured
    def _password(self, password):
        self._secure_password = hsh_pwd.encrypt(password)

    # verifying the password received through POST to the password
    # stored in db
    def auth_password(self, password):
        return hsh_pwd.verify(password, self._secure_password)


# authenticating the admin
@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == 'root':
        return True
    return False


# This function is for adding new users.

# Use the following format to add a new user. Until corresponding UI comes into picture

# curl -u admin:root -i -X POST -H "Content-Type: application/json" -d '{"username":"username",
# "password":"password","name":"name","email":"email","password":"password}


@app.route('/users', methods=['POST', 'GET'])
@auth.login_required
def add_users():
    username = request.json.get('username')
    password = request.json.get('password')
    name = request.json.get('name')
    email = request.json.get('email')
    phone = request.json.get('phone')
    if username is None or name is None or email is None\
            or phone is None or password is None:
        abort(400)
    user = User(username=username, name=name, email=email, phone=phone)
    user._password(password)
    db.session.add(user)
    db.session.commit()
    return ( jsonify({'username': user.username,
                    'name' : user.name,
                    'email' : user.email,
                    'phone' : user.phone}))

# This method is for viewing all the registered users.

# Open 'http://127.0.0.1:5000/view_users' in your browser and when prompted
# Type in 'admin' as username and 'root' as password

@app.route('/view_users', methods=['GET'])
@auth.login_required
def get_users():
    users = User.query.all()
    _u = []
    if users is not None:
        for u in users:
            _u.append([u.name, u.email, u.phone, u.username])

        return (jsonify(users=_u))




if __name__ == "__main__":
    # if database does not exist create a new one and then proceed
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
