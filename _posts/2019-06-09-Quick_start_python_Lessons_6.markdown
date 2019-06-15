---
layout:     post
title:      "Quick_start_python_Lessons_6"
subtitle:   " \"function\""
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

函數是為了讓整個程式更簡潔和易讀而編寫的, 也可以將特定功能的一段程序包裝起來重覆使用  
例如:

    def print_hello():    #函數的命名一般使用"動詞", 其他變數均使用"名詞"
        print("my name is John, nice to meet you!")

這就是使用函數把print("my name is John, nice to meet you!")包裝起來  
函數設定後並不會使用, 例如上式便不會print出任何東西, 注意函數須使用def及(:)  
裡面的內容須縮進4個空格或1個tab  

    def print_hello():
        print("my name is John, nice to meet you!")
    
    print_hello()
    print_hello()
    print_hello()
    =========== result ==========
    my name is John, nice to meet you!
    my name is John, nice to meet you!
    my name is John, nice to meet you!

這樣便運行了3次函數print_hello(), 函數可以在()內加入變數, 供函數內部使用  

    def print_hello(name):
        print("my name is {}, nice to meet you!".format(name))
    
    print_hello('John')
    print_hello('Mary')
    print_hello('Susan')
    =========== result ==========
    my name is John, nice to meet you!
    my name is Mary, nice to meet you!
    my name is Susan, nice to meet you!
    
當傳遞給函數的變數多於1個時, 順序是必須的  

    def print_hello(name, age):
        print("my name is {}, I am {} years ago!".format(name, age))
    
    print_hello('John', 3)
    print_hello(4, 'Mary')
    =========== result ==========
    my name is John, I am 3 years ago!
    my name is 4, I am Mary years ago!

使用此方式可無視順序  

    def print_hello(name, age):
        print("my name is {}, I am {} years ago!".format(name, age))
    
    print_hello(age=4, name='Mary')
    =========== result ==========
    my name is Mary, I am 4 years ago!

因此在使用函數時必須清楚函數有多少個變數需要傳遞, 以及變數的名稱是什麼  
下面是函數錯誤的使用例子  

    def print_hello(name, age, school):
        print("my name is {}, I am {} years ago, I study in {}!".format(name, age, school))

    print_hello('Mary')
    =========== result ==========
    TypeError: print_hello() missing 2 required positional arguments: 'age' and 'school'
   

函數可定義默認值(default值), 不輸入其他值時自動傳入默認值    

    def print_hello(name, school='KaoYip'):
        print("my name is {}, I study in {}!".format(name, school))

    print_hello('Mary')
    print_hello('Mary', 'CDSJ5' )   
    =========== result ==========
    my name is Mary, I study in KaoYip!
    my name is Mary, I study in CDSJ5!

函數的結尾使用return表示輸出結果(返回值)      

    def calucale(x):
        y = 3*x + 4
        return y

    result = calucale(10)
    print("result:", result)   
    =========== result ==========
    result: 34

return多個返回值     

    def calucale(x):
        y = 3*x + 4
        z = -2*x + 1
        return y, z

    result_1, result_2 = calucale(10)
    print("result_1:", result_1)   
    print("result_2:", result_2) 
    =========== result ==========
    result: 34
    result: -19
    
<p id = "build"></p>
---
    
## 練習


(a) 利用函數生成字典, 可以應用在生成機器學習的Label之中:  
    現在有3筆資料
    - apple, 3個
    - orange, 5個
    - waterlemon, 10個
    試用函數傳遞參數的方式生成字典fruits = {'apple':3, 'orange':5, 'waterlemon':10}, 例如  
    
    def make_fruit_dict(fruit_1, fruit_2, fruit_3):
        ...etc

(b) 函數可以傳遞列表, 例如:

    usernames = ['John', 'Mary', 'Susan']
    def list_name(users):
        print("user1:", users[0])
        print("user2:", users[1])
        print("user3:", users[2])
    
    list_name(usernames)
    =========== result ==========
    user1: John
    user2: Mary
    user3: Susan
    
若usernames列表的的數量不回定, 如何編寫合適的函數來print出所有的user?
hint:使用for user in uesrs:


(c) 編寫等差數列的前n項和函數, def sum_ap(a1, an, d):  
    傳入首項a1, an及d, 可以自動求出項數n, 並且return Sn的值