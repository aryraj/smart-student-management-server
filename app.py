from flask import Flask, jsonify, make_response
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'usn' : ['1DS15EE001', '1DS15EE002', '1DS15EE003', '1DS15EE004', '1DS15EE005'],
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    }
]

@app.route('/', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})

@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == "__main__":
    app.run()
