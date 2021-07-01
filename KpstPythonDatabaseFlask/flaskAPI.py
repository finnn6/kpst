from flask import Flask, session, render_template, redirect, request, url_for

import test

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login')
def login():
    # id = request.get
    test.logIn(sql="SELECT COUNT(EMP_ID)  FROM TBL_EMP te WHERE EMP_ID = 'sys'and PWD ='123123';")
    return

@app.route('/createEmp')
def createEmp():

    return

@app.route('/checkid')
def chekid():

    return

@app.route('/updateEmp')
def updateEmp():

    return

@app.route('/getAllEmp')
def getAllEmp():

    return

@app.route('/deleteEmp')
def deleteEmp():

    return

@app.route('/getKeywordRank')
def getKeywordRank():

    return

@app.route('/increaseKeywordCnt')
def increaseKeywordCnt():

    return

@app.route('/insertKeyword')
def insertKeyword():

    return

@app.route('/searchKeyword')
def searchKeyword():

    return

@app.route('/getRecentStudyTime')
def getKeywordRank():

    return

@app.route('/getTodayStudyTime')
def getKeywordRank():

    return

@app.route('/insertStudyEndTime')
def getKeywordRank():

    return

@app.route('/insertStudyStartTime')
def getKeywordRank():

    return

@app.route('/selectAllStudyTime')
def getKeywordRank():

    return

@app.route('/studyStatus')
def getKeywordRank():

    return

if __name__ == '__main__':
    app.run(debug=True)

