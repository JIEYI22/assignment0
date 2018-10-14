import csv #导入CSV
readings=['trade-wars-news1.txt',
          'trade-wars-news2.txt',
          'trade-wars-news3.txt',
          'trade-wars-news4.txt',
         'trade-wars-news5.txt'] #定义所有的readings

all_readings = [] #建立阅读库
for reading in readings: #读里边的每一篇=循环
    a=open(reading,'r') #打开-->读1，2，3，4篇文章
    content=a.read()#把a的内容赋给content
    all_readings.append(content)#把content加进all_reading的list中

all_words=[] #建立词语库
for i in range(5): #循环五篇阅读中的words
    words=all_readings[i].split()#将五篇文章撕开成独立的单词元素
    for all_word in words: #定义了的值需要记住
        all_words.append(all_word)#将all_word加入到词语库中

from collections import Counter #从collections 库中导入计算器
count = Counter() #定义计算 count=cnt
for a in all_words: #循环计算all_words中的所有单词
    count[a] += 1 #count[a]=count[a]+1 单词a每出现一次就会+1
print(count.most_common()) #打印最常出现的词频

#count.most_common()

with open ('count_all_word.csv','w')as f: #输出为CSV格式
    mywriter=csv.writer(f)
    header=['word','frequency']
    mywriter.writerow(header)
    mywriter.writerows(count.most_common())