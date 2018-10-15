import csv 
readings=['trade-wars-news1.txt',
          'trade-wars-news2.txt',
          'trade-wars-news3.txt',
          'trade-wars-news4.txt',
         'trade-wars-news5.txt'] #创建新的列表

all_readings=[] #创建阅读库
for reading in readings: #建立阅读循环
    f=open(reading,'r') 
    content=f.read() #把读取的内容赋给content
    all_readings.append(content) #把content加入阅读库中

all_words=[] #创建词语库
for i in range(5): #建立循环读取词语
    words=all_readings[i].split() #split词语
    for word in words: 
        all_words.append(word) #把word加入到词语库中

from collections import Counter #从collections库中导入计算功能
count=Counter() #开始计算 
for a in all_words: #频率计算循环
    count[a]=count[a]+1 #count[a]=count[a]+1
    count.most_common() #计算每个单词的最高频率

frequency=count.most_common() #定义frequency
type(frequency) 

with open ('word_and_frequecy.csv','w')as f:
    mywriter=csv.writer(f) #用CSV的格式来写f
    header=['word','frequency'] 
    mywriter.writerow(header) 
    mywriter.writerows(frequency)