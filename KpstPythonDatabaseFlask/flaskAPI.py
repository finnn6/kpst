from flask import Flask, session, render_template, redirect, request, url_for

import DBconn

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        id = request.args.get("id")
        pwd = request.args.get("pwd")
    DBconn.logIn(sql="SELECT COUNT(EMP_ID)  FROM TBL_EMP te WHERE EMP_ID = '{}'and PWD ='{}';"
                 .format(id,pwd))
    return "login"

@app.route('/createEmp', methods=['GET','POST'])
def createEmp():
    if request.method == 'GET':
        id =request.args.get("id")
        pwd = request.args.get("pwd")
        name = request.args.get("name")
        birth = request.args.get("birth")
        ph = request.args.get("ph")
        rec = request.args.get("rec")
    sql = "INSERT into TBL_EMP values (%s,%s,%s,%s,%s,%s);"
    val = (id,pwd,name,birth,ph,rec)
    DBconn.createEmp(sql, val)

    return "createEmp"

@app.route('/checkid', methods=['GET','POST'])
def chekid():
    if request.method == 'GET':
        id = request.args.get("id")
    DBconn.checkid(sql="select  EMP_ID  from TBL_EMP te where EMP_ID = '{}';"
                   .format(id))
    return "chekid"
#
@app.route('/updateEmp', methods=['GET','POST'])
def updateEmp():
    if request.method == 'GET':
        id = request.args.get("id")
        pwd = request.args.get("pwd")
        name = request.args.get("name")
        ph = request.args.get("ph")
    sql = "UPDATE TBL_EMP SET PWD=%s,NAME=%s,PH=%s WHERE EMP_ID=%s;"
    val = (pwd,name,ph,id)
    DBconn.updateEmp(sql, val)
    return "updateEmp"

@app.route('/deleteEmp', methods=['GET','POST'])
def deleteEmp():
    if request.method == 'GET':
        id = request.args.get("id")
        pwd = request.args.get("pwd")
    sql = "DELETE FROM TBL_EMP WHERE EMP_ID = %s and PWD = %s;"
    val = (id,pwd)
    DBconn.deleteEmp(sql, val)
    return "deleteEmp"
#
@app.route('/getAllEmp', methods=['GET','POST'])
def getAllEmp():
    if request.method == 'GET':
        id = request.args.get("id")
    sql = "select * from TBL_EMP WHERE EMP_ID= '{}';".format(id)
    print(sql)
    DBconn.getAllEmp(sql)
    return "getAllEmp"
#
#
@app.route('/getKeywordRank')
def getKeywordRank():
    sql = '''SELECT
                    @rownum:=@rownum+1 
                    ,SEARCH_WORD
                    ,SEARCH_CNT
                FROM
                    TBL_VOICE_REC tvr
                WHERE (SELECT @rownum:=0)=0
                ORDER BY SEARCH_CNT DESC'''
    result = DBconn.getKeywordRank(sql)
    return result

# @app.route('/increaseKeywordCnt')
# def increaseKeywordCnt():
#
#     return
#
# @app.route('/insertKeyword')
# def insertKeyword():
#
#     return
#
# @app.route('/searchKeyword')
# def searchKeyword():
#
#     return
#
#
# @app.route('/getRecentStudyTime')
# def getKeywordRank():
#
#     return
#
# @app.route('/getTodayStudyTime')
# def getKeywordRank():
#
#     return
#
# @app.route('/insertStudyEndTime')
# def getKeywordRank():
#
#     return
#
# @app.route('/insertStudyStartTime')
# def getKeywordRank():
#
#     return
#
# @app.route('/selectAllStudyTime')
# def getKeywordRank():
#
#     return
#
# @app.route('/studyStatus')
# def getKeywordRank():
#
#     return

if __name__ == '__main__':
    app.run(debug=True)

