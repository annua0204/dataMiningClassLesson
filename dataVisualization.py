# -*- coding: utf-8 -*-

import pymysql
import matplotlib.pyplot as plt
import numpy as np

from collections import Counter

connection = pymysql.connect(host='127.0.0.1', port=3306, user='annua', passwd='Sorrow0081', db='data_mining', charset='utf8mb4')
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

def test():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Men')
    rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()
    plt.show()
    pass

def drawDataVisual(array):
    print('drawDataVisual')
    width = 0.25  # the width of the bars
    x = np.arange(len(array[0]['indexes']))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, array[0]['values'], width, label=u'out-patient clinic')
    rects2 = ax.bar(x, array[1]['values'], width, label=u'admission')
    rects3 = ax.bar(x + width, array[2]['values'], width, label=u'emergency')
    
    print(array[0]['indexes'])

    ax.set_ylabel(u'surger again record count.')
    ax.set_xlabel(u'dept')
    ax.set_xticks(x)
    ax.set_xticklabels(array[0]['indexes'])
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    fig.tight_layout()
    plt.show()
    pass

def formatData(datas, dept_datas):
    print('formatData')
    # 病人來源 O: 門診, I: 住院, E: 急診
    indexes = []
    values_O = []
    values_I = []
    values_E = []

    for dept_data in dept_datas:
        indexes.append(dept_data['ODR_DEPT'])
        v_o = 0
        v_i = 0
        v_e = 0
        for data in datas:
            if (dept_data['ODR_DEPT'] == data['ODR_DEPT']):
                if (data['ODR_PSRC'] == 'O'):
                    v_o = data['C']
                elif (data['ODR_PSRC'] == 'I'):
                    v_i = data['C']
                elif (data['ODR_PSRC'] == 'E'):
                    v_e = data['C']
        
        values_O.append(v_o)
        values_I.append(v_i)
        values_E.append(v_e)

    r = []
    r.append({
        'indexes': indexes,
        'values': values_O
    })
    r.append({
        'indexes': indexes,
        'values': values_I
    })
    r.append({
        'indexes': indexes,
        'values': values_E
    })
    # r['] = indexes
    # r['values'] = values
    # r['labels'] = indexes
    # print(r)
    return r

def get_sql():
    select_sql = "SELECT ODR_DEPT , ODR_PSRC, count(AGAIN) as C FROM `2019_surger_datas` GROUP by ODR_DEPT , ODR_PSRC order by ODR_DEPT , ODR_PSRC"
    return select_sql

def getDatas():
    print('getDatas')
    data_array = []
    result = cursor.execute(get_sql())
    datas = cursor.fetchall()

    result2 = cursor.execute("SELECT ODR_DEPT FROM `2019_surger_datas` GROUP by ODR_DEPT order by ODR_DEPT")
    dept_datas = cursor.fetchall()

    r = formatData(datas, dept_datas)
    drawDataVisual(r)

    print('done')
    pass


getDatas()
# test()
