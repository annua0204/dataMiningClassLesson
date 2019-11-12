# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

def  sample_1():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()
    pass

# 直方圖（Histogram）
def sample_2_1():
    # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
    normal_samples = np.random.normal(size=100000)
    uniform_samples = np.random.uniform(
        size=100000)  # 生成 100000 組介於 0 與 1 之間均勻分配隨機變數

    plt.hist(normal_samples)
    plt.show()
    plt.hist(uniform_samples)
    plt.show()
    pass

# 散佈圖（Scatter plot
def sample_2_2():
    speed = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15,
             15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
    dist = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26,
        54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]
    plt.scatter(speed, dist)
    plt.show()
    pass

# 線圖（Line plot）
def sample_2_3():
    speed = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15,
             15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
    dist = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26,
        54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]
    plt.plot(speed, dist)
    plt.show()
    pass

#長條圖（Bar plot）
def sample_2_4():
    cyl = [6 ,6 ,4 ,6 ,8 ,6 ,8 ,4 ,4 ,6 ,6 ,8 ,8 ,8 ,8 ,8 ,8 ,4 ,4 ,4 ,4 ,8 ,8 ,8 ,8 ,4 ,4 ,4 ,8 ,6 ,8 ,4]
    labels, values = zip(*Counter(cyl).items())
    indexes = np.arange(len(values))

    print(indexes)
    print(values)
    print(labels)

    plt.bar(indexes, values, width = 0.5)
    plt.xticks(indexes, labels)
    plt.show()
    pass

    # 長條圖
def sample_2_4_1():
    labels = ['Physics', 'Chemistry', 'Literature', 'Peace']
    foo_data = [3, 6, 10, 4]
    bar_width = 0.5
    xlocations = np.array(range(len(foo_data))) + bar_width
    plt.bar(xlocations, foo_data, width=bar_width)
    # plt.xticks(xlocations, labels)
    plt.title('Stock Price')
    plt.show()
    pass

def  sample_2_4_2():
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()
    pass

#盒鬚圖（Box plot）
def sample_2_5():
    # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
    normal_samples = np.random.normal(size=100000)
    plt.boxplot(normal_samples)
    plt.show()
    pass


sample_2_4_1()
