---
layout:     post
title:      "Quick_start_python_Lessons_6"
subtitle:   " \"dict and tuple\""
date:       2019-06-09 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Python Quick start
---

## 前言

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

元組(tuple)和列表(list)的形式很像, 但列表可以被修改, 元組不可以  
由此決定了元組可以使用什麼語法, 例如取出目標值, 求總和等等
由於元組不可修改, 因此像append, pop等等全部不可使用  
元組常見於描迷資料的形狀(data.shape)  
例如一張150x150的彩色相片的資料就是(150,150,3)

    tuple_a = (0,1,2,3,4,5)
    tuple_b = (0,'a',2,'b',4,'c')
    print("tuple_a[1]:", tuple_a[1])    #取出目標值
    print("sum(tuple_a):",sum(tuple_a) )    #求總和
    print("tuple_b:", tuple_b)    #不同的數據類型也可儲存
    
字典dict的用處很多, 特點是形成資料間的對應關係, 例如:  

    dict_a = {}
    dict_a['user_1'] = 'sam'
    dict_a['user_2'] = 'mary'
    dict_a['user_3'] = 'hon20002000'
    dict_b = {}
    dict_b['house_1'] = 3000
    dict_b['house_2'] = 5000
    dict_b['house_3'] = 7000
    print("dict_a:", dict_a)
    print("dict_b:", dict_b)

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



