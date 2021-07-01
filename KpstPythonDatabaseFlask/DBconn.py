import mysql.connector

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

def createEmp(sql1):
    try:
        conn1 = mysql.connector.connect(**config)
        print(conn1)
        cursor1 = conn1.cursor()
        sql1
        cursor1.execute(sql1)
        rere1 = cursor1.fetchall()
        print(rere1)
        # print(total1)
    except mysql.connector.Error as err1:
        print(err1)

def checkid(sql):
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

def updateEmp(sql):
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

def getAllEmp(sql):
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

def getKeywordRank(sql):
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