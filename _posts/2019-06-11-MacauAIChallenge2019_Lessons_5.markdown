---
layout:     post
title:      "MacauAIChallenge2019_Lessons_5"
subtitle:   " \"If, read and write\""
date:       2019-06-11 16:00:00
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
>>教得十分仔細, 若想深入python的進階用法可以查看他的內容   

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
         

<p id = "build"></p>
---

開啟文件應該是學習python中最重要的語法, 開啟圖片, 文件的方法有少許不同  
但必須記著開啟了文件必須在使用後關閉, 否則可能會有error或資料沒有儲存等等  
在[MacauAIChallenge2019_pythonLessons](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)裡面下載csv_1.csv檔案  
把這個csv檔放在你python的資料夾同一目錄, 就可以讀取出來
裡面描述了4個人的姓名,身高,年齡, 試把他們用for列印出來, 下面的程式碼可以打開csv檔

    #methon_1
    file =  open('csv_1.csv')   
    content = file.readlines()    #把文件一次過讀完, 儲存方法是每行讀取一次, 並保存在content中
    print(content)    #content是list
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
method_2比較難理解但更完善, 利用try, except語法確保最後能關閉檔案  
method_3最簡潔也最完善, python內置語法with open() as xxx:  
當python內部開啟檔案之後必定自動關閉檔案(無論是否出現error)    

    
在python中可以簡化寫成如下, 注意python不用寫{ }, 而是用縮進4個空格或1個tab來表示巢狀結構    

    for i in range(3):
        print("i:", i)
    =========== result ==========
    i: 0
    i: 1
    i: 2

也可以換個方式寫成  

    for i in range(0,3):
        print("i:", i)
    =========== result ==========
    i: 0
    i: 1
    i: 2




    
    
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

(e) 在[MacauAIChallenge2019_pythonLessons](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)裡面下載一個csv_1.csv檔案  
把這個csv檔放在你python的資料夾同一目錄, 就可以讀取出來
裡面描述了4個人的姓名,身高,年齡, 試把他們用for列印出來, 下面的程式碼可以打開csv檔

    with open('csv_1.csv) as f:
        content = f.readlines()
        print(content)
    =========== result ==========
    list_a: [1,2,3,4,5,6]
    list_b: [1,2,3,4,5,6]

