import mysql.connector
import pandas as pd
import datetime
"""
@author: MD23002
"""
def CallingData(chatgpt):

    cnx = None

    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='hit_database',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='triplrs'  # データベース名
        )

        if cnx.is_connected():
            print("Mysql Connect success")

        if not cnx.is_connected():
            raise Exception("Mysql Connect unsuccess")

        cursor = cnx.cursor(buffered=True)

        #param = ('Bookmark',)
        activity = [chatgpt[i]["activity"] for i in range(len(chatgpt))]
        datetime = [chatgpt[i]["datetime"] for i in range(len(chatgpt))]

        data = [[0 for j in range(2)] for i in range(len(chatgpt))]
        for i in range(len(chatgpt)):
            data[i][0]=activity[i]
            data[i][1]=datetime[i]

        print(type(data))
        
        with cnx:
            with cnx.cursor() as cursor:
                sql = "insert into bookmark values(%s, %s)"
                cursor.executemany(sql,data)

            cnx.commit()

        # for (first_name, last_name, gender) in cursor:
        #     print(f"{first_name} {last_name} ({gender})")
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    # finally:
    #     if cnx is not None and cnx.is_connected():
    #         cnx.close()

