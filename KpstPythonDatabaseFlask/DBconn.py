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
