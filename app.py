#!flask/bin/python
from flask import Flask,request,json,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'status': 200, 'message': "Python Rest API Server Successfully connected"})

@app.route('/html/view')
def html_view():
    return "<html><head><title>HTML</title></head><body><h1>Test Success</h1></body></html>"

@app.route('/employee/<int:id>')
def get_employee_id(id):
    if id > 1000 :
        return jsonify({'status':200,'message':"Given employee id is valid"})
    else:
        return jsonify({'status':400,'message':"Please enter valid id"})

@app.route('/employee/create', methods=['POST'])
def create_task():
    user = {
        'username': request.json['username'],
        'password': request.json['password'],
    }
    return jsonify({'employee': user,'status': 200,'message':'Employee Successfully created!'})

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == '__main__':
    app.run(debug=True)
