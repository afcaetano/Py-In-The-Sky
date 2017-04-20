# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, url_for, render_template

app = Flask(__name__)

# Index -- some inocuous comment to version the file
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'Allan', 'age': 47},
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/hello')
@app.route('/hello/<string:name>')
def greet(name='Stranger'):
    return render_template('<html><head>Greetings</head><body><p>Hello <b>{{name}}</b>, how are you?</body></html>', name=name)
    # return '<html><head>Greetings</head><body><p>Hello <b>%s</b>, how are you?</body></html>' % name

@app.route('/env/')
def getEnv():
    return 'FOOBAR= [%s]' % os.getenv('FOOBAR')

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

def do_the_login():
    pass

def show_the_login_form():
    return '<html><head>Login</head><body><p>Login:</p></body></html>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
