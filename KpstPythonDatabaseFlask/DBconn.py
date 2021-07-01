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
        resultrow = dict()
        for result in resultList:
            resultrow["EMP_ID"]= result[0]
            resultrow["PWD"] = result[1]
            resultrow["NAME"] = result[2]
            resultrow["BIR"] = result[3]
            resultrow["PH"] = result[4]
            resultrow["INTROD_ID"] = result[5]
        print(resultrow)
        json_val = json.dumps(resultrow, ensure_ascii=False)
        return json_val
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

    except mysql.connector.Error as err:
        print(err)
    index = 0
    dictresult = dict()
    str = []
    for result in rere:
        resultrow = dict()
        index+=1
        resultrow["RANK"] = index
        resultrow["SEARCH_WORD"] = result[1]
        resultrow["SEARCH_CNT"] = result[2]
        str.append(resultrow)

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
        conn.commit()
        rere = cursor.fetchall()
        json_val = json.dumps(rere, ensure_ascii=False)
        return json_val
    except mysql.connector.Error as err:
        print(err)



def insertKeyword(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        conn.commit()
        rere = cursor.fetchall()
        json_val = json.dumps(rere, ensure_ascii=False)
        return json_val
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

        index = 0
        dictresult = dict()
        for result in rere:
            resultrow = dict()
            index += 1
            dictresult["SEARCH_WORD"] = result[0]
        json_val = json.dumps(dictresult, ensure_ascii=False)
        print(json_val)
        return json_val
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
        index = 0
        dictresult = dict()
        for result in rere:
            dictresult["STD_START"] = result[0]
            dictresult["STD_END"] = result[1]
            dictresult["SUB_NAME"] = result[2]

        json_val = json.dumps(dictresult, ensure_ascii=False)
        print(str)
        print(json_val)
        return json_val
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
        str = []
        for result in rere:
            dictresultrow = dict()
            dictresultrow["STD_START"] = result[0]
            dictresultrow["STD_END"] = result[1]
            dictresultrow["SUB_NAME"] = result[2]
            str.append(dictresultrow)
        json_val = json.dumps(str, ensure_ascii=False)
        print(str)
        print(json_val)
        return json_val
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
        conn.commit()
        rere = cursor.fetchall()
        json_val = json.dumps(rere, ensure_ascii=False)
        return json_val

    except mysql.connector.Error as err:
        print(err)

def insertStudyStartTime(sql):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        cursor = conn.cursor()
        sql
        total = cursor.execute(sql)
        conn.commit()
        rere = cursor.fetchall()
        json_val = json.dumps(rere, ensure_ascii=False)
        return json_val
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
        index = 0
        dictresult = dict()
        str = []
        for result in rere:
            dictresultrow = dict()
            dictresultrow["STD_START"] = result[0]
            dictresultrow["STD_END"] = result[1]
            dictresultrow["SUB_NAME"] = result[2]
            str.append(dictresultrow)
        json_val = json.dumps(str, ensure_ascii=False)
        print(str)
        print(json_val)
        return json_val
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
        dictresult = dict()
        for result in rere:
            dictresult["STUDY_STATUS"] = result[0]
            if(result[0]==0):
                print("ON")

            elif(result[0]!=0):
                print("OFF")
        json_val = json.dumps(dictresult, ensure_ascii=False)
        print(json_val)
        return json_val
    except mysql.connector.Error as err:

        print(err)