import mysql.connector
import json
config = {
    "user": "study_lim",
    "password": "123123",
    "host": "127.0.0.1",
    "database": "study_db",
    "port": "3306"
}


def logIn(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    except mysql.connector.Error as err:
        print(err)

def createEmp(sql,val):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        cursor.execute(sql,val)
        rere = cursor.fetchall()
        conn.commit()
        print(rere)
        print(sql,val)
        # print(total)
    except mysql.connector.Error as err:
        print(err)

def checkid(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        print(sql)
        total = cursor.execute(sql)

        print(total)

    except mysql.connector.Error as err:
        print(err)

def updateEmp(sql,val):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql,val)
        # cursor.fetchall()
        print(sql,val)
        conn.commit()
    except mysql.connector.Error as err:
        print(err)

def deleteEmp(sql,val):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql,val)
        # cursor.fetchall()
        print(sql,val)
        conn.commit()
    except mysql.connector.Error as err:
        print(err)

def getAllEmp(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        resultList = cursor.fetchall()
        for result in resultList:
            EMP_ID = result[0]
            PWD = result[1]
            NAME = result[2]
            BIR = result[3]
            PH = result[4]
            INTROD_ID = result[5]
            info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID, PWD, NAME, BIR, PH, INTROD_ID)
            print(info)
    except mysql.connector.Error as err:

        print(err)

def getKeywordRank(sql):

    try:
        print(sql)
        conn = mysql.connector.connect(**config)
        # print(conn)
        cursor = conn.cursor()
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        # print(total)
    except mysql.connector.Error as err:
        print(err)
    index = 0
    dictresult = dict()
    str =  []
    for result in rere:
        resultrow = dict()
        index+=1
        resultrow["RANK"] = index
        resultrow["SEARCH_WORD"] = result[1]
        resultrow["SEARCH_CNT"] = result[2]
        str.append(resultrow)
    # with open('file.txt', 'w', encoding='UTF-8') as file:
    #     json_val= file.write(json.dumps(str))
    json_val = json.dumps(str, ensure_ascii=False)
    print(str)
    print(json_val)
    return json_val

def increaseKeywordCnt(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]        print(rere)
        print(total)
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def insertKeyword(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def searchKeyword(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def getRecentStudyTime(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def getTodayStudyTime(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def insertStudyEndTime(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def insertStudyStartTime(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def selectAllStudyTime(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)

def studyStatus(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        rere = cursor.fetchall()
        print(rere)
        print(total)
    # for result in resultList:
    #     EMP_ID = result[0]
    #     PWD = result[1]
    #     NAME = result[2]
    #     BIR = result[3]
    #     PH = result[4]
    #     INTROD_ID = result[5]
    #     info = "EMP_ID:{},PWD:{},NAME:{},BIR:{},PH{},INTROD_ID{}".format(EMP_ID,PWD,NAME,BIR,PH,INTROD_ID)
    #
    #     print(info)
    except mysql.connector.Error as err:

        print(err)