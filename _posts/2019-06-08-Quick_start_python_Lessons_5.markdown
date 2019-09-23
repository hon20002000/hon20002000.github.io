---
layout:     post
title:      "Quick_start_python_Lessons_5"
subtitle:   " \"open, close, read and write\""
date:       2019-06-08 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Python Quick start
---

## 前言
  
'''  
作者: hon20002000   
最後更新: 2019/9/17    
'''   
  
本教程是為了讓同學們快速體驗機器學習/深度學習而設計的.  
裡面只學習最常用的python語法.

>想更深入了解python, 網上資源可以看[廖雪峰的python教學網站](https://www.liaoxuefeng.com/wiki/1016959663602400)  
>或是[RUNOOB.com](http://www.runoob.com/python/python-tutorial.html)python教程
>教得十分仔細, 若想深入python的進階用法可以查看他們的內容   

教程用法:  
>>閱讀本blog上的基礎語法  
>>完成每篇文章的作業  
>>部分學習所需的檔案在[github](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)下載  
>>遇到問題或其他改善建議可在下面留言


<p id = "build"></p>
---

## 正文

開啟文件是學習python中最重要的語法, 開啟不同文件方法是不一樣的  
但必須記著開啟了文件必須在讀取後關閉, 否則可能會有error出現    
下面程序需要在[MacauAIChallenge2019_pythonLessons](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)裡面下載csv_1.csv檔案  
把這個csv檔和下面的python程序放在同一個資料夾內, 就可以讀取出來, 否則需要修改路徑  
裡面描述了4個人的姓名,身高,年齡, 試把他們的全部資料用for及print列印出來  
  
<font color="#666600">  
     
## 打開csv文件的三種方法  
  
</font>   


    #methon_1
    file =  open('csv_1.csv')   
    content = file.readlines()    #把文件一次過讀完, 儲存方法是每行讀取一次, 並保存在content中
    print(content)    #content是list    #<---若程序在open和close中間出錯, 則close不了
    file.close()
    =========== result ==========
    ['name,height,age\n', 'john,170,17\n', 'mary,155,22\n', 'steven,158,21\n', 'sam,180,33']

    #methon_2
    try:
        file = open('csv_1.csv')
        content = file.readlines()    
    except:    #更加完善的方法, 利用try:來開啟檔案, 若中途出現error則使用except來關閉file
        file.close()
    finally:
        print(content)
        file.close()     
    =========== result ==========
    ['name,height,age\n', 'john,170,17\n', 'mary,155,22\n', 'steven,158,21\n', 'sam,180,33']
    
    #method_3
    with open('csv_1.csv') as f:
        content = f.readlines()    #把文件一次過讀完, 儲存方法是每行讀取一次, 並保存在content中
        print(content)    #content是list
    =========== result ==========
    ['name,height,age\n', 'john,170,17\n', 'mary,155,22\n', 'steven,158,21\n', 'sam,180,33']

method_1的程式碼較清晰, open() >> readlines() >> close()的流程  
但缺點是若程序出錯則文件不會自行關閉    
method_2比較難理解但更完善, 利用try, except語法確保最後能關閉檔案    
try, except是指若程式碼在try中出現error, 則運行except語法  
程序仍然會繼續運行  
method_3最簡潔也最完善, python內置語法with open() as xxx:    
xxx是自定義旳名稱, 後面可以運用xxx.read或xxx.write等等  
此寫法的好處是當python開啟檔案之後必定自動關閉檔案(無論是否出現error)  
上面三個方法可以選擇一個適當的methon去開啟你的檔案~  
   
接下來我們學習產生一個txt檔並寫入資料  
我們可以使用'w'寫入文件或是'a'寫入文件  
'w'的特點是開啟檔案後, 先<清除>文件內容, 再從頭寫入  
'a'的特點是開啟檔案後, 在文件的末端接著寫入

    path ='abc.txt'
    file = open(path, 'w')    
    file.write('student,scores\n')
    file.write('A,55\n')
    file.write('B,36\n')
    file.write('C,80\n')
    file.write('D,77\n')
    file.write('E,99\n')
    file.close()

<img src="/img/aaa.png" width="40%">  

下面我們把txt檔案改為csv檔, 我們可以手動改副檔名  
也可以利用python的一些module把它改掉
    
    #method_1
    import os
    os.rename('abc.txt', 'abc.csv')
    
    #method_2
    import shutil
    shutil.move('abc.txt', 'abc.csv')    

<img src="/img/csv.png" width="40%">  
可以看到abc.txt已經改為abc.csv了  
csv檔的全稱是Comma Separated Value  
它在machine learning或是deep learning都會用到  
因為它的儲存格式是用","逗號分隔, 大家有了這種共識後  
讀取或寫入檔案就會方便很多  
  
我們試著把文件的內容讀取出來, 我們可以使用read(), readline(), readlines()三種方式  
  
    #method_1
    path ='abc.csv'
    file = open(path, 'r')    #open的默認條件是'r', 'r'可寫也可不寫  
    content_1 = file.read()
    print("content_1:", content_1)
    content_2 = file.read()
    print("content_2:", content_2)
    =========== result ==========    
    content_1: student,scores    #可看出read()是一次全部讀取所有內容, content_2沒有任何輸出
    A,55
    B,36
    C,80
    D,77
    E,99
    
    content_2: 
     
    #method_2
    path ='abc.csv'
    file = open(path, 'r')   
    content_1 = file.readline()
    print("content_1:", content_1, end='')   #print()默認end='\n', 會自動換行, 加上end=''不換行
    content_2 = file.readline()
    print("content_2:", content_2)
    =========== result ==========    
    content_1: student,scores    #可看出readline()每次只讀一行
    content_2: A,55

    #method_3
    path ='abc.csv'
    file = open(path, 'r')    
    contents = file.readlines()    #把file全部逐行讀入
    print("contents:", contents)    #readlines已經保存為list
    for content in contents:
        print(content, end='')
    =========== result ==========  
    contents: ['student,scores\n', 'A,55\n', 'B,36\n', 'C,80\n', 'D,77\n', 'E,99\n']
    content_1: student,scores    
    A,55
    B,36
    C,80
    D,77
    E,99

一般來說readlines()比較好用, 因為轉為list之後可以控制輸出那一行內容  

讀取csv檔的技巧:

    path ='abc.csv'
    file = open(path, 'r')     
    contents = file.readlines()    
    for content in contents:
        student = content.split(',')[0]
        score = content.split(',')[1]
        print("{}: {}".format(student, score), end='')    #.format()可以在{}裡輸出內容
    =========== result ==========  
    A: 55
    B: 36
    C: 80
    D: 77
    E: 99

<p id = "build"></p>
---


    
## 練習


(a) 利用write生成一個txt檔案, 裡面寫入5名學生的名字及數學及英文成績, 儲存成為csv檔, 例如命名為score.csv  
格式類似於:  
    
    student,math,eng\n
    sam,59,77\n
    mary,88,46\n
    ...etc

(b) 利用上面生成的score.csv檔, 利用readlines(), print出各位學生的成績  
利用list來找出數學科或英文科最高、最低分的學生, 以及各科的平均成績  
hint:   
(1)由於readlines()的list的第一行是字串student,math,eng, 因此第一行並不是我們要的資料  
我們可以用list[1:]來獲取正確的資料  
(2)我們讀取csv檔時, 可以用split(',')[0]及split(',')[1]...來取出不同位置的資料  
  
## 解答  
  
#(a)  
  
    #path ='homework.txt'
    path ='homework.csv'
    file = open(path, 'w')    
    file.write('student,math,english\n')
    file.write('A,55,80\n')
    file.write('B,36,44\n')
    file.write('C,80,78\n')
    file.write('D,77,62\n')
    file.write('E,99,77\n')
    file.close()
    print("done!")
  
#(b)  
  
    with open('homework.csv') as f:
        contents = f.readlines()    #把文件一次過讀完, 儲存方法是每行讀取一次, 並保存在contet中
        print(contents)    #contents是list
        print(contents[1:])    

    math_sum = []
    eng_sum = []
    average = 0
    for content in contents[1:]:
        math = int(content.split(',')[1])
        math_sum.append(math)
        print(math)    #math

    print("math_max:", max(math_sum))
    print("math_min:", min(math_sum))
    print('-'*30)  

    for content in contents[1:]:
        eng = content.split(',')[2].replace("\n", "")    #english
        eng_sum.append(eng)

    print(eng_sum)    #math

    print("eng_max:", max(eng_sum))
    print("eng_min:", min(eng_sum))
    =========== result ==========  
    ['student,math,english\n', 'A,55,80\n', 'B,36,44\n', 'C,80,78\n', 'D,77,62\n', 'E,99,77\n']
    ['A,55,80\n', 'B,36,44\n', 'C,80,78\n', 'D,77,62\n', 'E,99,77\n']
    55
    36
    80
    77
    99
    math_max: 99
    math_min: 36
    ------------------------------
    ['80', '44', '78', '62', '77']
    eng_max: 80
    eng_min: 44

使用pandas和numpy庫可以更好地處理資料  
pandas和numpy是作數據處理的標準流程  
往後會進一步講解numpy和pandas的使用方法  

#(b)  
  
    import pandas as pd
    import numpy as np
    contents = pd.read_csv('homework.csv')
    content = pd.DataFrame(contents)
    print(content)
    print('-'*30)
    print(content['math'])
    print("math_mean:", np.mean(content['math']))
    print("math_max:", np.max(content['math']))
    print("math_min:", np.min(content['math']))
    print('-'*30)
    print(content['english'])
    print("english_mean:", np.mean(content['english']))
    print("english_max:", np.max(content['english']))
    =========== result ==========      
          student  math  english
    0       A    55       80
    1       B    36       44
    2       C    80       78
    3       D    77       62
    4       E    99       77
    ------------------------------
    0    55
    1    36
    2    80
    3    77
    4    99
    Name: math, dtype: int64
    math_mean: 69.4
    math_max: 99
    math_min: 36
    ------------------------------
    0    80
    1    44
    2    78
    3    62
    4    77
    Name: english, dtype: int64
    english_mean: 68.2
    english_max: 80
    english_min: 44
        print("english_min:", np.min(content['english']))



