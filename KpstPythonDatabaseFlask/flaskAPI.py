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
    result =DBconn.getAllEmp(sql)
    return result

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

@app.route('/increaseKeywordCnt')
def increaseKeywordCnt():
    if request.method == 'GET' :
        keyword = request.args.get("keyword")
    sql = '''UPDATE TBL_VOICE_REC 
        SET SEARCH_CNT = SEARCH_CNT+1 
        WHERE SEARCH_WORD = '{}' '''.format(keyword)
    print(sql)
    result = DBconn.increaseKeywordCnt(sql)
    return result

@app.route('/insertKeyword')
def insertKeyword():
    if request.method == 'GET':
        keyword = request.args.get("keyword")
    sql = "INSERT into TBL_VOICE_REC values (nextval(SEQ_TBL_VOICE_REC),'"+keyword+"',1)".format(keyword)
    print(sql)
    result = DBconn.increaseKeywordCnt(sql)
    return result

@app.route('/searchKeyword')
def searchKeyword():
    if request.method == 'GET':
        keyword = request.args.get("keyword")
    sql = '''SELECT COUNT(SEARCH_WORD) 
        FROM TBL_VOICE_REC tvr 
        WHERE SEARCH_WORD = '{}' '''.format(keyword)
    print(sql)
    result = DBconn.searchKeyword(sql)
    return result

@app.route('/getRecentStudyTime')
def getRecentStudyTime():
    if request.method == 'GET':
        id = request.args.get("id")
    sql = f'''SELECT ts.STD_START , ts.STD_END 
        ,tss.SUB_NAME 
        FROM TBL_STD ts ,TBL_SUB_STD tss
        WHERE ts.SUB_ID = tss.SUB_ID
        AND ts.EMP_ID = '{id}'
        AND ts.STD_START > date_sub(now(), interval 1 day)
        ORDER BY ts.STD_SEQ DESC
        LIMIT 0,1 '''
    print(sql)
    result = DBconn.getRecentStudyTime(sql)
    return result

@app.route('/getTodayStudyTime')
def getTodayStudyTime():
    if request.method == 'GET':
        id = request.args.get("id")
    sql = '''SELECT STD_SEQ ,ts.STD_START ,ts.STD_END ,ts.EMP_ID,ts.SUB_ID,tss.SUB_NAME
        FROM TBL_STD ts,TBL_SUB_STD tss  
        WHERE  ts.SUB_ID = tss.SUB_ID 
        AND EMP_ID = '{}'
        AND STD_START > date_sub(now(), interval 1 day) 
        ORDER BY STD_SEQ DESC '''.format(id)
    print(sql)
    result = DBconn.getTodayStudyTime(sql)
    return result

@app.route('/insertStudyEndTime')
def insertStudyEndTime():
    if request.method == 'GET':
        id = request.args.get("id")
    sql = f'''UPDATE TBL_STD 
        SET
        STD_END = SYSDATE() 
        WHERE 
        EMP_ID = '{id}'
        AND STD_END = 'N' 
        ORDER  BY STD_SEQ DESC '''
    print(sql)
    result = DBconn.insertStudyEndTime(sql)
    return result

@app.route('/insertStudyStartTime')
def insertStudyStartTime():
    if request.method == 'GET':
        id = request.args.get("id")
        sub = request.args.get("sub")
    sql = f"INSERT into TBL_STD values (nextval(SEQ_TBL_VOICE_REC),SYSDATE(),'N','{id}', '{sub}')"
    print(sql)
    result = DBconn.insertStudyStartTime(sql)
    return result

@app.route('/selectAllStudyTime')
def selectAllStudyTime():
    if request.method == 'GET':
        id = request.args.get("id")
    sql = f'''SELECT ts.STD_SEQ ,ts.STD_START ,ts.STD_END ,ts.SUB_ID ,tss.SUB_NAME
        FROM TBL_STD ts ,TBL_SUB_STD tss
        WHERE ts.SUB_ID = tss.SUB_ID
        AND ts.EMP_ID = '{id}'
        ORDER BY STD_SEQ DESC'''.format(id)

    print(sql)
    result = DBconn.selectAllStudyTime(sql)
    return result

@app.route('/studyStatus')
def studyStatus():
    if request.method == 'GET':
        id = request.args.get("id")
    sql = f'''SELECT
        COUNT(T.STD_SEQ)
        FROM(SELECT * FROM TBL_STD ts WHERE EMP_ID = '{id}' AND STD_START > date_sub(now(), interval 1 day) ORDER BY STD_SEQ DESC LIMIT 0,1) T
        WHERE T.STD_END = 'N' '''
    print(sql)
    result = DBconn.studyStatus(sql)
    return result

if __name__ == '__main__':
    app.run(host='192.168.0.18',debug=True)

