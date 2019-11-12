# -*- coding: utf-8 -*-

import pymysql

connection = pymysql.connect(host='127.0.0.1', port=3306, user='annua', passwd='Sorrow0081', db='data_mining', charset='utf8mb4')
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)


def output(datas):
    f = open('outPut.txt', 'a')
    for data in datas:
        # f.write("\"" + data['ODR_CHRT'] + "\"," + data['ODR_DEPT'] + "," + data['ODR_PSRC'] + ",\"" + data['ODR_M_DR'] + "\","+data['AGAIN']+"\n")
        f.write( data['ODR_DEPT'] + "," + data['ODR_PSRC'] + "," + data['ODR_M_DR'] + ","+data['AGAIN']+"\n")
    pass


def getDatas():
    print('getDatas')
    result = cursor.execute("SELECT `ODR_CHRT`, `ODR_DEPT`, `ODR_PSRC`, `ODR_M_DR`, `AGAIN` FROM `2019_surger_datas` LIMIT 120000")
    datas = cursor.fetchall()
    output(datas)
    print('done')
    pass

getDatas()
