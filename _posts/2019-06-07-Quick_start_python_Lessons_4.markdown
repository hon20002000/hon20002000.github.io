---
layout:     post
title:      "Quick_start_python_Lessons_4"
subtitle:   " \"If, elif, else and while\""
date:       2019-06-07 16:00:00
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

if用來判斷條件是否成立, 然後運行if裡面的語句  
例如條件成立時

    num_1 = 3
    if num_1 > 2:
        print("success")
    print("if test")    
    =========== result ==========
    success
    if test  
  
當條件不成立, 自然不會運行裡面的語法

    num_1 = 3
    if num_1 > 4:
        print("success")
    print("if test")    
    =========== result ==========
    if test  
    
當if裡面還有多層if(或其他語法), 則繼續判斷內層語法 

    num_1 = 3
    if num_1 > 4:
        print("success_1")
        if num_1 == 3:
            print("success_2")
            if num_1 == 'a':
                print("success_3")
    print("if test")    
    =========== result ==========
    success_1
    success_2
    if test 
   
下面是基本的if, elif(其他語言的else if), else語法  
一個if判斷句可以沒有elif, 也可以沒有else, 如何使用隨自己的邏輯而定

    a = 10
    b = 5
    if a == b:
        print("a=b")
    elif a < b:
        print("a<b")
    else:
        print("a>b")
    =========== result ==========
    a>b
         
while的用法是, 只要符合條件便會無限循環  
因此while必須設定停止點, 另外一種方法是使用break跳出迴圈  
    
    #case_1
    a = 10
    while a>7:
        print(a)  #這是無限循環
    =========== result ==========
    10
    10
    10
    ...etc    #無限循環時按ctrl+c可停止
    
    #case_2
    a = 10
    while a>7:
        a = a-1    #設置停止點
        print(a)
    =========== result ==========
    9
    8
    7    
        
    #case_3
    a = 10
    while True:    #
        a = a-1   
        print(a)
        if a < 8:
            break     #設置跳出點
    =========== result ==========
    9
    8
    7 

    #case_4
    a = 10
    running = True
    while running:
        a = a-1   
        print(a)
        if a < 8:
            running = False     #設置跳出點
    =========== result ==========
    9
    8
    7 

以上方法是常見的while寫法

<p id = "build"></p>
---
    
 
## 練習


(a) 三個整數x, y, z = 1, 2, 3  
如果用if判斷大小, 並用print列出它們(使用a>b>c)的形式?

(b) 有4個數字1,2,3,4作不重覆任意排列, 用for或if等語法把它們所有可能的排序列出  
例如1,2,3,4 或 3, 1, 2, 4
  
(c) 列出1~100之間的所有質數(例如2,3,5,7,11,13,17,19...), 並計算個數  
hint:(1)使用列表生成1~100的數, 然後通過刪除法得出剩餘的質數 
     (2)質數不能被1以外的小於或等於自己的數整除   
     (3)整數N的最大因數小於或等於sqrt(N), 因為N = k**2 

(d) 寫出1/2+2/3+3/4+...20/21的值之和?(ANS:16.40226...)
hint:用for及while各寫1次

