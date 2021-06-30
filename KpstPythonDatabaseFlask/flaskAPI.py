from flask import Flask, session, render_template, redirect, request, url_for

import DBconn

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/logIn')
def login():
    # id = request.get
    DBconn.logIn(sql="SELECT COUNT(EMP_ID)  FROM TBL_EMP te WHERE EMP_ID = 'sys'and PWD ='123123';")
    return

if __name__ == '__main__':
    app.run(debug=True)

