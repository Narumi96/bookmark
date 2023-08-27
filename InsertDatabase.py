import mysql.connector
import pandas as pd
"""
@author: MD23002
"""
def InsertData():

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
        sql = ("""select * from bookmark""")

        #param = ('Bookmark',)

        cursor.execute(sql)
        result = cursor.fetchall()

        #print(result[0][1])

        # for (first_name, last_name, gender) in cursor:
        #     print(f"{first_name} {last_name} ({gender})")
        cursor.close()
        return result

    except Exception as e:
        print(f"Error Occurred: {e}")

    # finally:
    #     if cnx is not None and cnx.is_connected():
    #         cnx.close()

