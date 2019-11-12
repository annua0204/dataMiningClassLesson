#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
from datetime import datetime

connection = pymysql.connect(host='127.0.0.1', port=3306, user='annua', passwd='Sorrow0081', db='data_mining', charset='utf8mb4')
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
select_sql = "SELECT `ID`, `ODR_CHRT`, `ODR_TXDT` FROM `2019_surger_datas` WHERE `ODR_CHRT` IN(SELECT `ODR_CHRT` FROM(SELECT `ODR_CHRT`, COUNT(*) c FROM `2019_surger_datas` GROUP BY `ODR_CHRT`) as c where c > 1) ORDER BY `ODR_CHRT`, `ODR_TXDT`"

def isInOneMonth(first_date, last_date):
    inOneMonth = False
    if (last_date['ODR_CHRT'] == first_date['ODR_CHRT']):
        delta = last_date['ODR_TXDT'] - first_date['ODR_TXDT']
        if (delta.days < 30):
            inOneMonth = True
    return inOneMonth

def updateRecord(data, again):
    data['AGAIN'] = again
    update_sql = "UPDATE `2019_surger_datas` SET `AGAIN`=%(AGAIN)s WHERE `ID`= %(ID)s"
    cursor.execute(update_sql, data)
    connection.commit()
    pass

def checkDatas(datas, datas_len):
    index = 0
    for  data  in datas:
        if (index == (datas_len - 1)):
            updateRecord(data, "0")
        else:
            if (isInOneMonth(data, datas[(index + 1)])):
                updateRecord(data, "1")
            else:
                updateRecord(data, "0")
        index += 1
    pass

def  check_surger_again():
    print('start check_surger_again')
    result = cursor.execute(select_sql)
    datas = cursor.fetchall()
    checkDatas(datas, result)
    cursor.close()
    connection.close()
    print('done.')
    pass

check_surger_again()
