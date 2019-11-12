#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
from datetime import datetime

connection = pymysql.connect(host='127.0.0.1', port=3306, user='annua',
                             passwd='Sorrow0081', db='data_mining', charset='utf8mb4')
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
select_sql = """SELECT `ID`,
CAST(((UNIX_TIMESTAMP(`ODR_AE`) - UNIX_TIMESTAMP(`ODR_AS`)) / 60) AS UNSIGNED) AS ODR_ANA_TIME,
CAST(((UNIX_TIMESTAMP(`ODR_OE`) - UNIX_TIMESTAMP(`ODR_OS`)) / 60) AS UNSIGNED) AS ODR_OP_TIME,
CAST(((UNIX_TIMESTAMP(`ODR_OT`) - UNIX_TIMESTAMP(`ODR_IN`)) / 60) AS UNSIGNED) AS ODR_OR_TIME
FROM(
    select `ID`,
    ADDTIME(`ODR_AS_D`, CONCAT(substring(`ODR_AS_T`, 1, 2), ":", substring(`ODR_AS_T`, 3, 2), ":00")) as ODR_AS,
    ADDTIME(`ODR_AE_D`, CONCAT(substring(`ODR_AE_T`, 1, 2), ":", substring(`ODR_AE_T`, 3, 2), ":00")) as ODR_AE,
    ADDTIME(`ODR_OS_D`, CONCAT(substring(`ODR_OS_T`, 1, 2), ":", substring(`ODR_OS_T`, 3, 2), ":00")) as ODR_OS,
    ADDTIME(`ODR_OE_D`, CONCAT(substring(`ODR_OE_T`, 1, 2), ":", substring(`ODR_OE_T`, 3, 2), ":00")) as ODR_OE,
    ADDTIME(`ODR_IN_D`, CONCAT(substring(`ODR_IN_T`, 1, 2), ":", substring(`ODR_IN_T`, 3, 2), ":00")) as ODR_IN,
    ADDTIME(`ODR_OT_D`, CONCAT(substring(`ODR_OT_T`, 1, 2), ":", substring(`ODR_OT_T`, 3, 2), ":00")) as ODR_OT
    from `2019_surger_datas`) as test"""


# def isInOneMonth(first_date, last_date):
#     inOneMonth = False
#     if (last_date['ODR_CHRT'] == first_date['ODR_CHRT']):
#         delta = last_date['ODR_TXDT'] - first_date['ODR_TXDT']
#         if (delta.days < 30):
#             inOneMonth = True
#     return inOneMonth


def updateTimes(data):
    print("updateTimes")
    print(data)
    update_sql = "UPDATE `2019_surger_datas` SET `ODR_ANA_TIME`=%(ODR_ANA_TIME)s, `ODR_OP_TIME`=%(ODR_OP_TIME)s, `ODR_OR_TIME`=%(ODR_OR_TIME)s WHERE `ID`= %(ID)s"
    cursor.execute(update_sql, data)
    connection.commit()
    pass

def checkDatas(datas, datas_len):
    print("checkDatas")
    for data in datas:
        print(data)
        updateTimes(data)
    pass

def main():
    print('main strart')
    result = cursor.execute(select_sql)
    datas = cursor.fetchall()
    checkDatas(datas, result)
    cursor.close()
    connection.close()
    print('done.')
    pass


main()
